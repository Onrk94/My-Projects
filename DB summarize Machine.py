import sqlite3
from transformers import AutoModelForCausalLM, AutoTokenizer
import nltk
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

load_dotenv()

DB_PATH = os.getenv('DB_PATH', 'C:/Users/onrku/Desktop/KinderGartenDB/school.db')
MODEL_NAME = os.getenv('MODEL_NAME', 'facebook/opt-350m')
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def fetch_data():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT Notes, s.Name, a.Date, p.Email
        FROM Activities AS a
        JOIN Students AS s ON a.Student_id = s.ID
        JOIN Parents AS p ON s.ID = p.Student_ID
        WHERE a.Date IS NOT NULL AND s.Name IS NOT NULL AND Notes IS NOT NULL
        ORDER BY a.Date
        """)
        return cursor.fetchall()

def process_data(text_records):
    data = pd.DataFrame(text_records, columns=["Notes", "Name", "Date", "ParentEmail"])
    data.dropna(inplace=True)
    data['Date'] = pd.to_datetime(data['Date'])
    return data.groupby(["Name", pd.Grouper(key="Date", freq="W-SUN"), "ParentEmail"])["Notes"].apply(' '.join).reset_index()

def summarize_text(text, model, tokenizer):
    encoded_input = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(encoded_input['input_ids'], max_length=400, num_beams=2, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def make_human_friendly(summary):
    sentences = nltk.sent_tokenize(summary)
    return ' '.join(sentence.capitalize() for sentence in sentences) + '.'

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to: {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

    text_records = fetch_data()
    weekly_data = process_data(text_records)

    for row in weekly_data.itertuples():
        student_name = row.Name
        week_start = row.Date.strftime("%Y-%m-%d")
        week_end = (row.Date + pd.Timedelta(days=6)).strftime("%Y-%m-%d")
        notes = row.Notes
        parent_email = row.ParentEmail

        summary = summarize_text(notes, model, tokenizer)
        human_friendly_summary = make_human_friendly(summary)

        summary_text = f"{student_name} had an exciting week at School from {week_start} to {week_end}. {human_friendly_summary}"

        print(summary_text)

        email_subject = f"Weekly Summary for {student_name} ({week_start} - {week_end})"
        send_email(parent_email, email_subject, summary_text)

    # Veritabanı bağlantısını kapat
    get_db_connection().close()

if __name__ == "__main__":
    main()
