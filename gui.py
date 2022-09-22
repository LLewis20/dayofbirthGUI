import PySimpleGUI as sg
from datetime import datetime
import doomsday
import inputValidation as iv

layout = [
    [sg.Text('Please enter your first name:')],
    [sg.Input(key='-name-', size=(20, 1))],
    [sg.Text('Please enter your birthday(dd/mm/yyyy):')],
    [sg.Input(key='-Birthday-', size=(20, 1))],
    [sg.Text('Please enter your favorite day:')],
    [sg.Input(key='-FavDay-', size=(20, 1))],
    [sg.Text(size=(20,2), justification='center', key='-OUTPUT-')],
    [sg.Button('Submit'), sg.Button('Exit')]
]


window = sg.Window("Calendar", layout)



while True:
    event, values = window.read()
    day, month, year = values["-Birthday-"].split('/')
    datefound = doomsday.days[doomsday.day_of_week(int(day),int(month),int(year))]
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Submit":
        output = iv.validate(values["-name-"], values["-FavDay-"], values["-Birthday-"])
        if(output[0] and values["-FavDay-"].upper() == datefound):
            window['-OUTPUT-'].update("Congrats you were born on your favorite day \N{thumbs up sign}!!!!")
        else:
            window['-OUTPUT-'].update("Unfortunately you were not born on your favorite day")