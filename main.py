import os
import random
import discord
import dictionary
from discord import utils
from discord.ext import commands

# client
client = commands.Bot(command_prefix = '!')

# auto-role
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id = int("693809741880623154"))
    await member.add_roles(role)

# goodbye
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, id = int("697763834143703139"))
    await channel.send(f"{member} 𝐥𝐞𝐟𝐭 𝐮𝐬 𝐟𝐨𝐫 𝐚𝐧 𝐮𝐧𝐤𝐧𝐨𝐰𝐧 𝐫𝐞𝐚𝐬𝐨𝐧 :(")

# coin game
@client.command()
async def c(ctx, arg):
	if args == random.choice(var := ['орел', 'решка']):
		await ctx.send('Да! Тебе попалась сторона: ' + args)
	elif args not in var:
		await ctx.send('Выбери орел или решка')
	else:
		await ctx.send('Не повезло...попалась сторона: ' + var)

# ask game
@client.command()
async def a(ctx, *, args):
	if (exception := len(list(args))) < 3:
		await ctx.send('Отличный вопрос,а теперь задай нормальный')
	else:
		await ctx.send("Твой вопрос был: " + args + "\nОтвет: " + random.choice(dictionary.answers))

# helping
@client.command()
async def h(ctx):
	await ctx.send(dictionary.helping)

# info
@client.command()
async def i(ctx):
	await ctx.send(dictionary.info)

# who am i
@client.command()
async def w(ctx):
	await ctx.send(dictionary.who_am_i)

# nums game
@client.command()
async def rn(ctx, args, rangei):
	if (arg := int(args)) == (num := random.choice(range(0, (rangeint := int(rangei))))):
		await ctx.send('Везунчик!Я выбрал: ' + str(num) + " ,как и ты")
	elif arg > rangeint:
		await ctx.send('Число: ' + args + ',больше чем: ' + str(rangeint))
	else:
		await ctx.send('Лузер....Я загадал: ' + str(num))

# creator info
@client.command()
async def cr(ctx):
	await ctx.send(dictionary.creator_info)

# clearing
@client.command()
async def cl(ctx, n = 3):
    if n > 101:
        await ctx.send('Слишком большое число')
    else:
        await ctx.channel.purge(limit = n)

# members info
@client.command()
async def mi(ctx):
	await ctx.send("Всего: " + str(len(ctx.guild.members)) + "\nОнлайн: " + str(len(discord.members.Status.online)))

# random num bot choosing
@client.command()
async def rnb(ctx, args, rangei):
	if (bot_c := random.choice(range(0, (rangeint := int(rangei))))) == (arg := int(args)):
		await ctx.send('Я знаю!Твое число: ' + args + '\nЭто было проще простого')
	elif arg > rangeint:
		await ctx.send('Число ' + args + ' больше, чем ' + rangei + '. Меня - еврея, не обманешь')
	else:
		await ctx.send('Мой ответ был: ' + str(bot_c) + '\nЯ снова не угадал...')

# RUN
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
