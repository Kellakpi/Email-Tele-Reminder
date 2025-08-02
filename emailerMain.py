import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import schedule
import time
import requests

load_dotenv() # Load everything into the env file, into memory.

#Accessing the memory, to access the data from the env file. (Never hardcode Credentials)
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

def send_email():
    
    msg = EmailMessage() # Define email parameters
    msg["Subject"] = "Daily Reminder"
    msg["From"] = email_address
    msg["To"] = email_address
    msg.set_content("Practice some python!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: # Connect to gmail smtp server, over SSL on port 465.    
            smtp.login(email_address, email_password) # Logs in.
            smtp.send_message(msg) # Send message, and closes the connection. 
            print("Email sent!")   


def send_telegram(): 
       bot_token = os.getenv("TELEGRAM_BOT_TOKEN") # We retrieve the token
       chat_id = os.getenv("TELEGRAM_CHAT_ID") # We retrieve the Chat ID.
       message = "Practice some python!" #The message sent to the telegram bot

       url = f"https://api.telegram.org/bot{bot_token}/sendMessage" #We contstruct and access the telegram API url.
       data = {"chat_id": chat_id, "text": message} # Form data to send the message, with the given ID.

       response = requests.post(url, data=data) #Makes an http post and request. 
       print("Telegram message sent!")
       print("Status:", response.status_code) # Prints a confirmation and response for Debugging.
       print("Response:", response.text)


#Main schedulers
schedule.every().day.at("16:00").do(send_telegram)
schedule.every().day.at("16:00").do(send_email)

#Main looper
while True:
        schedule.run_pending()
        time.sleep(60)
