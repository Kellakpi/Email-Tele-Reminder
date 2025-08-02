# Daily Reminder Email/Bot

This is a python script that sends **daily reminders** via:
- Email (Using Email + SMTP)
- Telegram Bot (Using Telegram Bot API)

Usefull to set up reminders, and daily tasks, can be changed to use as a notification from your self to stop doom scrolling.

---

# Features 

- Sends email reminders at a scheduled time
- Sends telegram messages, using your own bot
- Uses '.env' file to keep credential hidden
- Customizable message content and schedule
- Lightweight - no frameworks, just standard libraries and 'requests'.

---

# How it works

The script:
1. Loads credentials from a `.env` file
2. Schedules both an email and a Telegram message
3. Sends them at your configured times

# Requirements

- Python 3.10+
- Gmail account with App Password enabled (App password is not the same as the password, don't make my mistake, look it up on google)
- Telegram bot (created via [BotFather](https://t.me/BotFather))
- Your chat ID (use [@userinfobot](https://t.me/userinfobot) to find it) - userinfobot = ur bot **Information**

Install Dependencies: 

'''bash 
>pip install python-dotenv schedule requests **To use the .env to keep ur info secure**

Then create an .env file in the folder, and inside it add a variable with the token and ID, aswell as the gmail email, and App password.
Like this:

EMAIL_ADDRESS=your_email@gmail.com - 
EMAIL_PASSWORD=**your_gmail_app_password**

TELEGRAM_BOT_TOKEN=**your_telegram_bot_token** - 
TELEGRAM_CHAT_ID=**123456789**

# Usage

To run it:

'''bash 
>python emailerMain.py

# TO-DO(eventually)

- Add GUI or CLI interface
- Add message customization
- Option to pull reminders from file or web

---

Built for you by @Kellakpi