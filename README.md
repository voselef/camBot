# About CamBot Project:
This project about a discord bot that can capture photos with discord commands and send it to channel. With this project you can watch your bird, plant, child with just arduino and OV7670 camera module.
## Physical Requirements:
- 2 Arduino Uno/Nano/Mega/Leo...
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
- Then create a folder named "out" in the "C:" folder

## Configure First Arduino

Upload code to First Arduion from "camBot/1st Arduino/OV7670.ino"

## Configure Second Arduion

Upload code to Second Arduino from "camBot/2nd Arduino/2ndArduino.ino"

We'll use second Arduino for creating communication between first Arduino and discord bot. While we are using java for capturing picture, we can't create Serial connection with first Arduino because of intensity. Therefore we need to use digitalRead for creating connection.

Connect First Arduino and Second Arduino according to schema given.

![resim_2023-06-17_195207782](https://github.com/voselef/camBot/assets/90857438/30362677-7f0e-49df-8d48-68f7697cec4d)

## Configure Discord Bot
- Download discordbot folder to your computer.
- Open cmd and write `cd [downloaded folder path]`
- Write these commands in order. 
  - `pip install discord` press enter and wait to uploaded.
  - After than `pip install pyserial` press enter and wait to uploaded.
  - After than `pip install pillow` press enter and wait to uploaded.

- After than open main.py and change some variables from "CONFIGURATIONS" part.
  - Write folder path that you run in main.py. VAriable: filePath
  - Write bot token. Variable: token[^3]
  - Write port that you connected to 2nd Arduino. Variable: secondArduinoPort
  - save and exit.

# Running
Your project is ready for running. Before running you need to do something every opening.
1. Open cmd and go to bin folder via writing this: `cd C:\Program Files (x86)\Java\jdk-1.8\bin`
2. After than write `java code.SimpleRead`

Java is ready for capturing photo. Open discord bot:
1. Open cmd and write `cd [File path of main.py]`
2. Write `python main.py` [^4]

If a message with p content arrives java will be save photo to "C:/out" folder and discord bot will send it to channel.

You can ask whatever you need about project

Enjoy your project :tada:

[^1]: You need to download x86 jdk 8u371 even if you have x64 processor.
[^2]: This project made for Windows OS. If you want to run in Linux or MacOS you need to update libraries and rewrite codes.
[^3]: You don't need to worry about token. If you are running discord bot in your own computer, its impossible to anyone acces token unless you are using web server.
[^4]: If it didn't work you can try `py main.py`or `python3 main.py`
