import discord 
from discord.ext import commands
import datetime
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='-', description="Bot de ayuda")

#Respuesta
@bot.command()

async def ping(ctx):
    await ctx.send('pong')

#-sum n1 n2
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

#-info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Información básica del Bot",
    timestamp= datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server OWner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://infosertecblog.files.wordpress.com/2019/01/500px-python-logo-notext.svg_.png")

    await ctx.send(embed=embed)

#youtube
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    # Se mostrara el primer resultado de busqueda de videos
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

#Eventos
@bot.event
async def on_ready():
    game = discord.Game('Aprendiendo algo nuevo')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('El Bot se encuentra encendido')

bot.run('token')
