from time import sleep
from subprocess import run
from os import listdir
from os.path import isfile, join
from sys import argv
from random import random

backgrounds = []
unused = []
previousWallpaper = ""
# TODO: Make sure two wallpapers are not shown in a row

# Check if file ends with valid picture extension
def isPicture(fileName):
    extensions = ['.jpg', '.png', '.jpeg', '.gif']
    for extension in extensions:
        if fileName.endswith(extension):
            return True

    return False

# Change desktop wallpaper
def changeWallpaper(unused):
    global previousWallpaper
    print("Changing Background")
    nextIndex = int(random() * 1000) % len(unused)

    # Check to make sure two wallpapers aren't displayed in a row
    if previousWallpaper == str(unused[nextIndex]):
        nextIndex = (nextIndex + 1) % len(unused)

    picture = str(unused[nextIndex])
    print(picture)
    run(["feh", "--bg-scale", picture])
    previousWallpaper = str(unused[nextIndex])
    unused.pop(nextIndex)
    print("Sleeping")
    sleep(10)

path = argv[1]
print("Printing Image Directory")
print(str(path))

dirContents = listdir(path)

for fileName in dirContents:
    filePath = join(path, fileName)
    if isfile(filePath) and isPicture(fileName):
        backgrounds.append(filePath)

print("Printing images in given directory")
for back in backgrounds:
    print(back)

unused = list(backgrounds)

while True:
    # Use random number modulo unused length to pick the first wallpaper
    # First check to ensure unused list is not empty
    if len(unused) == 0:
        unused = list(backgrounds)

    changeWallpaper(unused)
