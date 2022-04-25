import subprocess
import os
import shutil

path_to_glob = ''
how_much_glob = 0
files = []


def path_to_folder(path_to):
    global path_to_glob, files
    path_to_glob = path_to
    files = os.listdir(os.chdir(path_to_glob))
    return files


def how_much_in_folder(how_much):
    global how_much_glob
    """:param how_much:           How many elements you want to
        :type how_much:            INT"""
    how_much_glob = how_much
    return how_much_glob


def join():
    global how_much_glob, path_to_glob, files
    try:
        os.mkdir('joined')
    except FileExistsError:
        pass
    common_list = []
    common_el = ''
    cnt = 0
    while len(files) != 0:
        common_list.append(files[0:how_much_glob])
        for i in common_list:
            common_el += '|'.join(i)
        subprocess.run(f'ffmpeg -i "concat:{common_el}" -acodec copy joined_{cnt}.mp3')
        new_file = f'joined_{cnt}.mp3'
        destination_path = path_to_glob + r'\joined'
        new_location = shutil.move(new_file, destination_path)
        common_list.clear()
        common_el = ''
        cnt += 1
        del files[0:how_much_glob]
