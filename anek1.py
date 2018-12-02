import telebot
import random

token = "561568815:AAE3kTf7n2apXhUFvLndnyxlWmbVffcvEm0"
# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5://tvorogme@tvorog.me:6666'}

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)
anekdoty=['Ревизия на складе. - А куда делся вагон растворимого кофе? - Растворился!',
      'Два депутата в джакузи:  - У тебя охрана сколько человек? - 11, а у тебя?  - И у меня 11, может в футбол сыграем? ',
      'На уроке литературы:- Вовочка, что тебе известно о Чехове и Пушкине?- Чехов - это город, и Пушкин - это город. - А кто же тогда Толстой? - А Толстой - это лев!', 
      'Учительница спрашивает Вовочку: - Вовочка, а кто из родителей делал тебе домашнее задание? - Не знаю, я в это время уже сплю!', 
      'Урок зоологии в школе. Учительница: - Дети, как размножаются ежи? Вовочка: - Очень, очень осторожно',
      'Маленький Вовочка смотрит, как папа красит потолок. Мама говорит ему: - Смотри, Вовочка, и учись, подрастешь и папе помогать будешь. - А что, он к тому времени сам не докрасит?']

@bot.message_handler(commands=["anek"])
def anek(message):
    text = message.text
    user = message.chat.id
    bot.send_message(user, random.choice(anekdoty))

@bot.message_handler(commands=["help", "start"])
def help(message):
    text = message.text
    user = message.chat.id
    bot.send_message(user, "Введите /anek  и разхихикайтесь. Не забудьте потом съесть Смекту" )

@bot.message_handler(content_types=['text'])
def echo(message):
    text = message.text
    user = message.chat.id
    bot.send_message(user, text)

bot.polling(none_stop=True)
