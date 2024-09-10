# Automated Birthday Wisher App

This Python project automatically sends birthday wishes to your contacts via email. It reads a CSV file containing the list of birthdays, selects a random birthday letter from a set of templates, replaces placeholders with the actual names and sender details, and emails the personalized message.

## Features
- Reads birthdays from a CSV file.
- Automatically sends personalized email reminders on the person's birthday.
- Uses SMTP to send emails.
- Ability to choose between multiple birthday letter templates.
- Can be scheduled to run daily for automatic birthday reminders.

## Requirements

To run this project, you need to install the following libraries:

```bash
pip install pandas
pip install smtplib
```

## How to Use

1. **Prepare the Birthday Data:**
   - There is a CSV file named `birthdays.csv` that contains the following columns:
     - `Name`: The name of the person.
     - `Email`: The email address of the person.
     - `Year`, `Month`, `Day`: The birthday date broken down into these columns.
       
   You can simply add the emails and birthday dates here.
   
   Example CSV format:
   ```csv
   name,email,year,month,day
   John Doe,john@example.com,1990,09,25
   Jane Smith,jane@example.com,1985,12,01
   ```

2. **Set Up Email Configuration:**
   - In the `main.py` file, edit the sender’s email and app password for SMTP. You can also change the sender's name.
   ```python
   SENDER = "YOUR NAME"
   SENDER_EMAIL = "YOUR_EMAIL@example.com"
   PASSWORD = "APP PASSWORD"
   ```

   If you're using **Gmail**, the SMTP configuration should look like this:
   ```python
   with smtplib.SMTP("smtp.gmail.com") as connection:
       connection.starttls()
       connection.login(user=SENDER_EMAIL, password=PASSWORD)
   ```

   > **Note:** If you're using Gmail, you may need to enable "Less secure apps" in your Gmail settings or use an app-specific password for this script to work.

   **For other email providers**, you will need to change the SMTP server and port accordingly. Here are some examples:
   - **Yahoo Mail:**
     ```python
     with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
         connection.starttls()
         connection.login(user=SENDER_EMAIL, password=PASSWORD)
     ```
   - **Outlook/Hotmail:**
     ```python
     with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
         connection.starttls()
         connection.login(user=SENDER_EMAIL, password=PASSWORD)
     ```
   - **Zoho Mail:**
     ```python
     with smtplib.SMTP("smtp.zoho.com", 587) as connection:
         connection.starttls()
         connection.login(user=SENDER_EMAIL, password=PASSWORD)
     ```

   Be sure to check the SMTP settings for your email provider and replace the `smtp.gmail.com` section of the code accordingly.

3. **Customize Birthday Letters:**
   - The project uses three different letter templates, located in the `letter_templates` folder. Each template uses placeholders `[NAME]` and `[SENDER]`.
     - `[NAME]` will be automatically replaced with the recipient's name from the `birthdays.csv` file.
     - `[SENDER]` will be replaced by the name you provided in the `SENDER` variable.

   You can edit the letters or add new ones by following the same format, just make sure to use the placeholders `[NAME]` and `[SENDER]`.

## Schedule the Script to Run Automatically

To schedule the script to run every day automatically, you can use **PythonAnywhere**, a free Python hosting platform.

### Instructions for PythonAnywhere:

1. **Create an Account:**
   - Go to [PythonAnywhere](https://www.pythonanywhere.com/) and create a free account.

2. **Upload Your Code:**
   - Once you're logged in, go to the "Files" tab.
   - Upload the `main.py`, `birthdays.csv`, and your `letter_templates` folder.

3. **Set Up a Scheduled Task:**
   - Go to the "Tasks" tab.
   - Click "Add a new scheduled task."
   - Choose the time when you want the script to run (e.g., every day at 8:00 AM).
   - In the "Command" field, enter the path to your Python script, for example:
     ```bash
     /home/yourusername/main.py
     ```
   - Click "Create" to schedule the task.

4. **Test the Script:**
   You can also test the script by running it in the PythonAnywhere console. Navigate to the "Consoles" tab, select a Python 3.x console, and run the script manually:
   ```bash
   python3 main.py
   ```

The script will now run automatically every day at the time you specified and send birthday emails to your contacts.

