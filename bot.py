import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get bot token from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Set up the Flask app
flask_app = Flask(__name__)

# Command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from Raider Bot!")

# Create Telegram application
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

# Set webhook route for Telegram
@flask_app.route("/webhook", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    await telegram_app.process_update(update)
    return "ok"

# Run bot polling locally (optional for testing)
if __name__ == "__main__":
    import asyncio
    async def main():
        await telegram_app.initialize()
        await telegram_app.start()
        await telegram_app.updater.start_polling()
        print("Bot is polling...")

    asyncio.run(main())

