from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Your bot token
TOKEN = "token"

# Dictionary to store expenses
expenses = {}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /add <amount> <description> to add expenses, and /summary to see total.")

# Add expense command
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(context.args[0])
        description = " ".join(context.args[1:]) if len(context.args) > 1 else "No description"
        user_id = update.effective_user.id
        
        if user_id not in expenses:
            expenses[user_id] = []
        expenses[user_id].append((amount, description))
        
        await update.message.reply_text(f"Added expense: ₹{amount} - {description}")
    except:
        await update.message.reply_text("Usage: /add <amount> <description>")

# Summary command
async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in expenses and expenses[user_id]:
        total = sum(e[0] for e in expenses[user_id])
        details = "\n".join([f"₹{e[0]} - {e[1]}" for e in expenses[user_id]])
        await update.message.reply_text(f"Your expenses:\n{details}\n\nTotal: ₹{total}")
    else:
        await update.message.reply_text("No expenses recorded yet.")

# Main function to run bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("summary", summary))
    app.run_polling()

if __name__ == "__main__":
    main()
