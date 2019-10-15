import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import sqlite3
import json
import requests
from PIL import Image
import logging


token = "token" #insert API token here

bot = telegram.Bot(token = token)
updater = Updater(token = token, use_context = True)
connection = sqlite3.connect('data.db',check_same_thread = False)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot,update):
	bot.send_message(chat_id = update.effective_chat.id , text = 'Hey!')

def filereader(update,context):
	file = update.message.document
	print(file.mime_type)
	#print(file)
	#print(bot.getFile(file.file_id))
	# file = update.message.document
	#update.message.document.get_file().download(custom_path)
	print(update.message.document.get_file())
	update.message.document.get_file().download(custom_path = 'Documents/file.jpg')
	im = Image.open('/Users/saravananmano/Documents/file.jpg')
	im.save('/Users/saravananmano/Documents/file.png')
	#print(bot.send_photo(chat_id=update.effective_chat.id, photo=open('GTA.jpg')))
	bot.send_document(chat_id=update.effective_chat.id, document=open('/Users/saravananmano/Documents/file.png', 'rb'))

	#im = Image.copy(file)
	# im.save('Foto.png')
	# print('Success')
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
# updates = bot.get_updates()
# print([u.message.photo for u in updates if u.message.photo])
#bot.sendP#print(bot)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.document,filereader))
updater.dispatcher.add_error_handler(error)
updater.start_polling()
