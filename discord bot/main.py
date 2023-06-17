import discord
from discord.ext import commands
import serial
import time
from datetime import datetime
import os
from PIL import Image

# CONFIGURATIONS
filePath = r""
jpgFileCurrentPath = rf"{filePath}\o.jpg"
rotated_jpgFileCurrentPath = rf"{filePath}\p.jpg"
logPath = rf"{filePath}\log.txt"
token = "" # If you are using web server do not use that. (process.ENV.token)
secondArduinoPort = "COM4"
rotateKey = 1 # If you don't want to rotate your photo rewrite 0.

print(jpgFileCurrentPath)

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

client = discord.Client(intents=intents)
s_port = secondArduinoPort
s_f = 115200
s = serial.Serial(s_port, 115200, timeout=12)
@client.event
async def on_ready():
    print(f"Logged in as {client.user}. You are running camBot project by voselef :)")
    starttime = datetime.now()
    starttime2 = starttime.strftime("%Y-%m-%d %H:%M:%S")
    await client.change_presence(activity=discord.Streaming(name=f'{starttime2}', url='https://www.youtube.com/watch?v=kbJu9LPQAGE&list=LL&index=5'))

@client.event
async def on_message(message):
    #print(message.content)
    closekey = 0
    if closekey == 2:
        return
    if message.author == client.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        await message.reply("Unauthorized messsage type")
        return
    #if message.channel.id != [special channel id for using camBot]: # if you want the bot to only reply to a private channel that you choosed
    #   return
    if message.content.lower() == "fp":
        await message.reply(f"Bot is alive.")
    if message.content.lower() == "p":
        if closekey == 1:
            await message.reply("Capturing closed by bot owner.")
            return
        mesaj1 = await message.reply("Function processed. Please wait about 10 seconds.")
        s.write("p".encode('utf-8'))
        time.sleep(9)
        bmp_file = find_bmp_file(r"C:\out")
        bmp_file_path = fr"C:\out\{bmp_file}"
        bmp_to_jpg(bmp_file_path, jpgFileCurrentPath)
        if rotateKey == 1:
            rotate_image(jpgFileCurrentPath, rotated_jpgFileCurrentPath)
            file = rotated_jpgFileCurrentPath
        else:
            file = jpgFileCurrentPath
        with open(file, 'rb') as file:
            picture = discord.File(file)
            await message.channel.send(file=picture)
            await mesaj1.edit(content=f"Fonction completed. Requested by {message.author}")
            nowl = datetime.now()
            localtime = nowl.strftime("%Y-%m-%d %H:%M:%S")
            log = open(logPath, "a")
            log.write(f"\n{localtime} : Photo Captured By {message.author}"
                      f" and sent to {message.channel} channel. Server: {message.guild}\n")
            log.flush()
            log.close()

        while find_bmp_file(r"C:\out"):
            bmpfile3 = find_bmp_file(r"C:\out")
            os.remove(fr"C:\out\{bmpfile3}")

def bmp_to_jpg(bmp_path, jpg_path):
    try:
        image = Image.open(bmp_path)
        image.save(jpg_path, "JPEG")
    except Exception as e:
        print("BMP Error:", e)
def find_bmp_file(directory):
    for file in os.listdir(directory):
        if file.endswith(".bmp"):
            return file
    return None
def rotate_image(image_path, save_path):
    try:
        image = Image.open(image_path)
        rotated_image = image.rotate(180)
        rotated_image.save(save_path)
    except Exception as e:
        print("Error:", e)

client.run(token)
