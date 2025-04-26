import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Send me a Instergram link.")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me an Instagram link and I will send you the media. develop by Dewnan.")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "instagram.com" in text:
        await update.message.reply_text("It is a valid link.")
    else:
        await update.message.reply_text("This is not a valid Instagram link.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
