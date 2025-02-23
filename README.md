# Simple MAME Frontend
This frontend is just a list of your roms. Pick a game and play. It's not perfect but it works. Again, simple. 
<br>
This is for GroovyArcade. Resolution should be set to `320x240p` in `gasetup`. 
<br>
<br>
![screenshot](screenshot.jpg) 
<br>
<br>
Run these commands to replace and autostart into this frontend in GroovyArcade.
<br>
<br>
Install `git` if you haven't already:
```
sudo pacman git
```
Download frontend.
```
cd /home/arcade/
sudo git clone https://github.com/fixongbg/simple_mame_frontend.git
sudo chown -R arcade:arcade simple_mame_frontend
sudo chmod 777 -R simple_mame_frontend
```
Disable default frontend in GroovyArcade.
```
sudo nano /home/arcade/shared/configs/ga.conf
```
Comment out the frontend and add path to the new frontend `simple.py`.
```
#!/bin/bash

if [[ $(tty) == /dev/tty1 ]] ; then
    sudo setterm --powerdown 0 --blank 0
    /opt/galauncher/startfe.sh
##  sudo gasetup
##  /opt/gasetup/login.sh
    python /home/arcade/simple_mame_frontend/simple.py
fi
```
Edit frontend script
```
sudo nano /home/arcade/simple_mame_frontend/simple.py
```
Change paths and parameters to your liking.
```
# Path to your MAME executable and ROMs directory
MAME_CMD = "SDL_VIDEODRIVER=kmsdrm /usr/lib/mame/groovymame -switchres"
ROMS_DIR = "/home/arcade/shared/roms/mame"

# Number of visible items in the list
VISIBLE_ITEMS = 20  

# # Adjust this to control the left position of the list.
PADDING = 5 
```
Clean up.
```
sudo rm /home/arcade/simple_mame_frontend/screenshot.jpg
```
