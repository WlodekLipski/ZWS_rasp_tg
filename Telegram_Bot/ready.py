from configparser import ConfigParser
from telegram.ext import Updater, CommandHandler

config = ConfigParser()
config.read('config.ini')

token = config.get('Telegram','token')

def hello(update, context):
    update.message.reply_text(
        'Hello {}. I am ready for start'.format(update.message.from_user.first_name))


updater = Updater(token, use_context=True)

#pending command to a function
updater.dispatcher.add_handler(CommandHandler('ready', hello))

updater.start_polling()
updater.idle()
