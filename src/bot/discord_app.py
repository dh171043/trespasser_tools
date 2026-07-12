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
    pattern = r"(\d+)?d(\d+)([+-]\d+)?"
    match = re.match(pattern, input)
    if match:
        number, dice, arithmetic = match.groups()
        num_dice = int(number or 1)
        size_dice = int(dice)
        arithmetic_val = int(arithmetic or 0)

        dice_rolls = []
        for x in range(num_dice):
            dice_rolls.append(random.randint(1, size_dice))
        result = sum(dice_rolls) + arithmetic_val
        message = f"You rolled a {result} {dice_rolls} + {arithmetic_val}"
        return message, result, dice_rolls, arithmetic_val
    else:
        message = "Invalid format"
        return message

    
    

@bot.command()
async def roll(ctx, dice_input:str):
    message, result, dice_rolls, arithmetic_val = calculate_roll(dice_input)
    await ctx.send(f'{message}')

bot.run(TOKEN)


# # TESTING BLOCK
# if __name__ == "__main__":
#     test_input = "d8-2"
#     message, result, dice_rolls, arithmetic_val = calculate_roll(test_input)
#     print(message, result, dice_rolls, arithmetic_val)