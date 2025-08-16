# BillBuddy-Telegram-expense-tracker
A simple Telegram bot to track daily and monthly expenses. Built with Python and python-telegram-bot.

🚀 Features

➕ Add expenses with /add <amount> <description>

📜 View all recorded expenses with /list

📅 Check monthly summary with /summary

🗑️ Clear all expenses with /clear

⚙️ Installation & Setup

Clone this repository

git clone https://github.com/annamj111/BillBuddy-Telegram-expense-tracker.git
cd telegram-expense-tracker


Install dependencies

pip install -r requirements.txt


Set your bot token

Get a token from BotFather on Telegram.

Store it as an environment variable:

export BOT_TOKEN="your_telegram_token_here"

Or put it inside a .env file.

Run the bot

python bot.py

🛠️ Tech Stack

Python 3

python-telegram-bot library

JSON / CSV (for storing expenses locally)

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

📌 To-Do / Future Improvements

 Add category-wise expenses

 Add database support (SQLite/PostgreSQL)

 Deploy to cloud (Heroku / Railway / AWS)

⚡ Developed with ❤️ by Anna Maria Jose
