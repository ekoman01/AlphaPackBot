import discord
from discord.ext import commands
import random
import os

TOKEN = ''

client = commands.Bot(command_prefix = '*')
client.remove_command('help')

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
    
@client.command(aliases=["Ice", "Black", "BlackIce" , "black_ice"])
async def BLack_Ice(ctx):
    await ctx.send("HAHA u wish")

@client.command()
async def pack(ctx):
    global pack
    pack = ("Full")
    await ctx.send(file=discord.File(f"D:/Programming/Bot/Animation.gif"))

@client.command()
async def open(ctx):
    global pack
    if pack == ("Full"):
        pack = ("Empty")
        randomloot = random.choice(os.listdir("D:/Programming/Bot/Loot"))
        loot = os.path.splitext(randomloot)[0]
        await ctx.send(file=discord.File(f"D:/Programming/Bot/Loot/{loot}.jpg"))
    elif pack == ("Empty"):
        await ctx.send("You have no packs.")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='How the pack opener works:')
    embed.add_field(name='help', value='This command..', inline=False)
    embed.add_field(name='ping', value='Pong!', inline=False)
    embed.add_field(name='get pack', value='Starts the loot roll', inline=False)
    embed.add_field(name='get open', value='Opens your pack and gives you random loot \n Good luck! ;)', inline=False)

    await ctx.send(author, embed=embed)



client.run(TOKEN)

