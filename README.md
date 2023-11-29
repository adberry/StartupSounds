# StartupSounds

This powershell script was made to run in the Windows Task Scheduler as a task.

Supported sound files include .wav.

# Setup Work

You will need to run the following in an admin powershell window: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

Then you will need to set up a task that will be ran whenever you want at login,unlock,etc.
You can take use the .xml in this repository to create a task similar to what I did.

Alternatively, you can create a task with your own triggers.
If you do, I would recommend the following be done under the Actions tab:
    Program/script textbox should say "powershell"
    Add arguemnts (optional) textbox should say -WindowStyle Hidden -File <insert_full_filepath_to_the_playSound.ps1_here>

# How to Call the Script:

In a powershell window: <filepath_to_the_ps1_file>\.\playSound.ps1

# Change the Sound That Plays

In the playSound.ps1, update the filepath to the audio file on your local PC.