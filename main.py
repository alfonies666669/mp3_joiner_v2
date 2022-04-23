import subprocess
import os
import shutil
#cd
path_to_book = input("Path to file: ")
files = os.listdir(os.chdir(path_to_book))
try:
    os.mkdir('joined')
except FileExistsError:
    pass
common_list = []
common_el = ''
cnt = 0
how_much = int(input("How much: "))
while len(files) != 0:
    common_list.append(files[0:how_much])
    for i in common_list:
        common_el += '|'.join(i)
    subprocess.run(f'ffmpeg -i "concat:{common_el}" -acodec copy joined_{cnt}.mp3')
    new_file = f'joined_{cnt}.mp3'
    destination_path = path_to_book + r'\joined'
    new_location = shutil.move(new_file, destination_path)
    common_list.clear()
    common_el = ''
    cnt += 1
    del files[0:how_much]
