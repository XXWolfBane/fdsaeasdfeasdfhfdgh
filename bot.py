import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
asycn def on_ready():
   print('Logged in as')
   print(bot.user.name)
   print(bot.userid)
   print('-------------')

@bot.command()
async def test(ctx):
    await.ctx.send('This is a Testing command')
      
 

bot.run('NDY5ODkzMzI1NzgxMDczOTIz.DjOWvQ.l3CHq42SXWlAKyvJXuVD2FHmQjk')
