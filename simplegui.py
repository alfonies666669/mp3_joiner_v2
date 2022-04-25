import PySimpleGUI as sg
from main import *

layout = [[sg.Text('Choose a folder')],
          [sg.Input(), sg.FolderBrowse(key='-FOLDER-')],
          [sg.Button('OK', key='ok')],
          [sg.Button('Cancel', key='Cancel')],
          [sg.Spin([i for i in range(1, 100)],
                   initial_value='0', key='-HOW-'), sg.Text('How many parts')]]

layout2 = [[sg.Text('Choose a folder')],
           [sg.Button('OK', key='ok')]]

window = sg.Window('Easy mp3 Joiner', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event in (sg.Button, 'ok'):
        a = path_to_folder(values['-FOLDER-'])
        b = how_much_in_folder(values['-HOW-'])
        if len(a) != 0 and isinstance(b, int):
            load_bar = int(len(a)) // int(b)
            #join()
            sg.Window('Loading', [[sg.ProgressBar(100, size=(35, 20), orientation='h', bar_color=('Green', 'White'), key='-BAR-')]],
                      ).read(close=True)
        else:
            sg.Popup('Choice the folder '
                     'And',
                     'How many parts you want to')

window.close()
