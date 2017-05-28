import os
import shutil

from titlecase import titlecase

def get_target_dir():
    target_dir = input("Enter the full path of target directory " \
                        "(or press enter for current): ")
    if not target_dir:
        target_dir = os.getcwd()
    return target_dir


def get_file_names(directory):
    return os.listdir(directory)


def rename_files(files):
    for filename in files:
        new_filename = _rename_file(filename)
        new_filename = _format_as_title(new_filename)
        # print(f'Renaming {filename} to {new_filename}')
        shutil.move(filename, new_filename)
        # print(filename, new_filename)



def _rename_file(filename):
    dashes_removed = filename.split('-')

    return " ".join(dashes_removed)


def _format_as_title(filename):
    # Avoids renaming extension, too
    title, extension = filename.split('.')

    return f'{title.title()}.{extension}'


if __name__ == '__main__':
    directory = get_target_dir()
    os.chdir(directory)
    files = get_file_names(directory)
    rename_files(files)
    
