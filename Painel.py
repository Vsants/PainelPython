from PySimpleGUI import PySimpleGUI as sg;

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Lembrar login')],
    [sg.Button('Entrar')]
]

#Window

#Event