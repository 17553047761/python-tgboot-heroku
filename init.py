# coding: utf-8
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
# 启动的端口
PORT = int(os.environ.get('PORT', '8443'))
# tgbot的token
TOKEN = '1836395637:AAEFLN82cMMOMAGgwFhfFTpUXbZqXvF7F04'
# 消息的回调地址,awdawda123：heroku的容器名
url = "https://awdawda123.herokuapp.com/"

# 日志
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi!')

def help(update, context):
    update.message.reply_text('Help!')

def echo(update, context):

    update.message.reply_text(update.message.text)

def error(update, context):

    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():


    updater = Updater(TOKEN, use_context=True)


    dp = updater.dispatcher

    # 接收到/命令就执行某个方法
    # /start  就执行 start 方法
    # /help  就执行 help 方法
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # 非命令消息（普通消息）处理方法：echo
    dp.add_handler(MessageHandler(Filters.text, echo))

    # 错误日志
    dp.add_error_handler(error)

    # 开启机器人
    # webhook_url：消息的回调路径，tg把消息转发到哪里，服务器的路径
    # 路径是：https://【heroku项目名】.herokuapp.com
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url=url + TOKEN)


    updater.idle()

if __name__ == '__main__':
    main()




