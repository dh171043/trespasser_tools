import random
import os
import re
from dotenv import load_dotenv 
import discord
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "/", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}.')

def calculate_roll(input):
    dice_rolls = []
    if "+" not in input: input += "+0"
    number, dice, arithmatic = re.split(r"[d+-]", input)
    for x in range(int(number)):
        dice_rolls.append(random.randint(1, int(dice)))
    result = sum(dice_rolls) + int(arithmatic)
    message = f"You rolled a {result} {dice_rolls} + {arithmatic}"
    return dice_rolls, str(result), arithmatic, message

@bot.command()
async def roll(ctx, dice_input:str, dice_rolls:list, arithmatic):
    result = calculate_roll(dice_input)

    ctx.send(f'{result}')
    pass

# bot.run(TOKEN)


# TESTING BLOCK
if __name__ == "__main__":
    test_input = "3d8+2"
    dice_rolls, result, arithmatic, message = calculate_roll(test_input)
    print(message)