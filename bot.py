import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.messege.reply_text("Hello! Send me a Instergram link.")
    
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.messege.reply_text("Send me a Instergram link and I will send you the media.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "instergram.com":
        await update.message.reply_text("It is valid link.")
    else:
        await update.message.reply_text("This is not a valid link.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    app.add_handler(message_handler)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
