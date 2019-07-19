import telebot
import os
from flask import Flask, request
import logging

#names = []

bot = telebot.TeleBot('883652979:AAFZDW2E8mcJ8dbTq9Lcct-YTZ4uxcnJoBw')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Наша продукция').row('Контакты').row('Наш адрес')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Мебель для спальни').row('Мебель для гостинной').row('Назад')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Камея', 'Розалина', 'Мармарис')
keyboard3.row('Анна', 'Элегант Люкс', 'Александра')
keyboard3.row('Рояль', 'Сенатор', 'Изабелла 4')
keyboard3.row('Изабелла 6', '0101', '0102')
keyboard3.row('0103', '0104', 'Честер')
keyboard3.row('Комод', 'Назад')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Пенал 8069', 'Пенал 8070', 'Стенка Афродита')
keyboard4.row('Горка 8069', 'Горка Классик', 'Горка Элегант')
keyboard4.row('Горка Катерина', 'Катерина сундук', 'Элегант сундук')
keyboard4.row('Клеопатра сундук', 'Классик сундук', 'Афродита сундук')
keyboard4.row('Назад')

keyboard_all_colors = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_all_colors.row('Ночь', 'Белый', 'Дуб')
keyboard_all_colors.row('Назад')

keyboard_two_colors = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_two_colors.row('Ночь', 'Белый')
keyboard_two_colors.row('Назад')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!, Вас приветствует бот компании Izabella mebel', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    current = message.text.lower()
    if current == 'контакты':
        bot.send_message(message.chat.id, '+998983022283 Фарход\n+998977562007 Музаффар\n+998994881133 Давлат')
    elif current == 'наша продукция':
        bot.send_message(message.chat.id, 'Выберите вид мебели', reply_markup=keyboard2)
    elif current == 'назад':
        bot.send_message(message.chat.id, 'Выберите нужный режим', reply_markup=keyboard1)

    elif current == 'мебель для спальни':
        bot.send_message(message.chat.id, 'Выберите нужную модель', reply_markup=keyboard3)
    elif current == 'мебель для гостинной':
        bot.send_message(message.chat.id, 'Выберите нужную модель', reply_markup=keyboard4)
    elif current == 'наш адрес':
        bot.send_message(message.chat.id,
                         'Перейдите по ссылке: https://www.google.com/maps/place/GRANT+FUTURES+MEBEL/@41.2481259,69.1636308,254a,35y,39.24t/data=!3m1!1e3!4m5!3m4!1s0x38ae891a6a7927c1:0xc2971cdaabfe7bc0!8m2!3d41.2499708!4d69.1645316')
    elif current == 'камея':
        bot.send_photo(message.chat.id, 'https://imbt.ga/cOwq72pAb8')
    elif current == 'рояль':
        bot.send_photo(message.chat.id, 'https://imbt.ga/viczUgiohx')
    elif current == 'честер':
        bot.send_photo(message.chat.id, 'https://imbt.ga/jf1OCqM4J6')
    elif current == 'комод':
        bot.send_photo(message.chat.id, 'https://imbt.ga/pJHZP3AtKP')
    elif current == 'горка катерина':
        bot.send_photo(message.chat.id, 'https://imbt.ga/8Xu5i6d3Xu')
    elif current == 'горка элегант':
        bot.send_photo(message.chat.id, 'https://imbt.ga/adnBFFKQhh')
    elif current == 'горка классик':
        bot.send_photo(message.chat.id, 'https://imbt.ga/wVpfBO1JMB')
    elif current == 'катерина сундук':
        bot.send_photo(message.chat.id, 'https://imbt.ga/QOxvHj9a2y')
    elif current == 'элегант сундук':
        bot.send_photo(message.chat.id, 'https://imbt.ga/QOxvHj9a2y')
    elif current == 'клеопатра сундук':
        bot.send_photo(message.chat.id, 'https://imbt.ga/4fPuILxzvc')
    elif current == 'классик сундук':
        bot.send_photo(message.chat.id, 'https://imbt.ga/4fPuILxzvc')
    elif current == 'афродита сундук':
        bot.send_photo(message.chat.id, 'https://imbt.ga/bO0rl62KQ4')
    '''elif current == 'розалина':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_all_colors)
    elif current == 'мармарис':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_all_colors)
    elif current == 'анна':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == 'элегант люкс':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == 'александра':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == 'сенатор':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_all_colors)
    elif current == 'изабелла 4':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == 'изабелла 6':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == '0101':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == '0102':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == '0103':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == '0104':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == 'пенал 8069':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_all_colors)
    elif current == 'пенал 8070':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_all_colors)
    elif current == 'горка 8069':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_all_colors)
    elif current == 'стенка афродита':
        names.clear()
        names.append(current)
        bot.send_message(message.chat.id, 'Выберите цвет', reply_markup=keyboard_two_colors)
    elif current == 'ночь':
        names.append(current)
        if names[0] == 'розалина' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/rvNNpofHDz')
            #names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'мармарис' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/kgJnzMkcfw')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'анна' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/zZNjnN9ut2')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'элегант люкс' and names[len(names) - 1] ==  'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/vbFzXd02nN')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'александра' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/jREzYzVkiK')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'сенатор' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/nMPHUkruxO')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'изабелла 4' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/psb1OU5F9s')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'изабелла 6' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/xGwcMk6Gzo')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == '0101' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/9EuLQ0oq3E')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == '0102' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/aLuobZAH5g')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == '0103' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/uhXmBunX59')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == '0104' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/K2nZzPFmiM')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'пенал 8069' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/fOyL0Kw8IW')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'пенал 8070' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/9qKDYjHlyj')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'горка 8069' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/rPVXavv5ZL')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'стенка афродита' and names[len(names) - 1] == 'ночь':
            bot.send_photo(message.chat.id, 'https://imbt.ga/gFHjdfpnKg')
            # names.remove(names[len(names) - 1])
            names.clear()

    elif current == 'белый':
        names.append(current)
        if names[0] == 'розалина' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/ZuudtrTBA1')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'мармарис' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/t0rdR8wkFd')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'анна' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/P92vNIG0qB')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'элегант люкс' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/TuIOd8aQL4')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'александра' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/dE1lBc7pxQ')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'сенатор' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/eObbn4twmD')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'изабелла 4' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/GHi0DGrjQb')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'изабелла 6' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/aYPWExdyaR')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == '0101' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/IvUrBaIQCo')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == '0102' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/nrfeeC0jRf')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == '0103' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/J3fbUGG9jcf')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == '0104' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/WsxxcltFca')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'пенал 8069' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/3I1Fq3H9uW')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'пенал 8070' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/lNGW8HDvNE')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'горка 8069' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/1VuWUZ4zH2')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'стенка афродита' and names[len(names) - 1] == 'белый':
            bot.send_photo(message.chat.id, 'https://imbt.ga/bBOPVauc04')
            # names.remove(names[len(names) - 1])
            names.clear()

    elif current == 'дуб':
        names.append(current)
        if names[0] == 'розалина' and names[len(names) - 1] == 'дуб':
            bot.send_photo(message.chat.id, 'https://imbt.ga/mnJCvyj3Ly')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'мармарис' and names[len(names) - 1] == 'дуб':
            bot.send_photo(message.chat.id, 'https://imbt.ga/6HEILfar4Y')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'сенатор' and names[len(names) - 1] == 'дуб':
            bot.send_photo(message.chat.id, 'https://imbt.ga/MjFICKQm61')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'пенал 8069' and names[len(names) - 1] == 'дуб':
            bot.send_photo(message.chat.id, 'https://imbt.ga/B9tr2WXMvT')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'пенал 8070' and names[len(names) - 1] == 'дуб':
            bot.send_photo(message.chat.id, 'https://imbt.ga/nix9b8jgAG')
            # names.remove(names[len(names) - 1])
            names.clear()
        if names[0] == 'горка 8069' and names[len(names) - 1] == 'дуб':
            bot.send_photo(message.chat.id, 'https://imbt.ga/dQG67bCiDT')
            # names.remove(names[len(names) - 1])
            names.clear()'''


if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://izabella-mebel-bot.herokuapp.com/") # этот url нужно заменить на url вашего Хероку приложения
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)
