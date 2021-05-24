# coding: utf-8
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = '1836395637:AAEFLN82cMMOMAGgwFhfFTpUXbZqXvF7F04'
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://awdawda123.herokuapp.com/" + TOKEN)
updater.idle()
