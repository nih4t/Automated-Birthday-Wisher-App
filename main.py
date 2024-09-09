import smtplib
import datetime as dt
import pandas as pd

SENDER = "Your Name"
SENDER_EMAIL = "tstccnt0101@gmail.com"
# Must use app password for safety
PASSWORD = "zwki uznn hgen xvyi"
LETTER_TEMPLATE = "letter_1.txt"

now = dt.datetime.now()
df = pd.read_csv("./birthdays.csv")

birthdays = df[["name", "email"]][(df.day == now.day) & (df.month == now.month)]

if birthdays.empty:
    print("There is no birthday today.")
else:
    for index, row in birthdays.iterrows():
        name = row["name"]
        receiver_email = row["email"]

        with open(f"./letter_templates/{LETTER_TEMPLATE}") as file:
            letter = file.read()

        updated_letter = letter.replace("[NAME]", name).replace("[SENDER]", SENDER)



        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=receiver_email,
                                msg=f"Subject: Happy Birthday!\n\n{updated_letter}")







