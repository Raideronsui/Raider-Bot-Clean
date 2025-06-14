from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7586933538:AAEdrgOLMGkKzpA94558_1uLj25rxb7NKds"  # Replace with your actual token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Raider Bot is live and ready to trade!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Raider Bot Help:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/price - Get current SUI price\n"
        "/buy - Simulate a buy trade\n"
        "/sell - Simulate a sell trade\n"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()
