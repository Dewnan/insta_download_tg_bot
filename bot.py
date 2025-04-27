import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler
import instaloader

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

    image_loader = instaloader.Instaloader(
        save_metadata=False,
        download_video_thumbnails=False,
        download_pictures=True,
        download_videos=False,
        quiet=True,
    )

    video_loader = instaloader.Instaloader(
        save_metadata=False,
        download_video_thumbnails=False,
        download_pictures=False,
        download_videos=True,
        quiet=True,
    )
    try:
        post = instaloader.Post.from_shortcode(image_loader.context, url.split("/")[4])
        if post.is_video:
            loader = video_loader
            print("Using Video Loader.")
        else:
            loader = image_loader
            print("Switch to Image Loader.")

        print(f"Downloaded...")
        loader.download_post(post, target=f"download'/'{post.owner_username}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()