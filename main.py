import telebot
import filewriter
import filereader
import statistic_reader
from settings import *
import os

bot = telebot.TeleBot(Token)
bot.send_message(413431533,959)
state = 0
state1 = 0
name1 = 0
sum1 = 0
day1 = 0
add_stonks_name = 0
add_stonks_sum = 0
add_stonks_day = 0

main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_keyboard.row("Показать доходы", "Показать расходы")
main_keyboard.row('Добавить доход', 'Добавить расход')
main_keyboard.row("Показать статистику")
main_keyboard.row("Вывести остаток")
main_keyboard.row("Удалить записи")

statistik_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
statistik_keyboard.row("Показать статистику доходов", "Показать статистику расходов")
statistik_keyboard.row("Назад")

select_state_stonks_and_not_stonks = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
select_state_stonks_and_not_stonks.row("За день")
select_state_stonks_and_not_stonks.row("За месяц")
select_state_stonks_and_not_stonks.row("За год")
select_state_stonks_and_not_stonks.row("Назад")


@bot.message_handler(commands=['start', 'read'])
def Start(message):
    global state
    if message.text == "/start":
        if 'stonks.txt' not in os.listdir() or 'not_stonks.txt' not in os.listdir():
            bot.send_message(message.chat.id,
                             "Привет, я ваш личный бот, который будет присматривать за вашими расходами и доходами")
            filewriter.create_txts()
            bot.send_message(message.chat.id, "Введите сначала доходы\nВведите имя дохода:")
            state = 1
        else:
            bot.send_message(message.chat.id, "Привет, " + message.chat.first_name, reply_markup=main_keyboard)

    elif message.text == '/read':
        bot.send_message(message.chat.id,
                         "Здраствуйте пользователь\nПри вводе доходов и расходов нужно писать всё правильно\Примеры:\nДата дохода: 06 06 3027\nДата расхода: 20 12 2000")
        bot.send_message(message.chat.id,
                         "Если вы ввели не правильно, рекомендуется удалить все записи кнопкой 'Удалить записи' на главном экране после чего ввести команду /start и начать всё заново")

        bot.send_message(message.chat.id, "По вопросам, за помошью и по проблемам пишите мне: @py_hack06")


@bot.message_handler(content_types=['text'])
def text(message):
    global state, state1, name1, sum1, day1, add_stonks_day, add_stonks_sum, add_stonks_name
    if state == 1:
        name1 = message.text
        bot.send_message(message.chat.id, "Введите сумму")
        state = 2

    elif state == 2:
        sum1 = message.text
        bot.send_message(message.chat.id,
                         "Введите дату в формате 'дд мм гггг', где буквы 'д' день, буквы 'м' месяц а буквы 'г' год")
        state = 3

    elif state == 3:
        day1 = message.text
        result = filewriter.append_stonks(name1, sum1, day1)
        bot.send_message(message.chat.id, result)
        bot.send_message(message.chat.id, "Давайте попробуем ввести расход\nВведите имя расхода:")
        state = 4

    elif state == 4:
        name1 = message.text
        bot.send_message(message.chat.id, "Введите cумму расхода расхода:")
        state = 5

    elif state == 5:
        sum1 = message.text
        bot.send_message(message.chat.id,
                         "Введите дату в формате 'дд мм гггг', где буквы 'д' день, буквы 'м' месяц а буквы 'г' год")
        state = 6

    elif state == 6:
        day1 = message.text
        result = filewriter.append_not_stonks(name1, sum1, day1)
        if result == 'Успешно':
            bot.send_message(message.chat.id,
                             "Поздравляем с первой записью\nРекомендуем ознакомится с примечанием по использованию бота\nКоманда /read",
                             reply_markup=main_keyboard)
            state = 0
        else:
            print('Error405')

    elif message.text == 'Вывести остаток':
        state = 100
        bot.send_message(message.chat.id, "Пожалуйста, выберите период:",
                         reply_markup=select_state_stonks_and_not_stonks)


    elif message.text == 'За день' and state == 100:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'дд мм гггг', где буквы 'д' день, буквы 'м' месяц а буквы 'г' год ")
        state1 = 1
        state = 101

    elif message.text == "За месяц" and state == 100:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'мм гггг', где буквы 'м' месяц а буквы 'г' год ")
        state = 101
        state1 = 2

    elif message.text == "За год" and state == 100:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'гггг', где буквы 'г' год ")
        state = 101
        state1 = 3

    elif state == 101:
        temp = message.text
        result = statistic_reader.ostatok(temp, state1)
        state1 = 0
        bot.send_message(message.chat.id, f"Остаток денег за период: {result}", reply_markup=main_keyboard)
        state = 0




    elif message.text == "Добавить доход":
        state = 7
        bot.send_message(message.chat.id, "Введите имя дохода:")

    elif message.text == "Удалить записи":
        result = filewriter.del_all()
        bot.send_message(message.chat.id, result)

    elif state == 7:
        add_stonks_name = message.text
        bot.send_message(message.chat.id, "Введите сумму")
        state = 8

    elif state == 8:
        add_stonks_sum = message.text
        bot.send_message(message.chat.id,
                         "Введите дату в формате 'дд мм гггг', где буквы 'д' день, буквы 'м' месяц а буквы 'г' год")
        state = 9

    elif state == 9:
        add_stonks_day = message.text
        result = filewriter.append_stonks(add_stonks_name, add_stonks_sum, add_stonks_day)
        bot.send_message(message.chat.id, result, reply_markup=main_keyboard)
        state = 0

    elif message.text == "Добавить расход":
        state = 10
        bot.send_message(message.chat.id, "Введите имя расхода:")

    elif state == 10:
        add_stonks_name = message.text
        bot.send_message(message.chat.id, "Введите сумму")
        state = 11

    elif state == 11:
        add_stonks_sum = message.text
        bot.send_message(message.chat.id,
                         "Введите дату в формате 'дд мм гггг', где буквы 'д' день, буквы 'м' месяц а буквы 'г' год")
        state = 12

    elif state == 12:
        add_stonks_day = message.text
        result = filewriter.append_not_stonks(add_stonks_name, add_stonks_sum, add_stonks_day)
        bot.send_message(message.chat.id, result, reply_markup=main_keyboard)
        state = 0

    elif message.text == "Показать доходы":
        result = filereader.open_stonks()
        for qwe in result:
            bot.send_message(message.chat.id,
                             f" Имя: {qwe[0:qwe.find(':')]}\nСумма: {qwe[qwe.find(':') + 1:qwe.find('@')]}\nДата: {qwe[qwe.find('@') + 1:len(qwe)]}",
                             reply_markup=main_keyboard)

    elif message.text == "Показать расходы":
        result = filereader.open_not_stonks()
        for qwe in result:
            bot.send_message(message.chat.id,
                             f" Имя: {qwe[0:qwe.find(':')]}\nСумма: {qwe[qwe.find(':') + 1:qwe.find('@')]}\nДата: {qwe[qwe.find('@') + 1:len(qwe)]}",
                             reply_markup=main_keyboard)

    elif message.text == "Показать статистику":
        bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=statistik_keyboard)
        state = 13

    elif message.text == "Назад" and state == 13:
        bot.send_message(message.chat.id, "Переход на главное меню", reply_markup=main_keyboard)
        state = 0

    elif message.text == "Показать статистику доходов" and state == 13:
        bot.send_message(message.chat.id, "Пожалуйста, выберите период:",
                         reply_markup=select_state_stonks_and_not_stonks)
        state = 14

    elif message.text == "Показать статистику расходов" and state == 13:
        bot.send_message(message.chat.id, "Пожалуйста, выберите период:",
                         reply_markup=select_state_stonks_and_not_stonks)
        state = 16


    elif message.text == "Назад" and state == 100:
        bot.send_message(message.chat.id, "Возврат на главную страницу", reply_markup=main_keyboard)


    elif message.text == "За день" and state == 14:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'дд мм гггг', где буквы 'д' день, буквы 'м' месяц а буквы 'г' год ")
        state = 15
        state1 = 1

    elif message.text == "За месяц" and state == 14:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'мм гггг', где буквы 'м' месяц а буквы 'г' год ")
        state = 15
        state1 = 2


    elif message.text == "За год" and state == 14:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'гггг', где буквы 'г' год ")
        state = 15
        state1 = 3

    elif message.text == "Назад" and state == 14:
        bot.send_message(message.chat.id, "Возврат на главную страницу", reply_markup=main_keyboard)

    elif message.text == "За день" and state == 16:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'дд мм гггг', где буквы 'д' день, буквы 'м' месяц а буквы 'г' год ")
        state = 17
        state1 = 1

    elif message.text == "За месяц" and state == 16:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'мм гггг', где буквы 'м' месяц а буквы 'г' год ")
        state = 17
        state1 = 2

    elif message.text == "За год" and state == 16:
        bot.send_message(message.chat.id,
                         "Пожалуйста введите дату в формате 'гггг', где буквы 'г' год ")
        state = 17
        state1 = 3

    elif message.text == "Назад" and state == 16:
        bot.send_message(message.chat.id, "Возврат на главную страницу", reply_markup=main_keyboard)

    elif state == 15:
        temp = message.text
        result = statistic_reader.read_for_stonks(temp, state1)
        state1 = 0
        if result == 1:
            bot.send_message(message.chat.id, "Кажется вы ввели что-то неверно\nПопробуйте ввести ещё раз")

        elif any(result) == False:
            bot.send_message(message.chat.id, "Ничего не найдено", reply_markup=statistik_keyboard)
            state = 13

        else:
            for i in result:
                bot.send_message(message.chat.id, f"Имя дохода: {i}\nСумма: {result.get(i)}",
                                 reply_markup=statistik_keyboard)
                state = 13

    elif state == 17:
        temp = message.text
        result = statistic_reader.read_for_not_stonks(temp, state1)
        state1 = 0
        if result == 1:
            bot.send_message(message.chat.id, "Кажется вы ввели что-то неверно\nПопробуйте ввести ещё раз")

        elif any(result) == False:
            bot.send_message(message.chat.id, "Ничего не найдено", reply_markup=statistik_keyboard)
            state = 13

        else:
            for i in result:
                bot.send_message(message.chat.id, f"Имя дохода: {i}\nСумма: {result.get(i)}",
                                 reply_markup=statistik_keyboard)
                state = 13


bot.polling(none_stop=True)
