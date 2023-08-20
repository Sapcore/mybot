import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from datetime import date

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

commands_list = {
    '/start': 'Greets user. Context required: None',
    '/commands': 'Shows the list of commands available. Context required: None',
    '/planet': 'Shows the constellation of the planet of interest. Context required: planet name',
    '/wordcount': 'Counts words in the sentence. Context required: sentence',
    '<any message>': 'Repeats the message input by user'
}


def greet_user(update, context):
    print('/start command initiated')
    update.message.reply_text('''Hello dear friend! You have called the /start command.
You can see the commands list I can perform by typing /commands''')


def show_commands(update, context):
    print('/commands command initiated')
    update.message.reply_text('\n'.join(f'{key} ---> {item}' for key, item in commands_list.items()))


def check_planet(update, context):
    planet_dict = {
        'mercury': ephem.Mercury,
        'venus': ephem.Venus,
        'mars': ephem.Mars,
        'jupiter': ephem.Jupiter,
        'saturn': ephem.Saturn,
        'uranus': ephem.Uranus,
        'neptune': ephem.Neptune,
    }
    print(f'/planet command initiated with the following context: {context.args}')
    if context.args:
        if planet_dict.get(context.args[0].lower()):
            const = ephem.constellation(planet_dict[context.args[0].lower()](date.today()))[1]
            message = f'{context.args[0].capitalize()} is currently ({date.today()}) at {const}'
        else:
            message = 'There is no such planet'
    else:
        message = 'Please define a planet name and I can tell you where it is located.'
    update.message.reply_text(message)
    print('/planet command completed')


def count_words(update, context):
    print(f'/wordcount command initiated with the following context: {context.args}')
    if context.args:
        message = f'Number of words written = {len(context.args)}'
    else:
        message = 'Please input phrase and I will tell you the number of words within.'
    update.message.reply_text(message)
    print('/wordcount command completed')


def talk_to_me(update, context):
    user_text = update.message.text
    print(f'No command is called so \'talked_to_me\' is initiated with the following input: {user_text}')
    update.message.reply_text(user_text)


def main():

    mybot = Updater(settings.API_TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('commands', show_commands))
    dp.add_handler(CommandHandler('planet', check_planet))
    dp.add_handler(CommandHandler('wordcount', count_words))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    print('I have been started')
    logging.info('Bot is initiated')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
