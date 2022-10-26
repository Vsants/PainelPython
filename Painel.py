from PySimpleGUI import PySimpleGUI as sg;

#Layout
sg.theme('DarkBlue')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(40,4))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(40,4))],
    [sg.Checkbox('Lembrar login')],
    [sg.Button('Entrar')]
]

#Window
janela = sg.Window('Inicie uma sessão', layout)

#Event
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'User' and valores ['senha'] == 'Password@123456':
            print('Bem-vindo! Você iniciou uma nova sessão.')