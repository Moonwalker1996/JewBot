import os
import random
import discord
from discord import utils
from discord.ext import commands

# client
client = commands.Bot(command_prefix = '!')

# команда для очистки чата
@client.command()
async def cl(ctx, num = 5):
	await ctx.channel.purge(limit = num)

# ИНФОРМАЦИЯ
@client.command()
async def info(ctx):
	await ctx.send("Привет! Коротко о сервере: Сервер Evrey's Plays для совместных игр и общения участников клуба Еврии битчес")

# орел/решка
@client.command()
async def coin(ctx, args):
	coin_vars = ['орел','решка']
	if args == random.choice(coin_vars):
		await ctx.send('Да! Правильный ответ: ' + args)
	else:
		await ctx.send('Неа...Подкинь еще раз')

# да/нет игра
@client.command()
async def ask(ctx, *, args):
	answers = ['Да','Возможно','Нет','Вероятнее всего','Может быть','Определённо нет','Определённо да', 'Не знаю','Интересный вопрос,но отвечать я на него не буду','Не уверен','Дай минуту подумать']
	await ctx.send('Твой вопрос:' + args + '\nОтвет:' + random.choice(answers))

# выход персонажа
@client.event
async def on_member_remove(member):
	channel = discord.utils.get(member.guild.channels, id=int("693815346502565898"))
	await channel.send(f"{member} 𝘭𝘦𝘧𝘵 𝘶𝘴. 𝘉𝘺𝘦 𝘉𝘺𝘦!")

# авто-роль
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, id=int("693809741880623154"))
	await member.add_roles(role)

# RUN
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
