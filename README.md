# EAC Image Swapper
A python script for randomly picking a screenshot or image to use as the EAC splashscreen.

## Download the latest ImageSwapper.zip from https://github.com/synlogic/EAC-Image-Swapper/releases

# How To Use
1) Download the latest [release](https://github.com/synlogic/EAC-Image-Swapper/releases) **DON'T use code->download zip, that is for the source code only.**
2) Open steam, go to library and right click on VRChat.  Go to Manage->Browse Local Files
3) Unzip ImageSwapper.zip and place files into the local files folder
4) Open config.ini in a text editor and place the path of your photos directory. EX: photos = C:\Users\user\Pictures\VRChat
5) In steam again right click VRChat and go to properties.  In the launch options box insert "run.bat %COMMAND%" **before** any launch options
6) Run VRChat and enjoy seeing your screenshots or skebs or whatever else on your EAC screen!

# Extra info
You can adjust the timeout in the run.bat, if it's too low it may not update the picture before vrchat launches.

The image it chooses can be an image within a folder in the root folder.  EX: VRCHAT/2022-07/image.png

This was made and tested with VRChat in mind. However, this should work on other games with EAC as well as long as the EasyAntiCheat folder is in the same directory as ImageSwap.exe
