import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 10')
    layout = [
        [sg.Text('', font='Franklin 26', expand_x=True, justification='right', pad=(10, 20), right_click_menu= theme_menu, key = '-TEXT-')],
        [sg.Button('Clear', expand_x=True, size=(6, 3)), sg.Button('Enter', expand_x=True, size=(6, 3))],
        [sg.Button('7', size=(6, 3), key='-SEVEN-'), sg.Button('8', size=(6, 3)), sg.Button('9', size=(6, 3)),
         sg.Button('*', size=(6, 3))],
        [sg.Button('4', size=(6, 3)), sg.Button('5', size=(6, 3)), sg.Button('6', size=(6, 3)),
         sg.Button('/', size=(6, 3))],
        [sg.Button('1', size=(6, 3)), sg.Button('2', size=(6, 3)), sg.Button('3', size=(6, 3)),
         sg.Button('-', size=(6, 3))],
        [sg.Button('0', expand_x=True, size=(6, 3)), sg.Button('.', size=(6, 3)), sg.Button('+', size=(6, 3))]
    ]
    return sg.Window('Calculator', layout)

theme_menu = ['menu', ['LightGrey1', 'dark', 'light', 'random']]
## layout basically defines the structure of the app

window = create_window('dark')
## read method wait for the program to read the input and execute

current_num = []
current_op = []
full_operation = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)

    if event in ['+', '-', '/', '*']:
        current_op.append(''.join(current_num))
        current_num = []
        current_op.append(event)
        print(current_op)

    if event == 'Clear':
        current_op = []
        current_num = []

    if event == 'Enter':
        current_op.append(''.join(current_num))
        results = eval(''.join(current_op))
        window['-TEXT-'].update(results)
        current_op = []

window.close()
