# Simple MAME Frontend
This frontend is just a list of your roms. Pick a game and play!
<br>
<br>
This guide is tailored for GroovyArcade but could be used elsewhere. Remember to adjust resolution to your liking under `gasetup`. 
<br>
<br>
Press `up/down` to pick a game.
<br>
Press `left/right` to go the next/previous character. 
<br>
Press `esc` to `Shutdown` or `Exit to shell`.
<br>
<br>
**DISCLAIMER!**
<br>
I'm not a programmer. This python script was made using ChatGPT, therefore I don't know the in's and out's of this code but it works!
<br>
<br>
![screenshot](screenshot.jpg) 
<br>
<br>
Install `git` if you haven't already:
```
 sudo pacman -Sy git
```
Download frontend.
```
cd /home/arcade/
sudo git clone https://github.com/fixongbg/simple_mame_frontend.git
sudo chmod 777 /home/arcade/simple_mame_frontend/smf.py
sudo chmod 777 /home/arcade/rom_titles.txt
```
Disable default frontend in GroovyArcade.
```
sudo nano /home/arcade/shared/configs/ga.conf
```
Comment out `frontend`
```
##frontend=attractplus
video.backend=KMS
monitor=generic_15
kernel_video_cmdline=monitor=generic_15 video=VGA-1:640x480iS
connector=VGA-1
```
Disable autostart scripts.
```
sudo nano /home/arcade/.bash_profile
```
Comment out `sudo gasetup` and `/opt/gasetup/login.sh` and add path to the new frontend `smf.py` at the bottom.
```
#!/bin/bash

if [[ $(tty) == /dev/tty1 ]] ; then
    sudo setterm --powerdown 0 --blank 0
    /opt/galauncher/startfe.sh
##  sudo gasetup
##  /opt/gasetup/login.sh
    python /home/arcade/simple_mame_frontend/smf.py
fi
```
Edit frontend script paramters (if needed).
```
sudo nano /home/arcade/simple_mame_frontend/smf.py
```
Change paths and parameters to your liking.
```
# Path to your MAME executable and ROMs directory
MAME_CMD = "/usr/lib/mame/groovymame"
ROMS_DIR = "/home/arcade/shared/roms/mame"

# Number of visible items in the list
VISIBLE_ITEMS = 16

# # Adjust this to control the left position of the list.
PADDING = 1
```
Clean up.
```
sudo rm /home/arcade/simple_mame_frontend/screenshot.jpg
sudo rm /home/arcade/simple_mame_frontend/README.md
```
