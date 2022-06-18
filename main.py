from webserver import keep_alive
import os
import discord
from discord.ext import commands
bot=commands.Bot(command_prefix='!')
@bot.command()
async def info(ctx):

  
  await ctx.send(ctx.guild)
  await ctx.send(ctx.author)

@bot.command()
async def defensa(ctx):
    guild = ctx.guild
    channel = ctx.author.voice.channel
    await channel.connect()
    voice_client: discord.VoiceClient =discord.utils.get(bot.voice_clients,guild=guild)
    audio_source = discord.FFmpegOpusAudio('aud1.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
      
@bot.command()
async def descansar(ctx):
    await ctx.voice_client.disconnect()

keep_alive()

TOKEN = os.environ.get("TOKEN")

bot.run(TOKEN)
