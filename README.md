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
Disable and replace default frontend. Set it to autostart.
```
cd /home/arcade/
sudo git clone https://github.com/fixongbg/simple_mame_frontend.git
sudo rm /home/arcade/shared/configs/ga.conf
sudo rm /home/arcade/.bash_profile
sudo mv /home/arcade/simple_mame_frontend/ga.conf /home/arcade/shared/configs/
sudo mv /home/arcade/simple_mame_frontend/.bash_profile /home/arcade/
```
Edit frontend script to your paths and set parameters to your liking.
```
sudo nano /home/arcade/simple_mame_frontend/
```
`MAME_CMD` - Commando to start GroovyMAME.
<br>
`ROMS_DIR` - Path to your roms folder.
<br>
`VISIBLE_ITEMS` - Number of visible items in the list. 
 <br>
 `PADDING` - Adjust this to control the left position of the list
```
# Path to your MAME executable and ROMs directory
MAME_CMD = "SDL_VIDEODRIVER=kmsdrm /usr/lib/mame/groovymame -switchres"
ROMS_DIR = "/home/arcade/shared/roms/mame"

# Number of visible items in the list
VISIBLE_ITEMS = 20  

# Left padding for the ROM list
PADDING = 5 # Adjust this to control the left position of the list
```
