# Version 2.2 Good Password Fixed
# Librarys
import PySimpleGUI as sg
import random as r
import pyperclip
try:
    import config
    from config import theme_sel
    sg.theme(theme_sel)
except Exception:
    sg.theme('DarkGray12')


# Vars
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_small = letters.lower()
numbers = '0123456789'
symbols = '!@$%-*&'
password_mix = ''
templates = ['Шаблон #1', 'Шаблон #2', 'Шаблон #3']
numb = ['1','2','3','4','5','6','7','8','9','0']
alright = False

# UI Components
components_left = [
    [sg.Text('Количество символов')],
    [sg.Slider(range=(4, 40), default_value=12, orientation='h', key='-PASS_LEN-')],
    [sg.Checkbox('Цифры', key='-NUMB_BOX-', default=True)],
    [sg.Checkbox('Большие буквы', key='-BIG_L_BOX-')],
    [sg.Checkbox('Маленькие буквы', key='-SMALL_L_BOX-', default=True)],
    [sg.Checkbox('Спецсимволы', key='-SYM_BOX-')],
]

components_right = [
    [sg.InputText('', size=(37,1), key='-OUTPUT1-'), sg.Button('Копировать', size=(8,1), key='-COPY_PASS_1-')],
    [sg.InputText('', size=(37,1), key='-OUTPUT2-'), sg.Button('Копировать', size=(8,1), key='-COPY_PASS_2-')],
    [sg.InputText('', size=(37,1), key='-OUTPUT3-'), sg.Button('Копировать', size=(8,1), key='-COPY_PASS_3-')],
    [sg.InputText('', size=(37,1), key='-OUTPUT4-'), sg.Button('Копировать', size=(8,1), key='-COPY_PASS_4-')],
    [sg.Checkbox('Автокопирование первой строки', default=True, key='-AUTOCOPY_BOX-'),
     sg.Button('Объединить', size=(9,1),key= '-MIX-')],
    [sg.Checkbox('Надёжный', default=True, key='-GOOD_GEN-'), sg.Text('                             '), sg.Button('Сгенерировать', focus=True, size=(13,1), key='-GEN-')]
]

components_templ = [
    [sg.Button('Шаблон #1', k='-TEMP_1-'),sg.Button('!', k='-!_TMP_1-'),sg.Button('Шаблон #2', k='-TEMP_2-'),sg.Button('!', k='-!_TMP_2-'),sg.Button('Шаблон #3',k='-TEMP_3-'),sg.Button('!', k='-!_TMP_3-')],
]

# Components packing
layout = [
    [
        sg.Column(components_left), sg.VSeparator(), sg.Column(components_right),
    ],
    [sg.HSeparator()],
    [sg.Column(components_templ)],
]

# Functions
def numb_add():
    global password
    password += numbers
def s_let_add():
    global password
    password += letters_small
def b_let_add():
    global password
    password += letters
def sym_add():
    global password
    password += symbols
def gen():
    global length, i, password_out
    for i in range(length):
        password_out += r.choice(password)
def mix_all():
    global password_mix
    password_mix += values['-OUTPUT1-'] + '\n'
    password_mix += values['-OUTPUT2-'] + '\n'
    password_mix += values['-OUTPUT3-'] + '\n'
    password_mix += values['-OUTPUT4-']
    pyperclip.copy(password_mix)
    password_mix = ''
def temp_1():
    global password, length
    length = 12
    password = ''
    numb_add()
    s_let_add()
def temp_2():
    global password, length
    length = 12
    password = ''
    numb_add()
    s_let_add()
    b_let_add()
    sym_add()
def temp_3():
    global password, length
    length = 20
    password = ''
    numb_add()
    s_let_add()
    b_let_add()
    sym_add()
def tmp_len_add():
    global len_tmp
    len_tmp = values['']
def tmp_numb_add():
    global numbers_tmp
    numbers_tmp = True
def tmp_slet_add():
    global numbers_tmp
    numbers_tmp = True
def tmp_blet_add():
    global numbers_tmp
    numbers_tmp = True
def tmp_sym_add():
    global numbers_tmp
    numbers_tmp = True
def checker():
    global i, alright, password_out
    if numbers in password:
        while True:
            for i in numb:
                if i in password_out:
                    alright = True
                    break
                else:
                    alright = False
            if alright == False:
                password_out = ''
                gen()
            else:
                break
    else:
        pass



# PySimpleGUI window creating
window = sg.FlexForm('Password generator Standard Edition by GANTER', grab_anywhere=False)
window.Layout(layout)

# Window functions
while True:
    # Read window
    event, values = window.read()
    # Generate button
    if event == '-GEN-':        #values["NUMB_BOX"] == True:
        password = ''
        password_out = ''
        length = int(values['-PASS_LEN-'])
        if values['-NUMB_BOX-'] == True:
            numb_add()
        if values['-BIG_L_BOX-'] == True:
            b_let_add()
        if values['-SMALL_L_BOX-'] == True:
            s_let_add()
        if values['-SYM_BOX-'] == True:
            sym_add()
        if password != '':
            gen()
            if values['-GOOD_GEN-'] == True:
                checker()
        else:
            sg.popup('Выберите хотя бы один компонент для пароля')
            continue
        window['-OUTPUT1-'].update(password_out)
        if values['-AUTOCOPY_BOX-'] == True:
            pyperclip.copy(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    # Template button №1
    if event == '-TEMP_1-':
        temp_1()
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    # Template button №2
    if event == '-TEMP_2-':
        temp_2()
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    # Template button №3
    if event == '-TEMP_3-':
        temp_3()
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT1-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT2-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT3-'].update(password_out)
        password_out = ''
        gen()
        if values['-GOOD_GEN-'] == True:
            checker()
        window['-OUTPUT4-'].update(password_out)
        password_out = ''
    # Template info button №1
    if event == '-!_TMP_1-':
        tmp_1_info = 'Длина пароля - 12' + '\n'
        tmp_1_info += 'Цифры' + '\n'
        tmp_1_info += 'Маленькие буквы' + '\n'
        sg.popup(tmp_1_info)
        tmp_1_info = ''
    # Template info button №2
    if event == '-!_TMP_2-':
        tmp_1_info = 'Длина пароля - 12' + '\n'
        tmp_1_info += 'Цифры' + '\n'
        tmp_1_info += 'Маленькие буквы' + '\n'
        tmp_1_info += 'Большие буквы' + '\n'
        tmp_1_info += 'Символы' + '\n'
        sg.popup(tmp_1_info)
        tmp_1_info = ''
    # Template info button №3
    if event == '-!_TMP_3-':
        tmp_1_info = 'Длина пароля - 20' + '\n'
        tmp_1_info += 'Цифры' + '\n'
        tmp_1_info += 'Маленькие буквы' + '\n'
        tmp_1_info += 'Большие буквы' + '\n'
        tmp_1_info += 'Символы' + '\n'
        sg.popup(tmp_1_info)
        tmp_1_info = ''
    # Copy button №1
    if event == '-COPY_PASS_1-':
        password = values['-OUTPUT1-']
        pyperclip.copy(password)
        password = ''
    # Copy button №2
    if event == '-COPY_PASS_2-':
        password = values['-OUTPUT2-']
        pyperclip.copy(password)
        password = ''
    # Copy button №3
    if event == '-COPY_PASS_3-':
        password = values['-OUTPUT3-']
        pyperclip.copy(password)
        password = ''
    # Copy button №4
    if event == '-COPY_PASS_4-':
        password = values['-OUTPUT4-']
        pyperclip.copy(password)
        password = ''
    # Mix button
    if event == '-MIX-':
        if values['-OUTPUT1-'] != '' and values['-OUTPUT2-'] != '' and values['-OUTPUT3-'] != '' and values['-OUTPUT4-'] != '':
            mix_all()
        else:
            sg.popup('Невозможно сгенерировать пустые пароли')
    # Closing validator
    if event == sg.WINDOW_CLOSED:
        break