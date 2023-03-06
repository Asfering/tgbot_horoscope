import telebot
import datetime
import re
import os
import random

# Время
now = datetime.datetime.now()

# АПИ токен для бота
bot = telebot.TeleBot('6232422604:AAE3XTYt_lfjOfkqknYmX2pbYFdMlA9Zdlg')

# Регулярочка
type_regular = "[0-3][0-9]\.[0-1][0-9]"

# Массив прогнозов
prognoz_deals = [
    "Все дела у вас пойдут в гору.",
    "Возникнут трудности в неважных делах, когда как в глобальных всё будет хорошо.",
    "Сегодня отличный день для заключений контрактов.",
    "Сегодня не самый удачный день для заключения важных контрактов.",
    "Возникнут временные трудности в делах, но вы с лёгкостью сможете их преодолеть.",
    "Сегодня ужасный день для ведения дел, вам необходимо отдохнуть или принять помощь других."
]

prognoz_love = [
    "Сегодня отличный день для любовных действий.",
    "На личном фронте могут возникнуть трудности, следует быть осторожным в высказываниях и действиях.",
    "Стоит держать дистанцию от объектов воздыхания, могут возникнуть проблемы, способные привести к разрывам отношений.",
    "В любви могут возникнуть проблемы, но ваша половинка поможет вам вместе преодолеть все проблемы.",
    "Сегодня ваш день, стоит быть смелее по отношению к объекту воздыхания, всё получится.",
    "В любви сегодня не всё так однозначно, стоит уйти в свои мысли на некоторое время."
]

prognoz_community =[
    "Больше общайтесь с людьми, сегодня вы будете душой компании.",
    "Стоит реже общаться с людьми, над вами могут злостно пошутить.",
    "Постарайтесь избегать людных мест, вас могут выставить в плохом свете.",
    "Сегодня ваш день, общайтесь с обществом как можно больше.",
    "В общении с людьми могут возникнуть недопонимания, не переводите всё в ссору.",
    "В общении с людьми могут возникнуть проблемы, постарайтесь прислушаться к их доводам"
]

prognoz_luck =[
    "Сегодня вам крупно повезёт.",
    "Сегодня вас будут преследовать неудачи, постарайтесь жить спокойнее.",
    "Удача на вашей стороне.",
    "К сожалению, сегодня удача от вас отвернётся."
]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, напиши /help, чтобы узнать, что я умею!")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Вот что я могу: \n"
                                               "/horo - получить гороскоп\n")
    elif message.text == "/stest":
        testing(message)
    else:
        else_message(message)


def else_message(message):
    if re.search(type_regular, str(message)):
        parse_data(message)
    else:
        bot.send_message(message.from_user.id, "Возникла ошибка, введи /help")


def parse_data(message):
    Day = message.text[:2]
    Month = message.text[3:5]

    os.system("cls")

    if test_data(Day, Month):
        zodiac_sign = get_zodiac(Day, Month)
        final_string = get_data() + "\nНа сегодня знаку зодиаку " + zodiac_sign + " звёзды пророчат следующее: " \
                       "\n" + random.choice(prognoz_deals) + " " + random.choice(prognoz_love) + \
                       " " + random.choice(prognoz_community) + " " + random.choice(prognoz_luck) + \
                       "\nСчастливое число: " + str(random.randint(1, 100))
        bot.send_message(message.from_user.id, final_string)
    else:
        bot.send_message(message.from_user.id, "Ошибка: Дата введена неверно")


def get_data():
    return parse_day() + "." + parse_month() + "." + str(now.year)


def parse_day():
    if now.day < 10:
        return "0" + str(now.day)
    else:
        return str(now.day)


def parse_month():
    if now.month < 10:
        return "0" + str(now.month)
    else:
        return str(now.month)


def test_data(Day, Month):
    day = int(Day)
    month = int(Month)
    if 13 > month > 0:
        if month == 1 and 32 > day > 0:
            return True
        elif month == 2 and 30 > day > 0:
            return True
        elif month == 3 and 32 > day > 0:
            return True
        elif month == 4 and 31 > day > 0:
            return True
        elif month == 5 and 32 > day > 0:
            return True
        elif month == 6 and 31 > day > 0:
            return True
        elif month == 7 and 32 > day > 0:
            return True
        elif month == 8 and 32 > day > 0:
            return True
        elif month == 9 and 31 > day > 0:
            return True
        elif month == 10 and 32 > day > 0:
            return True
        elif month == 11 and 31 > day > 0:
            return True
        elif month == 12 and 32 > day > 0:
            return True
        else:
            return False
    else:
        return False


def get_zodiac(Day, Month):
    day = int(Day)
    month = int(Month)
    zodiac_sign = ""
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 17):
        zodiac_sign = "Водолей"
    elif (month == 2 and day >= 18) or (month == 3 and day <= 19):
        zodiac_sign = "Рыбы"
    elif (month == 3 and day >= 20) or (month == 4 and day <= 19):
        zodiac_sign = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Стрелец"

    return zodiac_sign


def testing(message):
    bot.send_message(message.from_user.id, "Введите дату рождения в формате DD.MM")


bot.polling(none_stop=True, interval=0)
