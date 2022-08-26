#!/usr/bin/python

from time import sleep
from subprocess import run
from os import listdir
from os.path import isfile, join, exists
from sys import argv
from random import random

runtime = {
        'wallpapers' : [],
        'path' : "",
        'time' : 60
}

def isPicture(file):
    extensions = ['.jpg', '.png', '.jpeg']
    for extension in extensions:
        if file.endswith(extension) and isfile(file):
            return True

    return False

def handleArguments():
    global runtime
    for i in range(1, len(argv)):
        if argv[i] == "-t":
            i += 1
            num = float(argv[i])
            runtime["time"] = int(num*60)
        else:
            if exists(str(argv[i])):
                runtime["path"] = argv[i]

def filterPrevAndReturnPictures(prev):
    pictures = list(runtime['wallpapers'])

    if prev != "":
        pictures.remove(prev)

    return pictures

def getPicturesExlucingPrev(prev):
    dir = runtime['path']
    content = listdir(dir)

    for item in content:
        filePath = join(dir, item)
        if isPicture(filePath):
            runtime['wallpapers'].append(filePath)

    res = filterPrevAndReturnPictures(prev)
    return res


def setNewWallpaperAndreturnAsPrev(picture):
    run(["feh", "--bg-scale", picture])
    return picture

if __name__ == "__main__":
    prevPicture = ""
    while True:
        print("-------------------------")

        handleArguments()
        pictures = getPicturesExlucingPrev(prevPicture)
        print("possible pictures")
        print(pictures)
        print("prev pic -> " + prevPicture)

        index = int(random() * 1000) % len(pictures)
        picture = pictures[index]
        print(picture + " has set")

        prevPicture = setNewWallpaperAndreturnAsPrev(picture)
        runtime['wallpapers'].clear()

        print("-------------------------")

        sleep(runtime['time'])

