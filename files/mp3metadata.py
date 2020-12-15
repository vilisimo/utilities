import os

from mutagen.easyid3 import EasyID3


def fill_metadata():
    os.chdir('target')
    files = os.listdir()
    for file in files:
        if file.startswith('.'):
            continue
        audio = EasyID3(file)
        name = file[:-4]
        audio["title"] = name
        audio.save()


if __name__ == '__main__':
    fill_metadata()