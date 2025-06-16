import os
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.environ.get('PORT', 5000))
APP_URL = os.getenv("RENDER_EXTERNAL_URL", "") + f"/webhook/{BOT_TOKEN}"

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Raider Bot is alive and ready!")

application = ApplicationBuilder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))

@app.route(f"/webhook/{BOT_TOKEN}", methods=["POST"])
async def webhook_handler():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Raider Bot is running!"

if __name__ == "__main__":
    import asyncio
    async def main():
        await application.initialize()
        await application.bot.set_webhook(APP_URL)
        await application.start()
        app.run(host="0.0.0.0", port=PORT)
    asyncio.run(main())

