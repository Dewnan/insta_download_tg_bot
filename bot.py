import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler
import yt_dlp

os.makedirs("download", exist_ok=True)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Send me a Instergram link.")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me an Instagram link and I will send you the media. develop by Dewnan.")
async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "instagram.com" in url:
        await update.message.reply_text("Downloading...")
        try:
            await download_content(url)
            await update.message.reply_text("Download Complete.")
        except Exception as e:
            await update.message.reply_text("Error downloading: Internal server error.")
            print(f"Error: {e}")
    else:
        await update.message.reply_text("This is not a valid Instagram link.")

async def download_content(url):
        ydl_opts = {
            'outtmpl': 'download/%(title).30s.%(ext)s',
            'quiet': True,
            'format': 'bestvideo+bestaudio/best',
            'skip_download': False,
            'noplaylist': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("start downloadng.")
            ydl.extract_info(url, download=True)
            
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
