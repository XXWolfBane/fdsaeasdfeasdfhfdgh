import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")
    
@bot.command()
async def about(ctx)
   embed = discord.Embed(title="About me", description="This command shows you info about me!", color=0xeee657)
    
    embed.add_field(title="Author", value="WolfBane#5559" inline=False)
    
    await ctx.send(embed=embed)
    
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Testing Bot One Help System", description="Hello, this is a list of all of my commands :D", color=0xeee657)
    
    embed.add_field(name="greet", value="This command greets people.", inline=False)
    
    await ctx.send(embed=embed)

bot.run('NDY5ODkzMzI1NzgxMDczOTIz.DjUn9Q.OcqLxPx9g6gEMSDzuTJSGJwuh4c')
