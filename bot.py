import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "hi":
        await update.message.reply_text("Hi")
    else:
        await update.message.reply_text("Hello")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    app.add_handler(message_handler)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
