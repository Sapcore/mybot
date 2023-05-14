import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('/start commant innitiated')
    update.message.reply_text(
        'Hello dear frieand! You have called the "/start" command')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(
        settings.API_TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    print('I have been started')
    logging.info('Bot is innitiated')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
