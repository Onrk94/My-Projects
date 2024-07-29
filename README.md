In this project, we summarize children's activities at school and inform their parents via email.

Project Description:

In this project, we aim to summarize the daily activities of children in a kindergarten and provide weekly summaries to their parents via email. The system is designed to:

Track Activities: Record various activities that children engage in during their time at the kindergarten, such as learning sessions, playtime, reading, and other educational tasks.

Summarize Activities: Utilize advanced natural language processing (NLP) models to generate concise summaries of the recorded activities. This includes using models like Facebook's OPT-350m for summarization.

Group by Week: Aggregate the activities on a weekly basis to provide a comprehensive overview of what each child has done throughout the week.

Generate Human-Friendly Summaries: Transform the summarized text into a narrative format that is easy for parents to read and understand. This involves proper sentence structuring and capitalization.

Send Emails: Automatically send the generated summaries to the parents' email addresses, ensuring they are kept informed about their child's progress and activities at the kindergarten.

Technical Details
Database Management: We use SQLite to store and manage the activities and related data.
Natural Language Processing: The project leverages transformers and NLP models from the Hugging Face library to perform text summarization.
Email Automation: The project integrates email automation to send the weekly summaries to parents.
Data Processing: Pandas is used for data manipulation and aggregation.
Text Cleaning and Tokenization: NLTK is used for text processing, including tokenization and cleaning.
Workflow
Data Collection: Activities are recorded in an SQLite database, including details like the activity type, description, date, and associated student.
Data Aggregation: The data is grouped by student and week using Pandas.
Text Summarization: The grouped activities are summarized using a pre-trained NLP model.
Email Composition: The summarized text is formatted into a human-friendly narrative.
Email Delivery: The formatted summaries are sent to the parents via email.
This project aims to bridge the communication gap between kindergartens and parents, ensuring that parents are well-informed about their child's daily and weekly activities in an efficient and automated manner.

