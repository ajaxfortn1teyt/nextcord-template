import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import os
import time
intents = nextcord.Intents.all()
intents.members = True
intents.messages = True
import datetime
import humanfriendly
client = commands.Bot(command_prefix='a?', intents=intents)

testingServerID = 973046336167510046

@client.event
async def on_ready():
  print("the bot is now online enjoy!")

  
@client.slash_command(name="repeat", description="Repeat anything you say!",guild_ids=[testingServerID,])
async def say(interaction : Interaction, message:str):
  await interaction.response.send_message(message)

client.run("YOUR TOKEN HERE")
