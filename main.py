import telebot
import os
#from telebot import types
from datetime import datetime
import pandas as pd
from keyboa.keyboard import Keyboa
import curators
import neiro

token ='6721196106:AAHa9mYliRmwwaNmF1zG9kmwOL7wluA-5q0'
bot = telebot.TeleBot(token)

kyrs={}

#Функция, которая работает с файловой системой и выдает список курсов и их уроки
def Courses():
    #Введите полный путь к папке с вашим материалом
    root_dir = r'materials'
    list_Kurs = list()
    for root, dirs, files in os.walk(root_dir):
        list1 = list()
        list1.append(root.split('\\')[-1])  # выводим название текущего каталога
        for file in files:
            if file.endswith('.docx'):
                list1.append(file[1:-5])
        list_Kurs.append(list1)
    del list_Kurs[0]
    transposed_matrix = [[row[i] for row in list_Kurs] for i in range(len(list_Kurs[0]))]
    return transposed_matrix[0]

def All():
    root_dir = r'materials'
    list_Kurs = list()
    for root, dirs, files in os.walk(root_dir):
        list1 = list()
        list1.append(root.split('\\')[-1])  # выводим название текущего каталога
        for file in files:
            if file.endswith('.docx'):
                list1.append(file[:-5])
        list_Kurs.append(list1)
    del list_Kurs[0]
    transposed_matrix = [[row[i] for row in list_Kurs] for i in range(len(list_Kurs[0]))]
    return transposed_matrix

def Lessons(courses):
    matrix = All()
    # Находим индекс строки, содержащей целевую строку
    row_index = matrix[0].index(courses)
    # Формируем список значений из соответствующего столбца
    column_values = [row[row_index] for row in matrix]
    del column_values[0]
    return column_values



yes_or_not = [["Да", "Нет"]]
test_mode=[["Режим собеседования", "Режим экзамена"]]
all_course = ["Тест по всему курсу"]
kb_yes_or_not = Keyboa(items=yes_or_not, copy_text_to_callback=True).keyboard
kb_test_mode = Keyboa(items=test_mode, copy_text_to_callback=True).keyboard
kb_courses = Keyboa(items=Courses(), copy_text_to_callback=True).keyboard
keyboard1 = Keyboa(items=Lessons('introduction'), copy_text_to_callback=True).keyboard
kb_all_course = Keyboa(items=all_course, copy_text_to_callback=True).keyboard
kb_lessons = Keyboa.combine(keyboards=(keyboard1, kb_all_course))
keyboard2 = Keyboa(items=Lessons('process'), copy_text_to_callback=True).keyboard
kb_lections = Keyboa.combine(keyboards=(keyboard2, kb_all_course))

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'Тест по всему курсу':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)

        if call.data == 'lection_1':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)



        if call.data == 'lection_2':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)



        if call.data == 'lection_3':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)



        if call.data == 'lection_4':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)



        if call.data == 'lection_5':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)



        if call.data == 'lection_6':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)


        if call.data == 'lesson_1':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)


        if call.data == 'lesson_2':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)


        if call.data == 'lesson_3':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)


        if call.data == 'lesson_4':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)


        if call.data == 'lesson_5':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)


        if call.data == 'lesson_6':
            bot.send_message(call.message.chat.id, reply_markup=kb_test_mode,
                             text='Теперь следует выбрать режим нашей битвы! '
                                  '\nЕсли хочешь видеть ход всей битвы пошагово, тогда выбери режим "Собеседования".  '
                                  '\nЕсли же тебе важен только результат выбери режим "Экзаменационный".👇 ')
            user_id = call.message.chat.id
            write_to_excel(user_id)

        if call.data == 'Режим собеседования':
            bot.send_message(call.message.chat.id,
                             text='Выбран режим собеседования.'
                                  '\nТеперь начнем, нас ждут 10 интереснейших вопросов. '
                                  '\nЧтобы победить нужно подключится к своим воспоминаниям и сконцетрироваться на вопросах. '
                                  '\nЯ верю, что у тебя все получится! Начнем!')
            user_id = call.message.chat.id
            write_to_excel(user_id)



            bot.send_message(call.message.chat.id, reply_markup=kb_yes_or_not,
                             text='Тест закончен! Есть ли у тебя какие либо вопросы по теме?')



        if call.data == 'Режим экзамена':
            bot.send_message(call.message.chat.id,
                             text='Выбран режим экзамена.'
                                  '\nТеперь начнем, нас ждут 10 интереснейших вопросов. '
                                  '\nЧтобы победить нужно подключится к своим воспоминаниям и сконцетрироваться на вопросах. '
                                  '\nЯ верю, что у тебя все получится! Начнем!')
            user_id = call.message.chat.id
            write_to_excel(user_id)



            bot.send_message(call.message.chat.id, reply_markup=kb_yes_or_not,
                             text='Тест закончен! Есть ли у тебя какие либо вопросы по теме?')





        if call.data == 'Да':
            user_id = call.message.chat.id
            write_to_excel(user_id)
            msg = bot.send_message(call.message.chat.id, 'Назови свою группу, что бы я мог отправить аккаунт вашего куратора.')
            bot.register_next_step_handler(msg, handle_group_id)


        if call.data == 'Нет':
            bot.send_message(call.message.chat.id,
                             text='Ты большой молодец! Эта битва была сложной, но ты справился и приложил не мало усилий.')
            user_id = call.message.chat.id
            write_to_excel(user_id)



        if call.data == 'introduction':
            bot.send_message(call.message.chat.id, reply_markup=kb_lessons,
                             text='Ты выбрал тему, теперь тебе следует определиться с областью!'
                                  '\nТы будешь обыгрывать меня по всей теме или по определенному уроку?👇')
            user_id = call.message.chat.id
            write_to_excel(user_id)



        if call.data == 'process':
            bot.send_message(call.message.chat.id, reply_markup=kb_lections,
                             text='Ты выбрал тему, теперь тебе следует определиться с областью! '
                                  '\nТы будешь обыгрывать меня по всей теме или по определенному уроку?👇')
            user_id = call.message.chat.id
            write_to_excel(user_id)

def write_to_excel(user_id):
    date = datetime.now()
    df1 = pd.DataFrame([[user_id, date]],
                        columns=['User ID', 'Activity_Date'])
    with pd.ExcelWriter('user_activity.xlsx',
                        mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name='Users', index=False)
    df1.to_excel('user_activity.xlsx', sheet_name='Users', engine='xlsxwriter', index=False)

def handle_group_id(message):
    cource = message.text
    user_id = message.chat.id
    kyrs[user_id] = {}
    kyrs[user_id]['course'] = cource

    try:

        bot.send_message(message.chat.id, f'Отлично! Ты из группы {cource}! Вот контакты твоего куратора: {curators.get_curator_by_course(cource)} ')
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при получении информации о группе: {e}")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, reply_markup=kb_courses, text= 'Привет, студент! Тебя приветствует помощник Сити!'
                                                                     '\nЯ могу помочь тебе проверить знания в некоторых областях. Те что мне известны находятся на кнопках. '
                                                                     '\nВыбери тему и давай посмотрим кто кого переиграет?👇 ')
    user_id = message.chat.id
    write_to_excel(user_id)



bot.polling(none_stop=True)
