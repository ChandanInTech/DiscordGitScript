from discord.ext import commands
from Config import token

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')


@client.event
async def on_member_join(member):
    print(f'Hi {member}, Welcome to the DotSi')


@client.event
async def on_member_remove(member):
    print(f'Bye {member}')


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)} ms')


@client.command(pass_context=True, aliases=['addtask', 'addTask'])
async def add_task(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)} ms')


# @client.command()
# async def clear(ctx, ammount=5):
#     await ctx.channel.purge(limit=ammount)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used')


# @client.event
# async def on_message(message):
#     print(message)


@client.command()
async def sr(ctx, *, tickers):
    tickers = tickers.split()
    await ctx.send(f'you passed {len(tickers)} ticker/s, {tickers}')


def log_task(task):
    pass


client.run(token)
