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
async def about(ctx):
    embed = discord.Embed(title="Info about me", description="This is who made me and my lib.", color=0xeee657)
    
    embed.add_field(name="Author", value="WolfBane#5559", inline=False)
    embed.add_field(name="Lib", value="Discord.py", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def updates(ctx):
    embed = discord.Embed(title="Update Logs", description="My most recent update!", color=0xeee657)
    
    embed.add_field(name="Update log 1.1", value="+ This command + Updated Help Command -Bugs", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def watmyid(ctx):
    ctx.message.send(message.author.id)
    
    

    
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Testing Bot One Help System", description="Hello, this is a list of all of my commands :D", color=0xeee657)
    
    embed.add_field(name="greet", value="This command greets people.", inline=False)
    embed.add_field(name="about", value="This command shows information about the bot.", inline=False)
    embed.add_field(name="updates", value="This command shows the bot's update logs.", inline=False)
    embed.add_field(name="watmyid", value="This command shows your userid", inline=False)
    
    await ctx.send(embed=embed)

bot.run('NDY5ODkzMzI1NzgxMDczOTIz.DjUn9Q.OcqLxPx9g6gEMSDzuTJSGJwuh4c')
