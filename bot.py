from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Raider Bot is live and running via webhook!")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🤖 Raider Bot Help:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/price - Get current SUI price\n"
        "/buy - Simulate a buy trade\n"
        "/sell - Simulate a sell trade"
    )

# Register command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Raider Bot Webhook is active."

if __name__ == "__main__":
    app.run(port=10000)
