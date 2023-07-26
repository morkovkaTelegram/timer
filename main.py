import telebot
import datetime
import config

token = config.timer_token
bot = telebot.TeleBot(token) 

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот, который может отправлять время в разных городах. Напишите /time для получения времени ")


@bot.message_handler(commands=['time'])
def time_command(message):
    moscow_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    almaty_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=6)))
    ekb_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=6)))
    text = f"Текущее время в Москве: {moscow_time.strftime('%H:%M:%S')}\nТекущее время в Екатеринбурге: {ekb_time.strftime('%H:%M:%S')}\nТекущее время в Алматы: {almaty_time.strftime('%H:%M:%S')}"
    bot.reply_to(message, text)

@bot.inline_handler(lambda query: True)
def inline_query(query):
    results = []
    moscow_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    almaty_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=6)))
    ekb_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5)))
    text = f"Текущее время в Москве: {moscow_time.strftime('%H:%M:%S')}\nТекущее время в Екатеринбурге: {ekb_time.strftime('%H:%M:%S')}\nТекущее время в Алматы: {almaty_time.strftime('%H:%M:%S')}"
    result = telebot.types.InlineQueryResultArticle(id="time", title="Текущее время",
                                                   description="Время в разных городах",
                                                   input_message_content=telebot.types.InputTextMessageContent(text))
    results.append(result)
    bot.answer_inline_query(query.id, results, cache_time=1)


while True: 
	bot.infinity_polling(none_stop=True, timeout = 10, long_polling_timeout =5)
