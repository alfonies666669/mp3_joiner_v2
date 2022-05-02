import subprocess
import os

path_to = r''


def main_loop():
    cnt = 0
    common_list = []
    common_el = ''
    cmd_files = subprocess.check_output(f'dir /b', shell=True, cwd=path_to).decode('utf-8')
    list_files = [row.replace('\r', '') for row in cmd_files.split('\n')]
    del list_files[-1]
    how_much = int(input("How: "))
    files = [x.join('""') for x in list_files]
    # max_value = int(len(files)) // int(how_much)
    while len(files) != 0:
        common_list.append(files[0:how_much])
        common_el = ['+'.join(i) for i in common_list]
        subprocess.run(f'copy /b {common_el[0]} "joined_{cnt}.mp3"', shell=True)
        common_list.clear()
        common_el = ''
        cnt += 1
        del files[0:how_much]


main_loop()
