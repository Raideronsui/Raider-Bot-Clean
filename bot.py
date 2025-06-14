from telegram.ext import Updater, CommandHandler

BOT_TOKEN = "7586933538:AAEdrgOLMGkKzpA94558_1uLj25rxb7NKds"  # Replace with your actual token

def start(update, context):
    update.message.reply_text("Raider Bot is live and ready to trade!")

def help_command(update, context):
    update.message.reply_text(
        "🤖 Raider Bot Help:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/price - Get current SUI price\n"
        "/buy - Simulate a buy trade\n"
        "/sell - Simulate a sell trade\n"
    )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
