# YOUTUBE VIDEO TO MP3 CONVERTER

##### REQUIRES ffmpeg, youtube-dl and vim

### Installing requirements:
###### ARCH LINUX:
    sudo pacman -S ffmpeg
    sudo pacman -S youtube-dl
    sudo pacman -S vim

### How to use:
 **1.** Open your terminal run this commands
###### RUN:
	cd ~/mp3
	mv ~/mp3/getMusic.sh ~/.local/bin
	chmod +x ~/.local/bin/getMusic.sh
	
 **2.** Now, when you want to download any music open the terminal and run this command  
###### RUN:
    getMusic.sh
    
 **3**. Now, this will prompt you a vim file, copy the links of the youtube videos which you want to download as mp3.
 **4.** it will check if the video from the link has been already downloaded or not, if not downloaded then it will download the video convert it to mp3 format delete the video and put the *.mp3 into your ~/Music directory. 
## Warning:

 - This a **personal utility**, please use with caution.
 - Do not remove any .txt file from the **~/mp3** directory.
  

 





