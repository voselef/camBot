# About CamBot Project:
This project about a discord bot that can capture photos with discord commands and send it to channel. With this project you can watch your bird, plant, child with just arduino and OV7670 camera module.
## Physical Requirements:
- 2 Arduino UNO/NANO/MEGA/LEO...
- 1 Arduino OV7670 Camera Module 
## Software Requirements
- Arduino IDE
- Python3
- Java SE Development Kit 8u371 for x86(Doesn't matter you have x64 processor.[^1])
- Windows OS[^2]
# Guide
Before guide you need to donwload softwares which mentioned in "Software Requirements" part.
## Connect OV7670 to Ardunio
Connect your OV7670 Camera Module to Arduino with using this 
![circuit](https://github.com/voselef/cambot/assets/90857438/c5b0361e-3b09-41fa-ac24-c361e38b70cb)
- SIOC means SCL and
- SIOD means SDL
## Download comFile
After that, you need to download a comFile according to the port you connect the Arduino to. If you know port you connect the Arduino you can pass the next part
### How to learn port you connect to Arduino
- Open the "Device Manager"
- Find the Ports menu
- There are some ports that you connected to your computer.
-![ports](https://github.com/voselef/cambot/assets/90857438/e19cec5f-2572-4bae-b327-85d63216624c)
- You can see the port you connected to Arduino
### Configure comFile
- Download the comFile with the same name as the port you found from the "camBot/comFiles/"
- Extract the .rar file and move "code" folder to "C:/Program Files (x86)/Java/jdk[jdk version]/bin" folder.
## Configure Arducamp.rar

- Download Arducamp.rar from this repositorie
- Extract .rar file and move "win32com.dll" to "C:/Program Files (x86)/Java/jdk[jdk version]/jre/bin" folder.
- Open lib folder from extracted files and move "comm" file to C:/Program Files (x86)/Java/jdk[jdk version]/jre/lib/ext" folder.
- Open lib folder from extracted files and move "javax.comm.properties" file to "C:/Program Files (x86)/Java/jdk[jdk version]/jre/lib" folder
- Then create a folder named "out" in the "C:" folder.

[^1]: You need to download x86 jdk 8u371 even if you have x64 processor.
[^2]: This project made for Windows OS. If you want to run in Linux or MacOS you need to update libraries and rewrite codes.
