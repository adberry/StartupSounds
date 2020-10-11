import os
from playsound import playsound


def main(soundFileLocation):
    # run playsound with the passed in file location
    playsound('/path/to/a/sound/file/you/want/to/play.mp3')


if __name__=='__main__':
    main()