import PySimpleGUI as sg
import subprocess
import os
import shutil

path_to = ''
how_much = '0'
layout = [[sg.Text('Choose a folder')],
          [sg.Input(), sg.FolderBrowse(key='-FOLDER-')],
          [sg.Button('OK', key='ok'), sg.Button('Cancel', key='Cancel')],
          [sg.Spin([i for i in range(1, 100)],
                   initial_value='0', key='-HOW-'), sg.Text('How many parts')]]


def main_loop():
    cnt = 0
    common_list = []
    common_el = ''
    files = os.listdir(os.chdir(path_to))
    try:
        os.mkdir('joined')
    except FileExistsError:
        pass
    max_value = int(len(files)) // int(how_much)
    destination_path = path_to + r'\joined'
    while len(files) != 0:
        common_list.append(files[0:how_much])
        for i in common_list:
            common_el += '|'.join(i)
        subprocess.run(f'ffmpeg -i "concat:{common_el}" -acodec copy joined_{cnt}.mp3')
        new_file = f'joined_{cnt}.mp3'
        shutil.move(new_file, destination_path)
        common_list.clear()
        common_el = ''
        cnt += 1
        del files[0:how_much]
        sg.one_line_progress_meter('Loading', cnt, max_value, orientation='h', no_button=True)


def main_window():
    global path_to, how_much
    window = sg.Window('Easy mp3 Joiner', layout, element_justification='c')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event in (sg.Button, 'ok'):
            try:
                path_to = values['-FOLDER-']
                how_much = values['-HOW-']
            except:
                sg.Popup('Choice the folder '
                         'And',
                         'How many parts you want to')
            if len(path_to) != 0 and isinstance(how_much, int):
                main_loop()
    window.close()


main_window()
