# Dynamic Backgrounds for i3
This is a simple slideshow script for i3 tiling window manager written in Python 3.

## Requirements
* Python3
* Pip3
* Feh

## Usage
1. Clone the repo

2. make main.py executable by command
```
chmod u+x main.py
```
otherwise i3 config won't exec it

3. Run the script by placing below command in your i3 config
```
exec your-path-to-the-folder/i3-dynamic-backgrounds/main.py -t 15 ~/Pictures/wallpapers/
```
The above command checks the directory Wallpapers for pictures, and shuffles the desktop background to change to a picture in the directory every 15 mins.

### Parameters
At the moment there are only 2 parameters, -t and the directory path.
* `-t` - How long to wait before changing the wallpaper, specified in minutes. Defaults to 1 minute.
* `/home/$USER/Pictures/Wallpaper` - Example directory containing images that should be shuffled. This argument must be supplied.
