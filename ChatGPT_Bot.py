import openai
import telebot
import json

PATH = 'X:\projects\ChatGPT_Bot\API_KEYS.json'

with open(PATH, 'r') as f:
    data = json.loads(f.read())

OPENAI_API_KEY = data['KEYS']['OPEN_AI']
TELEGRAM_API_KEY = data['KEYS']['TELEGRAM']

bot = telebot.TeleBot(TELEGRAM_API_KEY)

openai.api_key = OPENAI_API_KEY
model_engine = 'text-davinci-003'

def generate_response(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions['choices'][0]['text']
    return message

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Hello! Ask your question.')

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = generate_response(message.text)
    bot.send_message(message.chat.id, text=response)

bot.polling()