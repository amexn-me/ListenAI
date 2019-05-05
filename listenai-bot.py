# Imports
import json
import apiai
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Incorporating Telegram API Token received from @BotFather
updater = Updater(token='TELEGRAM API TOKEN')
dispatcher = updater.dispatcher

# Defining the start and Dialogflow sequel
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello, ListenAI here. Are you ready to have a chat?')
def textMessage(bot, update):
    request = apiai.ApiAI('DIALOGFLOW - SMALLTALK AGENT API TOKEN').text_request() # Dialogflow API Token
    request.lang = 'en' # Request language
    request.session_id = random.randint(1,101) # random session ID for bot training
    request.query = update.message.text # Requesting the Smalltalk Agent with what we have received from the user
    responseJson = json.loads(request.getresponse().read().decode('utf-8')) #Collecting the respinse
    response = responseJson['result']['fulfillment']['speech'] # Taking the answer in JSON
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Am sorry, I didnt get you.')

# Handlers for bot
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

# Adding handlers to the dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

# Start the search
updater.start_polling(clean=True)

# Stops the bot
updater.idle()