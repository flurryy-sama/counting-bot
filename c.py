import discord
from discord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix="c-", help_command=None)

number = 0
already_number = 0
channel_id = 888787230850691112

def read_setting():
    global number
    try:
        with open("setting.txt", "r") as file:
            number = int(file.readline().replace("\n", ""))
    except ValueError as e:
        print(e)
        number = 0
        print("No configs found...")
        print("Creating default setting...")
        os.remove("setting.txt")
        setting()


def setting():
    global number
    if "setting.txt" not in os.listdir():
        with open("setting.txt", "x") as file:
            file.write(str(number))
            file.flush()
            file.close()
    else:
        with open("setting.txt", "w") as file:
            file.write(str(number))
            file.flush()
            file.close()

@bot.event
async def on_ready():
    print('ready')

@bot.listen()
async def on_message(message):
    global channel_id, number, already_number
    if message.channel.id == channel_id:
        if not message.author.id == bot.user.id:
            if not message.author.bot:
                if str(message.content).isdigit():
                    if message.author.id == already_number:
                        await message.add_reaction(r"<:841606440678588437:844877846618177567>")
                        embed = discord.Embed(title=f"{message.author.name}, du darfst nur eine Zahl schreiben.", colour=discord.Colour.dark_red())
                        await message.channel.send(embed=embed)
                        number = 0
                        already_number = 0
                    else:
                        already_number = message.author.id
                        number += 1
                        if message.content == str(number):
                            emoji = '<:tick:888765648908476446>'
                            await message.add_reaction(emoji)
                        else:
                            await message.add_reaction(r"<:cross:888787001002819605>")
                            await asyncio.sleep(1)
                            await message.delete()
                            number += -1
                            already_number = 0
                        setting()

bot.run('ODI4MzA2NjE5MTYyNjg5NTU2.YGnqpw.5Op1hJgs_7QU9KjrPlm1hDgnvb8')
