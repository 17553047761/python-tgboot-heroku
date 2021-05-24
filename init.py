# coding: utf-8
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler


def start(update, context):
    update.message.reply_text('Hi!')

def help(update, context):
    update.message.reply_text('Help!')


def callback_query(bot,update):
    # user=update.callback_query.from_user
    # cmd=update.callback_query.data
    # bot.send_message(user.id, cmd)
    # update.callback_query.answer('OK')
    # updater.dispatcher.add_handler(CallbackQueryHandler(callback_query))

    update.message.reply_text('Help!')

def echo(update, context):
    # key = InlineKeyboardButton('哈哈哈', callback_data=f'new')
    # keyboard = InlineKeyboardMarkup([[key]])
    # update.message.reply_text('欢迎', reply_markup=keyboard)

    # update.message.reply_text(photo='<https://telegram.org/img/t_logo.png')

    # update.message

    print(update.message)
    # 回复消息，发送什么就回复什么
    update.message.reply_text(update.message.text)

def error(update, context):
    print('Update "%s" caused error "%s"', update, context.error)

if __name__ == '__main__':

    # 参数1：机器人的token
    # 参数3：使用的代理，是本地的代理，WinXray的代理

    updater = Updater('1836395637:AAEFLN82cMMOMAGgwFhfFTpUXbZqXvF7F04', use_context=True)

    dispatcher = updater.dispatcher

    # 接收到/命令就执行某个方法
    # /start  就执行 start 方法
    # /help  就执行 help 方法
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # 接收到任意文本消息就执行echo
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    dispatcher.add_error_handler(error)

    updater.start_polling()  # 使用发送请求获取消息模式
    updater.idle()
