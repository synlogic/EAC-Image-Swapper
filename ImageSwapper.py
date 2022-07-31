from random import choice
from os import path, listdir
from shutil import copyfile
from sys import exit
from glob import glob
import cv2
import configparser
import traceback
from numpy import append
import requests

def CheckForUpdates():
    current_version = "v2.0.0"
    print(f"EAC Image Swapper version: {current_version}")
    print("Checking for updates | You can disable this in config.ini")
    
    try:
        response = requests.get("https://github.com/synlogic/EAC-Image-Swapper/releases/latest")
        if not response.url.endswith(current_version):
            print("Update Available! Download from https://github.com/synlogic/EAC-Image-Swapper/releases/latest")
            input("Press any key to continue..")
    except Exception:
        traceback.print_exc()
        print('Checking for updates failed...')
        return

def Resize(image, height=450, inter = cv2.INTER_AREA):
    # Resizes while maintaining aspect ratio.
    border_v = 0
    border_h = 0

    IMG_COL = 450
    IMG_ROW = 800

    if (IMG_COL/IMG_ROW) >= (image.shape[0]/image.shape[1]):
        border_v = int((((IMG_COL/IMG_ROW)*image.shape[1])-image.shape[0])/2)
    else:
        border_h = int((((IMG_ROW/IMG_COL)*image.shape[0])-image.shape[1])/2)

    image = cv2.copyMakeBorder(image, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
    
    dimensions = None
    (h, w) = image.shape[:2]

    r = height / float(h)
    dimensions = (int(w * r), height)

    resized = cv2.resize(image, dimensions, interpolation = inter)
    return resized

def GenerateConfig():
    sections = ('PATH', 'OPTIONS')
    options = [['PATH', 'photos', ''], ['PATH', 'exclusions', ''], ['OPTIONS', 'pause_on_complete', 'false'], ['OPTIONS', 'check_for_updates', 'true']]
    config = configparser.ConfigParser()
    #Generate new config
    if not path.exists('config.ini'):
        for section in sections:
            config.add_section(section)
        for option in options:
            config.set(option[0], option[1], option[2])
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print('Add "run.bat %COMMAND%" without quotations to VRChat launch options then add your launch options after')
        input("Open config.ini and input your VRChat photo path and VRChat EAC path | Press any key to exit.")
        exit()

    # Generate missing options
    elif path.exists('config.ini'):
        config.read('config.ini')
        for option in options:
            if config.has_option(option[0], option[1]):
                config.set(option[0], option[1], config.get(option[0], option[1]))
            else:
                if not config.has_section(option[0]):
                    config.add_section(option[0])
                config.set(option[0], option[1], option[2])
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    if config.get('PATH', 'photos') == "":
        input("Open config.ini and input your VRChat photo path and VRChat EAC path | Press any key to exit.")
        exit()
    return config

def GetPhotosInDirectory(dir):
    print(f'Finding files in {dir}')
    photos = []
    if isfile(dir):
        photos.append(file)
        return
    for file in listdir(dir):
        if (file.lower().endswith('.png') or file.lower().endswith('.jpg')) and not file.lower().endswith('_vr.jpg'):
            path = dir + '\\' + file
            print(f'     - {file}')
            photos.append(path)
    return photos

def run():
    config = GenerateConfig()
    if config.get('OPTIONS', 'check_for_updates').lower() == "true": CheckForUpdates()
    exclusions = config.get('PATH', 'exclusions').split('+')
    paths = config.get('PATH', 'photos').split('+')
    photos = []
    for path_ in paths:
        glob_pattern = path.join(path_, '*')
        photos = photos + GetPhotosInDirectory(path_)
        files = sorted(glob(glob_pattern), key=path.getctime)
        for file in files:
            if path.isdir(file) and not file in exclusions:
                photos = photos + GetPhotosInDirectory(file)
    try:
        new_photo = choice(photos)
    except IndexError:
        print('No photos to be found! Empty photos directory maybe?')
        input("Press any key to exit.")
        exit()
    img = cv2.imread(new_photo, 1)
    scaled_img = Resize(img)
    cv2.imwrite('scaled.png', scaled_img)
    copyfile('scaled.png', './EasyAntiCheat/SplashScreen.png')
    print("Image successfully scaled and replaced.")
    if config.get('OPTIONS', 'pause_on_complete').lower() == 'true':
        input("Pause on Complete enabled in config.ini, press any key to exit")

if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        traceback.print_exc()
        input("Something went wrong, press any key to exit..")
        exit()