import discord
from discord import utils
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')

# команда для очистки чата
@client.command()
async def clear(ctx, num = 5):
	await ctx.channel.purge(limit = num)

# авто-роль
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, id=int("693809741880623154"))
	await member.add_roles(role)

@client.event
async def on_member_remove(member):
	channel = discord.utils.get(member.guild.channels, id=int("693815346502565898"))
	await channel.send(f"{member} 𝘭𝘦𝘧𝘵 𝘶𝘴. 𝘉𝘺𝘦 𝘉𝘺𝘦!")

# RUN
token = os.environ.get('BOT_TOKEN')

client.run(str(token))