# ListenAI
An AI-Powered (Dialogflow) Telegram chatbot made in Python. She's available @[ListenAI](https://t.me/listenai_bot)

#### Required Technologies
> 1. python-telegram-bot==11.1.0
> 2. apiai==1.2.3
> 3. requests==2.21.0
> 4. gunicorn==19.9.0

#### AI Setup
I used the Dialogflow from Google (which was formerly known as API.AI) for my ai part. In prebuilt agents, you can import a Small-Talk agent and paste it's client access token here in the code. You can also randomly ID your sessions for training the model in order to attain a better level of interaction with the user.
```python
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
```

#### Conclusion
And that's how you built a simple bot on the go. Yet the model need much more training for responding to complex questions. Hope you'll train it accordingly.
<br><br>
Thanks!
