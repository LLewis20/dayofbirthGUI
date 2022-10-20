import PySimpleGUI as sg
from datetime import datetime
import doomsday
import inputValidation as iv

layout = [
    [sg.Text('Please enter your first name:'),sg.Input(key='-name-', size=(20, 1)), sg.Text(size=(20,2),text_color=('red'), justification='center',  key='-ERROR1-')],
    [sg.Text('Please enter your birthday(dd/mm/yyyy):'),sg.Input(key='-Birthday-', size=(20, 1)), sg.Text(size=(20,2),text_color=('red'), justification='center', key='-ERROR2-')],
    [sg.Text('Please enter your favorite day:'),sg.Input(key='-FavDay-', size=(20, 1)), sg.Text(size=(20,2),text_color=('red'), justification='center', key='-ERROR3-')],
    [sg.Text(size=(20,2), justification='center', key='-OUTPUT-')],
    [sg.Button('Submit'), sg.Button('Exit')]
]

window = sg.Window("Calendar", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Submit":
        window['-ERROR1-'].update('')
        window['-ERROR2-'].update('')
        window['-ERROR3-'].update('')
        output = iv.validate(values["-name-"], values["-FavDay-"], values["-Birthday-"])
        if (output[0] == False):
            for i in range(len(output[1])):
                if (output[1][i] == "INVALID NAME"):
                    window['-ERROR1-'].update("*INVALID NAME")
                elif (output[1][i] == "INVALID FAVORITE DAY"):
                    window["-ERROR3-"].update("*INVALID FAVORITE DAY")
                elif (output[1][i] == "PLEASE ENTER A VALID DATE"):
                    window["-ERROR2-"].update("*INVALID DATE")
        elif(output[0] and values["-FavDay-"].upper() == iv.datefound(values["-Birthday-"])):
            window['-OUTPUT-'].update("Congrats you were born on your favorite day \N{thumbs up sign}!!!!")
        else:
            window['-OUTPUT-'].update("Unfortunately you were not born on your favorite day")