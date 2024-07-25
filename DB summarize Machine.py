import sqlite3
from transformers import AutoModelForCausalLM, AutoTokenizer
import nltk
import pandas as pd
from collections import Counter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

nltk.download('punkt')
nltk.download('stopwords')

# Veritabanı dosya yolu
db_path = "C:/Users/onrku/Desktop/KinderGartenDB/school.db"

# Veritabanına bağlanın
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Özetlenecek metinlerin bulunduğu sütun
notes_column = 'Notes'

# Özetlenecek metinleri, öğrenci isimlerini ve tarihleri seçin
cursor.execute(f"""
SELECT {notes_column}, s.Name, a.Date, p.Email
FROM Activities AS a
JOIN Students AS s ON a.Student_id = s.ID
JOIN Parents AS p ON s.ID = p.Student_ID
WHERE a.Date IS NOT NULL AND s.Name IS NOT NULL AND {notes_column} IS NOT NULL
ORDER BY a.Date
""")
text_records = cursor.fetchall()

# Yapay zeka modeli adı (OPT özetleme için)
model_name = "facebook/opt-350m"

# Tokenizer ve modeli yükleyin
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Verileri bir DataFrame'e dönüştürün
data = pd.DataFrame(text_records, columns=["Notes", "Name", "Date", "ParentEmail"])

# Boş değerleri filtreleyip kaldırın
data.dropna(inplace=True)

# Verileri haftalara göre gruplandırın
data['Date'] = pd.to_datetime(data['Date'])
weekly_data = data.groupby(["Name", pd.Grouper(key="Date", freq="W-SUN"), "ParentEmail"])["Notes"].apply(' '.join).reset_index()


def summarize_text(text):
    encoded_input = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(encoded_input['input_ids'], max_length=400, num_beams=2, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


def make_human_friendly(summary):
    # Split the summary into sentences
    sentences = nltk.sent_tokenize(summary)

    # Create a human-friendly summary
    human_friendly_summary = []

    for sentence in sentences:
        human_friendly_summary.append(sentence.capitalize())

    # Join the sentences with proper punctuation
    return ' '.join(human_friendly_summary) + '.'


def send_email(to_email, subject, body):
    from_email = "your_email@gmail.com"
    from_password = "your_email_password"

    # E-posta içeriğini oluşturun
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # SMTP sunucusuna bağlanın ve e-posta gönderin
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"E-posta başarıyla gönderildi: {to_email}")
    except Exception as e:
        print(f"E-posta gönderilirken hata oluştu: {e}")


# Her hafta için özet oluşturun ve e-posta gönderin
for row in weekly_data.itertuples():
    student_name = row.Name
    week_start = row.Date.strftime("%Y-%m-%d")
    week_end = (row.Date + pd.Timedelta(days=6)).strftime("%Y-%m-%d")
    notes = row.Notes
    parent_email = row.ParentEmail

    # Metni özetleyin
    summary = summarize_text(notes)
    human_friendly_summary = make_human_friendly(summary)

    # Anlatımsal özet oluşturun
    summary_text = f"{student_name} had an exciting week at School from {week_start} to {week_end}. {human_friendly_summary}"

    # Özeti yazdırın
    print(summary_text)

    # Özeti e-posta olarak gönderin
    email_subject = f"Weekly Summary for {student_name} ({week_start} - {week_end})"
    send_email(parent_email, email_subject, summary_text)

connection.close()