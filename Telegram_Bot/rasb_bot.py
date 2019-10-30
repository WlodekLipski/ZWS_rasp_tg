from telegram.ext import Updater, CommandHandler
from telegram.ext import RegexHandler
from pandas import read_csv
import numpy as np
import re

token = None
with open('config','r') as fd:
    token = fd.read().strip('\n')

MESSAGES = ['hello', 'help', 'pic (temp|humid|light) opt(size)', 'tail opt(size)']
VALID_ARGS_LIST = ['temp', 'light','humid']
TRUE_ARGS = {'temp':'Temperature', 'humid':'Humidity', 'light':'Light'}

def rasp_hello(update, context):
    update.message.reply_text(
        'Hello {}. I am ready for start'.format(update.message.from_user.first_name))
    
def rasp_pic(update, context):
    picture_type = context.args[0]
    if (picture_type is not None and
                picture_type in VALID_ARGS_LIST):
        try:
            amount = int(context.args[1])
            """
            Hook to a picture generator with size
            """
            update.message.reply_text('ONLY PICTURE with custom size*')
        except ValueError:
            """
            Hook to a picture generator
            """
            #print(TRUE_ARGS[context.args[0]])
            update.message.reply_text('ONLY PICTURE with standard size')
        else:
            update.message.reply_text('Invalid args')

def rasp_tail(update, context):
    tail_size = 10
    if len(context.args) != 0:
        tail_size = int(context.args[0])

    if tail_size < 0:
        tail_size *= -1
    data = read_csv('data.csv').tail(tail_size)
    for name in TRUE_ARGS.values():
        msg = name + ':\n'+ re.sub(' {2,}',' ',data.loc[:,name].to_string(index=False))
        update.message.reply_text(msg)


def rasp_help(update, context):
    reply  = '/' + MESSAGES[0]+'\n'
    for i in MESSAGES[1:]:
        reply += '/'+i+'\n'
    update.message.reply_text(
            'List of available commands:\n{}'.format(reply))

updater = Updater(token, use_context=True)

#pending command to a function
updater.dispatcher.add_handler(CommandHandler('hello', rasp_hello))
updater.dispatcher.add_handler(CommandHandler('pic', rasp_pic, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('tail', rasp_tail, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('help', rasp_help))

updater.start_polling()
updater.idle()
