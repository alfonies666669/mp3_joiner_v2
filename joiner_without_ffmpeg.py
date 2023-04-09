# coding: utf-8
import os
import shutil
import subprocess


def delete_files(path_to: str, files: list) -> str:
    if os.path.exists(path_to):
        os.chdir(path_to)
        for file in files:
            if os.path.exists(file):
                os.remove(file)
            else:
                return f"{file} do not found in {path_to}"
        return f'{files} removed'
    else:
        return f"{path_to} do not exist"


def create_destination_folder(path_to: str) -> str:
    folder_path = os.path.join(path_to, 'Merged_Files')
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(folder_path)
    return folder_path


def move_file(output_files: list, new_folder: str) -> str:
    if os.path.exists(new_folder):
        for output_file in output_files:
            if os.path.exists(output_file):
                shutil.move(output_file, new_folder)
            else:
                return f'{output_file} not exist'
    else:
        return f'{new_folder} not exist'
    return f'{output_files} moved to {new_folder}'


def merge_strings(strings: list, count: int) -> list:
    merged = []
    for i in range(0, len(strings), count):
        merged.append('+'.join(strings[i:i + count]))
    return merged


def main_loop(path_to: str, how_much: int, destination_folder=True, del_files=False):
    files = list(filter(lambda x: x.endswith('.mp3'), os.listdir(os.chdir(path_to))))
    merged_list = merge_strings(files, how_much)
    for cnt in range(0, len(merged_list)):
        subprocess.run(["copy", "/b", merged_list[cnt], f'Merged_{cnt + 1}.mp3'], shell=True)

    if destination_folder:
        new_folder = create_destination_folder(path_to)
        print(move_file(list(filter(lambda x: x.startswith('Merged_') and x.endswith('.mp3'),
                                    os.listdir(os.chdir(path_to)))), new_folder))

    if del_files:
        print(delete_files(path_to, files))


if __name__ == '__main__':
    main_loop(r'path/to/folder', 2)
