from discord.ext import commands
# import responses
import discord
from src import objects as ob
from src.get_yahoo_finance import get_simple_dict, make_message
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)
# channel = client.get_channel(int(ob.channel))
token = 'MTE4NDkzNTI4NjAwNjg4NjQ0MA.GsbUu6.1HrDw9QzTlpfW1mXDHDqVUAQ6vqTpOEJhDIxpQ'


@client.event
async def on_ready():
    print(f'---------------------------------------------')
    print(f'{client.user.name} has connected to Discord!')
    print(f'---------------------------------------------')

@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command(pass_context=True)
async def hello(ctx):
    ret_message = "Hello, World!"
    await ctx.send(ret_message)


###
###

@client.command(pass_context=True)
async def temp(ctx):
    try:
        await ctx.send("Cant be collect now or Not exist!")
    except:
        await ctx.send("Cant be collect now or Not exist!")

@client.command(pass_context=True)
async def places(ctx):
    try:
        await ctx.send("Cant be collect now or Not exist!")
    except:
        await ctx.send("Cant be collect now or Not exist!")

@client.command(pass_context=True)
async def add_station_to_collect(ctx):
    try:
        await ctx.send("Cant be collect now or Not exist!")
    except:
        await ctx.send("Cant be collect now or Not exist!")

@client.command(pass_context=True)
async def station_temp(ctx):
    try:
        await ctx.send("Cant be collect now or Not exist!")
    except:
        await ctx.send("Cant be collect now or Not exist!")


if __name__ == '__main__':
    client.run(token)
