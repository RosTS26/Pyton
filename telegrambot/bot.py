import telebot
import pyowm

owm = pyowm.OWM('c1f75160c4076a263aa79e6c2dade3b4', language = 'ru') # Переменная own принимает значение функции OWN
																	# Вставляем API сайта и указываем при помощи переменной Language язык 
bot = telebot.TeleBot('1175372681:AAG-qHUgC1jNrn4o4X8V5eiuyIh0ek6O8_Y')

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text) # Присваиваем переменной observation все данный о месте
	w = observation.get_weather() # Присваиваем переменной w данные о погоде
	temp = w.get_temperature('celsius')['temp'] # temp присваиваем значение о текущей температуре
	max_temp = w.get_temperature('celsius')['temp_max'] # max_temp присваиваем максимальную температуру 

	answer = 'В городе/стране ' + message.text + ' сейчас ' + w.get_detailed_status() + '\n'
	answer += 'Температура на данный момент: ' + str(temp) + '\n Максимальная температура: ' + str(max_temp) + '\n\n'

	if temp < -20:
		answer += 'Сейчас на улице дубак! Лучше не выходить!'
	elif temp < -5:
		answer += 'Сейчас на улице очень холодно, оденься теплее!'
	elif temp < 15:
		answer += 'На улице сейчас прохладно! Советую приодется :)'
	elif temp < 25:
		answer += 'Сейчас отличная температура на улице! Можно одеваться как летом!'
	elif temp < 40:
		answer += 'На улице жара! Накинь бейсболочку :)'
	else:
		answer += 'По-моему, мы в аду... О_о'

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)