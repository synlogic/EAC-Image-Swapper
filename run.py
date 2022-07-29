from random import choice
from os import path, listdir
from genericpath import isfile
from shutil import copyfile
import cv2
import configparser
import traceback

def resize(image, height=450, inter = cv2.INTER_AREA):
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
    resized = cv2.resize(image, (800,450), interpolation = inter)  # Enforce 800x450
    return resized

def run():
    config = configparser.ConfigParser()
    if not path.exists('config.ini'):
        config['PATH'] = {'Photos': ''}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print('Add "run.bat %COMMAND%" without quotations to VRChat launch options then add your launch options after')
        input("Open config.ini and input your VRChat photo path and VRChat EAC path | Press any key to exit.")
        quit()
    else:
        config.read('config.ini')
        if config.get('PATH', 'photos')== "" or './EasyAntiCheat/SplashScreen.png' == "":
            input("Open config.ini and input your VRChat photo path and VRChat EAC path | Press any key to exit.")
            quit()
    
    photos_path = config.get('PATH', 'photos')
    current_photo = './EasyAntiCheat/SplashScreen.png'
    new_photo = ""
    while not new_photo.endswith('.png') and not new_photo.endswith('.jpg'):
        new_photo = photos_path + "/" + choice(listdir(photos_path))
        if path.isdir(new_photo):
            try:
                new_photo = new_photo + '/' + choice(listdir(new_photo))
            except Exception as e:
                traceback.print_exc(e.__str__)
                input("Something went wrong, press any key to exit..")
                continue

    img = cv2.imread(new_photo, 1)
    scaled_img = resize(img)
    cv2.imwrite('scaled.png', scaled_img)

    copyfile('scaled.png', './EasyAntiCheat/SplashScreen.png')

if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        traceback.print_exc(e.__str__)
        input("Something went wrong, press any key to exit..")
        quit()
