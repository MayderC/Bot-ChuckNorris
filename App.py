import discord
from discord.ext import commands
from Token import myToken
from Peticion import peticion, req


bot = commands.Bot(command_prefix='!')

@bot.command()
async def norris(ctx):
    texto = peticion()
    await ctx.send(texto)

@bot.command()
async def joke(ctx):
    text = req()
    await ctx.send(text)

@bot.command()
async def info(ctx):
    embed=discord.Embed(title="Descripción", description="Soy un bot de chistes de Chuck Norris", color=0x13b2f6)
    embed.set_author(name="Mayder", url="https://github.com/MayderC/Bot-ChuckNorris", icon_url="https://avatars3.githubusercontent.com/u/44930667?s=400&u=41e287aeb5cbc2fe6812d701ee2bd45e21151570&v=4" )
    embed.add_field(name="Github", value="https://github.com/MayderC/Bot-ChuckNorris", inline=True)
    embed.set_footer(text="By MayderC")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(myToken())