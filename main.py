from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from random import randint
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '483781851:AAGIyGHC5yLRbUc8H7LTPMAqLQduWAPSEVM'

# Define stages of conversation
PLAY, MENU = range(2)


def _match_result(user_choice, computer_choice):
    logger.info('Computer Choice: %s', computer_choice)
    logger.info('User Choice: %s', user_choice)
    # WIN CONDITION
    if (user_choice, computer_choice) in [('SCISSOR', 'PAPER'), ('PAPER', 'ROCK'), ('ROCK', 'SCISSOR')]:
        return 'WIN'

    # DRAW CONDITION
    if user_choice == computer_choice:
        return 'DRAW'

    # LOSS CONDITION
    if (user_choice, computer_choice) in [('PAPER', 'SCISSOR'), ('ROCK', 'PAPER'), ('SCISSOR', 'ROCK')]:
        return 'LOSS'


def start(bot, update):
    reply_keyboard = [['Paper', 'Rock', 'Scissor']]
    update.message.reply_text(
        '''Let's play Rock–paper–scissor''',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return PLAY


def play(bot, update):
    user = update.message.from_user
    choices = ['SCISSOR', 'PAPER', 'ROCK']
    computer_choice = choices[randint(0, 2)]
    user_choice = (update.message.text).upper()
    result = _match_result(user_choice, computer_choice)

    logger.info(result)
    reply_keyboard = [['Play Again'], ['Finish']]

    update.message.reply_text('You chose: {}\nBot chose: {}\nYou {}.'.format(user_choice, computer_choice, result),
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return MENU


def finish(bot, update):
    user = update.message.from_user
    update.message.reply_text('Bye!',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            PLAY: [RegexHandler('^(Paper|Rock|Scissor)$', play)],
            MENU: [RegexHandler('^(Play Again)$', start)]
        },
        fallbacks=[RegexHandler('^(Finish)$', finish)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
