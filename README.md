# StartupSounds
This script was made to run in the Windows Startup Folder and will play a sound when your computer starts up.

This script also assumes you are not manually launching the script within the Startup folder (most likely you would launch it in the GitRepo folder) and will break if you do so.

Supported sound files include .mp3 and .wav

# Setup Work
You will need to have phython installed on your machine, current is 3.9 at https://www.python.org/downloads/ 

This script uses playsound, you will have to install it:
https://pypi.org/project/playsound/

You may also need to install Pip:
https://phoenixnap.com/kb/install-pip-windows 

# How to Call the Script:
    In the directory where the script is located you will have to call it for it to be added to the startup folder the first time:
    python StartupSound.py "name of filepath to sound file"

    Example:
    python StartupSound.py "C:\Users\Adam Berry\Downloads\hello-there.mp3"