import os
import sys
import os.path
import shutil
from playsound import playsound
import winreg as reg

startupFile = "StartupSound.txt"
windowsStartupDir = os.environ['USERPROFILE'] + "\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Startup"
playsoundString = ""

def main():
    # run playsound with the passed in file location from a text file (need text file to save location of sound file)
    # you will have to call the script with the location of the file as shown in the README
    # we want to grab the 2nd index in argv as the first index is the name of this python file
    soundFileLocation = sys.argv[1]
    currentDir = os.getcwd()
    print (currentDir)
    print (windowsStartupDir)
    path = os.path.dirname(os.path.realpath(__file__)) 

    # copy files from current directory into the Startup folder if calling it out 
    if str(currentDir) is not str(windowsStartupDir):
        shutil.copy(os.path.normpath(path + "\\StartupSound.py"), windowsStartupDir)
        shutil.copy(os.path.normpath(path + "\\" + startupFile), windowsStartupDir)

    handleTextFile(path,soundFileLocation)

    with open(startupFile, 'r') as startupSoundFile:
        readFileContent = startupSoundFile.readline()
        readFileContent.replace('\n','')

    playsoundString = str(readFileContent)

    #play the sound with the value from the StartupSound.txt 
    playsound(playsoundString)


def handleTextFile(path,soundFileLocation):
    # create the text file if it is not in the same dir
    # if the soundFileLocation (path of the file) is not None then overwrite the existing file content
    os.chdir(windowsStartupDir)

    if not os.path.exists(startupFile):
        print("Creating StartupSound.txt in current directory!")
        with open(startupFile, "w"): pass
    
    if soundFileLocation is not None:
        with open(startupFile, "w") as openedFile:
            print(soundFileLocation)
            openedFile.write(str(soundFileLocation)) 


if __name__=='__main__':
    main()