#import sqlite3
#from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
#import nltk

#nltk.download('punkt')
#nltk.download('stopwords')

# Veritabanı dosya yolu
#db_path = "C:/Users/onrku/Desktop/KinderGartenDB/ai_garden1.db"

# Veritabanına bağlanın
#connection = sqlite3.connect(db_path)
#cursor = connection.cursor()

# Özetlenecek metnin bulunduğu sütun
#text_column = "Notes"

# Özetlenecek metinleri seçin
#cursor.execute(f"SELECT {text_column} FROM Activities")
#text_records = cursor.fetchall()
#from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Yapay zeka modeli adı
#model_name = "facebook/bart-base"

# Tokenizer ve modeli yükleyin
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
#for text_record in text_records:
#   text = text_record[0]  # Metni veritabanından alın
#    encoded_input = tokenizer(text, return_tensors="pt")  # Metni modele girecek şekilde kodlayın
#   summary = model.generate(**encoded_input)  # Özeti üretin
#   decoded_summary = tokenizer.decode(summary[0], skip_special_tokens=True)  # Özeti metne dönüştürün
#   print(f"Özet: {decoded_summary}")
#connection.close()




#import sqlite3
#from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
#import nltk

#nltk.download('punkt')
#nltk.download('stopwords')

# Veritabanı dosya yolu
#db_path = "C:/Users/onrku/Desktop/KinderGartenDB/ai_garden1.db"

# Veritabanına bağlanın
#connection = sqlite3.connect(db_path)
#cursor = connection.cursor()

# Özetlenecek metinlerin bulunduğu sütun
#notes_column = "Notes"

# Özetlenecek metinleri ve öğrenci isimlerini alacağımız tablolar
#activities_table = "Activities"
#students_table = "Students"

# Özetlenecek metinleri ve öğrenci isimlerini seçin
#cursor.execute(f"""
#SELECT {notes_column}, s.Name
#FROM {activities_table} AS a
#JOIN {students_table} AS s ON a.Student_id = s.ID
#""")
#text_records = cursor.fetchall()

# Yapay zeka modeli adı
#model_name = "facebook/bart-base"

# Tokenizer ve modeli yükleyin
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Her metni özetleyin ve öğrenci ismiyle birlikte yazdırın
#for text_record in text_records:
#   notes = text_record[0]  # Metni veritabanından alın
    #   student_name = text_record[1]  # Öğrenci ismini veritabanından alın

    # Metni özetleyin
    #    encoded_input = tokenizer(notes, return_tensors="pt")
    #    summary = model.generate(**encoded_input)
    #    decoded_summary = tokenizer.decode(summary[0], skip_special_tokens=True)

    # Özeti öğrenci ismiyle birlikte yazdırın
    #    print(f"**Student:** {student_name}")
    #    print(f"**Summary:** {decoded_summary}")

#connection.close()



#import sqlite3
#from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
#import nltk
#import pandas as pd

#nltk.download('punkt')
#nltk.download('stopwords')

# Veritabanı dosya yolu
#db_path = "C:/Users/onrku/Desktop/KinderGartenDB/ai_garden1.db"

# Veritabanına bağlanın
#connection = sqlite3.connect(db_path)
#cursor = connection.cursor()

# Özetlenecek metinlerin bulunduğu sütun
#notes_column = "Notes"

# Özetlenecek metinleri ve öğrenci isimlerini alacağımız tablolar
#activities_table = "Activities"
#students_table = "Students"

# Özetlenecek metinleri, öğrenci isimlerini ve tarihleri seçin
#cursor.execute(f"""
#SELECT {notes_column}, s.Name, a.Date
#FROM {activities_table} AS a
#JOIN {students_table} AS s ON a.Student_id = s.ID
#ORDER BY a.Date
#""")
#text_records = cursor.fetchall()

# Yapay zeka modeli adı (İngilizce özetleme için)
#model_name = "facebook/bart-large-cnn"

# Tokenizer ve modeli yükleyin
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Verileri bir DataFrame'e dönüştürün
#data = pd.DataFrame(text_records, columns=["Notes", "Name", "Date"])

# Verileri haftalara göre gruplandırın
#data['Date'] = pd.to_datetime(data['Date'])
#weekly_data = data.groupby(["Name", pd.Grouper(key="Date", freq="W-SUN")])["Notes"].apply(' '.join).reset_index()

# Her hafta için özet oluşturun
#for row in weekly_data.itertuples():
#  student_name = row.Name
    #   week_start = row.Date.strftime("%Y-%m-%d")
    #   week_end = (row.Date + pd.Timedelta(days=6)).strftime("%Y-%m-%d")
    #  notes = row.Notes

    # Metni özetleyin
    #    encoded_input = tokenizer(notes, return_tensors="pt", max_length=1024, truncation=True)
    #    summary_ids = model.generate(encoded_input['input_ids'], max_length=150, num_beams=4, early_stopping=True)
    #   decoded_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Özeti yazdırın
    #   print(f"**Student:** {student_name}")
    #   print(f"**Week:** {week_start} - {week_end}")
    #   print(f"**Summary:** {decoded_summary}\n")

#connection.close()




#import sqlite3
#from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
#import nltk
#import pandas as pd

#nltk.download('punkt')
#nltk.download('stopwords')

# Veritabanı dosya yolu
#db_path = "C:/Users/onrku/Desktop/KinderGartenDB/ai_garden1.db"

# Veritabanına bağlanın
#connection = sqlite3.connect(db_path)
#cursor = connection.cursor()

# Özetlenecek metinlerin bulunduğu sütun
#notes_column = "Notes"

# Özetlenecek metinleri ve öğrenci isimlerini alacağımız tablolar
#activities_table = "Activities"
#students_table = "Students"

# Özetlenecek metinleri, öğrenci isimlerini ve tarihleri seçin
#cursor.execute(f"""
#SELECT {notes_column}, s.Name, a.Date
#FROM {activities_table} AS a
#JOIN {students_table} AS s ON a.Student_id = s.ID
#ORDER BY a.Date
#""")
#text_records = cursor.fetchall()

# Yapay zeka modeli adı (İngilizce özetleme için)
#model_name = "facebook/bart-large-cnn"

# Tokenizer ve modeli yükleyin
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Verileri bir DataFrame'e dönüştürün
#data = pd.DataFrame(text_records, columns=["Notes", "Name", "Date"])

# Verileri haftalara göre gruplandırın
#data['Date'] = pd.to_datetime(data['Date'])
#weekly_data = data.groupby(["Name", pd.Grouper(key="Date", freq="W-SUN")])["Notes"].apply(' '.join).reset_index()

# Her hafta için özet oluşturun
#for row in weekly_data.itertuples():
    #student_name = row.Name
    #week_start = row.Date.strftime("%Y-%m-%d")
    #week_end = (row.Date + pd.Timedelta(days=6)).strftime("%Y-%m-%d")
    #notes = row.Notes

    # Metni özetleyin
    #encoded_input = tokenizer(notes, return_tensors="pt", max_length=512, truncation=True)
    #summary_ids = model.generate(encoded_input['input_ids'], max_length=150, num_beams=2, early_stopping=True)
    #decoded_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Anlatımsal özet oluşturun
    #summary_text = f"This week, {student_name} engaged in various activities. {decoded_summary}. Overall, it was a week filled with learning and fun."

    # Özeti yazdırın
    #print(f"**Student:** {student_name}")
    #print(f"**Week:** {week_start} - {week_end}")
    #   print(f"**Summary:** {summary_text}\n")

#connection.close()






#import sqlite3
#from transformers import AutoModelForCausalLM, AutoTokenizer
#import nltk
#import pandas as pd

#nltk.download('punkt')
#nltk.download('stopwords')

# Veritabanı dosya yolu
#db_path = "C:/Users/onrku/Desktop/KinderGartenDB/ai_garden1.db"

# Veritabanına bağlanın
#connection = sqlite3.connect(db_path)
#cursor = connection.cursor()

# Özetlenecek metinlerin bulunduğu sütun
#notes_column = "Notes"

# Özetlenecek metinleri ve öğrenci isimlerini alacağımız tablolar
#activities_table = "Activities"
#students_table = "Students"

# Özetlenecek metinleri, öğrenci isimlerini ve tarihleri seçin
#cursor.execute(f"""
#SELECT {notes_column}, s.Name, a.Date
#FROM {activities_table} AS a
#JOIN {students_table} AS s ON a.Student_id = s.ID
#ORDER BY a.Date
#""")
#text_records = cursor.fetchall()

# Yapay zeka modeli adı (OPT özetleme için)
#model_name = "facebook/opt-350m"

# Tokenizer ve modeli yükleyin
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForCausalLM.from_pretrained(model_name)

# Verileri bir DataFrame'e dönüştürün
#data = pd.DataFrame(text_records, columns=["Notes", "Name", "Date"])

# Verileri haftalara göre gruplandırın
#data['Date'] = pd.to_datetime(data['Date'])
#weekly_data = data.groupby(["Name", pd.Grouper(key="Date", freq="W-SUN")])["Notes"].apply(' '.join).reset_index()

#def summarize_text(text):
    #encoded_input = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    #summary_ids = model.generate(encoded_input['input_ids'], max_length=150, num_beams=2, early_stopping=True)
    #summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    #return summary

# Her hafta için özet oluşturun
#for row in weekly_data.itertuples():
    #student_name = row.Name
    #week_start = row.Date.strftime("%Y-%m-%d")
    #week_end = (row.Date + pd.Timedelta(days=6)).strftime("%Y-%m-%d")
    #notes = row.Notes

    # Metni özetleyin
    #summary = summarize_text(notes)

    # Anlatımsal özet oluşturun
    #summary_text = f"This week, {student_name} had an exciting time at kindergarten! {summary} We had so much fun learning and growing together."

    # Özeti yazdırın
    # print(f"**Student:** {student_name}")
    # print(f"**Week:** {week_start} - {week_end}")
    # print(f"**Summary:** {summary_text}\n")

#connection.close()



#import sqlite3
#from transformers import AutoModelForCausalLM, AutoTokenizer
#import nltk
#import pandas as pd
#from collections import Counter

#nltk.download('punkt')
#nltk.download('stopwords')

# Veritabanı dosya yolu
#db_path = "C:/Users/onrku/Desktop/KinderGartenDB/ai_garden1.db"

# Veritabanına bağlanın
#connection = sqlite3.connect(db_path)
#cursor = connection.cursor()

# Özetlenecek metinlerin bulunduğu sütun
#notes_column = "Notes"

# Özetlenecek metinleri ve öğrenci isimlerini alacağımız tablolar
#activities_table = "Activities"
#students_table = "Students"

# Özetlenecek metinleri, öğrenci isimlerini ve tarihleri seçin
#cursor.execute(f"""
#SELECT {notes_column}, s.Name, a.Date
#FROM {activities_table} AS a
#JOIN {students_table} AS s ON a.Student_id = s.ID
#ORDER BY a.Date
#""")
#text_records = cursor.fetchall()

# Yapay zeka modeli adı (OPT özetleme için)
#model_name = "facebook/opt-350m"

# Tokenizer ve modeli yükleyin
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForCausalLM.from_pretrained(model_name)

# Verileri bir DataFrame'e dönüştürün
#data = pd.DataFrame(text_records, columns=["Notes", "Name", "Date"])

# Verileri haftalara göre gruplandırın
#data['Date'] = pd.to_datetime(data['Date'])
#weekly_data = data.groupby(["Name", pd.Grouper(key="Date", freq="W-SUN")])["Notes"].apply(' '.join).reset_index()


#def summarize_text(text):
    #encoded_input = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    #summary_ids = model.generate(encoded_input['input_ids'], max_length=150, num_beams=2, early_stopping=True)
    #summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    #return summary


#def make_human_friendly(summary):
    # Split the summary into activities
    #activities = summary.split(' ')

    # Count occurrences of each activity
    #activity_counts = Counter(activities)

    # Create a human-friendly summary
    #human_friendly_summary = []

    #for activity, count in activity_counts.items():
        #if count > 1:
            #human_friendly_summary.append(f"{activity} {count} times.")
            #else:
            #human_friendly_summary.append(f"{activity}.")

    # Join the activities with proper punctuation
    #return ' '.join(human_friendly_summary)


# Her hafta için özet oluşturun
#for row in weekly_data.itertuples():
    #student_name = row.Name
    #week_start = row.Date.strftime("%Y-%m-%d")
    #week_end = (row.Date + pd.Timedelta(days=6)).strftime("%Y-%m-%d")
    #notes = row.Notes

    # Metni özetleyin
    #summary = summarize_text(notes)
    #human_friendly_summary = make_human_friendly(summary)

    # Anlatımsal özet oluşturun
    #summary_text = f"This week, {student_name} had an exciting time at kindergarten! {human_friendly_summary} We had so much fun learning and growing together."

    # Özeti yazdırın
    #print(f"**Student:** {student_name}")
    #print(f"**Week:** {week_start} - {week_end}")
    #print(f"**Summary:** {summary_text}\n")

#connection.close()


#import sqlite3
#from transformers import AutoModelForCausalLM, AutoTokenizer
#import nltk
#import pandas as pd
#from collections import Counter

#nltk.download('punkt')
#nltk.download('stopwords')

# Veritabanı dosya yolu
#db_path = "C:/Users/onrku/Desktop/KinderGartenDB/school.db"

# Veritabanına bağlanın
#connection = sqlite3.connect(db_path)
#cursor = connection.cursor()

# Özetlenecek metinlerin bulunduğu sütun
#notes_column = "Notes"

# Özetlenecek metinleri ve öğrenci isimlerini alacağımız tablolar
#activities_table = "Activities"
#students_table = "Students"

# Özetlenecek metinleri, öğrenci isimlerini ve tarihleri seçin
#cursor.execute(f"""
#SELECT {notes_column}, s.Name, a.Date
#FROM {activities_table} AS a
#JOIN {students_table} AS s ON a.Student_id = s.ID
#WHERE a.Date IS NOT NULL AND s.Name IS NOT NULL AND {notes_column} IS NOT NULL
#ORDER BY a.Date
#""")
#text_records = cursor.fetchall()

# Yapay zeka modeli adı (OPT özetleme için)
#model_name = "facebook/opt-350m"

# Tokenizer ve modeli yükleyin
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForCausalLM.from_pretrained(model_name)

# Verileri bir DataFrame'e dönüştürün
#data = pd.DataFrame(text_records, columns=["Notes", "Name", "Date"])

# Boş değerleri filtreleyip kaldırın
#data.dropna(inplace=True)

# Verileri haftalara göre gruplandırın
#data['Date'] = pd.to_datetime(data['Date'])
#weekly_data = data.groupby(["Name", pd.Grouper(key="Date", freq="W-SUN")])["Notes"].apply(' '.join).reset_index()


#def summarize_text(text):
    #encoded_input = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    #summary_ids = model.generate(encoded_input['input_ids'], max_length=400, num_beams=2, early_stopping=True)
    #summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    #   return summary


#def make_human_friendly(summary):
    # Split the summary into sentences
    #sentences = nltk.sent_tokenize(summary)

    # Create a human-friendly summary
    #human_friendly_summary = []

    #   for sentence in sentences:


#   human_friendly_summary.append(sentence.capitalize())

    # Join the sentences with proper punctuation
    #return ' '.join(human_friendly_summary) + '.'


# Her hafta için özet oluşturun
#for row in weekly_data.itertuples():
    #student_name = row.Name
    #week_start = row.Date.strftime("%Y-%m-%d")
    #week_end = (row.Date + pd.Timedelta(days=6)).strftime("%Y-%m-%d")
    #notes = row.Notes

    # Metni özetleyin
    #summary = summarize_text(notes)
    #human_friendly_summary = make_human_friendly(summary)

    # Anlatımsal özet oluşturun
    #summary_text = f"{student_name} had an exciting week at School from {week_start} to {week_end}. {human_friendly_summary}"

    # Özeti yazdırın
    #   print(summary_text)

#connection.close()





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
db_path = "C:/Users/onrku/Desktop/KinderGartenDB/ai_garden.db"

# Veritabanına bağlanın
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Özetlenecek metinlerin bulunduğu sütun
notes_column = "Notes"

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

