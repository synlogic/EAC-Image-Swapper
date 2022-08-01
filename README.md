[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W21OEBU)
# EAC Image Swapper
A python script for randomly picking a screenshot or image to use as the EAC splashscreen.

## Download the latest ImageSwapper.zip from https://github.com/synlogic/EAC-Image-Swapper/releases

# How To Use
1) Download the latest [release](https://github.com/synlogic/EAC-Image-Swapper/releases) **DON'T use code->download zip, that is for the source code only.**
2) Open steam, go to library and right click on VRChat.  Go to Manage->Browse Local Files
3) Unzip ImageSwapper.zip and place files into the local files folder
4) Open config.ini in a text editor and place the path of your photos directory. EX: photos = C:\Users\user\Pictures\VRChat
- You can append more directories by using + between them.  Example: C:\Users\user\Pictures\VRChat+C:\Users\user\Pictures\Skebs
5) Set Exclusions of folders within the phtos directories if needed.  You can append more directories just like photos.
6) (Optional) Go ahead and run ImageSwapper.exe once manually by double clicking.  This just insures that the first run is a new image.
7) In steam again right click VRChat and go to properties.  In the launch options box insert "run.bat %COMMAND%" **BEFORE** any launch options
8) Run VRChat and enjoy seeing your screenshots, skebs, or whatever else on your EAC splash screen!

# Video Tutorial
[eac tutorial.webm](https://user-images.githubusercontent.com/26206994/182078101-76e2988a-d060-4f3d-abc6-cabfeee51efc.webm)




# Extra info
The image it chooses can be an image within a folder in the root folder.  EX: VRCHAT/2022-07/image.png

This was made and tested with VRChat in mind. However, this should work on other games with EAC as well as long as the EasyAntiCheat folder is in the same directory as ImageSwap.exe
