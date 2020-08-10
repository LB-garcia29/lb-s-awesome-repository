import logging
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
updater = Updater(token='1346270907:AAE5FeBKucqeR6OxsSzlXmRi6OxYWVPtt_U', use_context=True)
dispatcher = updater.dispatcher
bot = telegram.Bot(token='1346270907:AAE5FeBKucqeR6OxsSzlXmRi6OxYWVPtt_U')
profDict={'BATALLER':1, 'CHUMS':10}
name_of_prof:""
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Hi welcome to the Profs to pick bot\nHere are a list of commands\n/grade_a_prof\n/find_a_prof")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
def grade(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="you can grade a prof here: https://forms.gle/DtQpwxawcGwXwyrCA")
grade_handler = CommandHandler('grade_a_prof',grade)
dispatcher.add_handler(grade_handler)

def ProfName(update,context):
    name_of_prof=update.message.text
    if name_of_prof.upper() in profDict:
        context.bot.send_message(chat_id=update.effective_chat.id,text="Your prof's grade is {}".format(profDict[name_of_prof.upper()]))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text="Could not Find Prof ://")

def findProf(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Type in your prof's name")
find_handler = CommandHandler('find_a_prof',findProf)
dispatcher.add_handler(find_handler)

gradefinder_handler = MessageHandler(Filters.text & (~Filters.command), ProfName)
dispatcher.add_handler(gradefinder_handler)

updater.start_polling()