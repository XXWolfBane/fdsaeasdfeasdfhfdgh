import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$'

@bot.event
asycn def on_ready():
   print('Logged in as')
   print(bot.user.name)
   print(bot.userid)
   print('-------------')
 

bot.run('NDY5ODkzMzI1NzgxMDczOTIz.DjOWvQ.l3CHq42SXWlAKyvJXuVD2FHmQjk')
