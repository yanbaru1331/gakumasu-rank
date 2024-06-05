import discord
import datetime
import os
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Range
import cal


intents = discord.Intents.all()  
intents.typing = False  
GUILD_ID = discord.Object(id=os.environ["GUID"])



class Myclient(discord.Client):
    def __init__(self, intents: discord.Intents):
        super().__init__(

            intents=intents)

        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=GUILD_ID)
        await self.tree.sync(guild=GUILD_ID)

r = Range[int, 0, 1500]

client = Myclient(intents=intents)
# 起動確認
print(intents.members)

@ client.event
async def on_ready():
    # 起動後PC側にメッセージ送信
    print(datetime.datetime.now().time(),
          "on_ready/discordVer", discord.__version__)
    await client.change_presence(activity=discord.Activity(name="/rank", type=discord.ActivityType.playing))


@client.tree.command(name="gaku-rank", description="ランク計算用コマンド")
@app_commands.choices(rank=[
        app_commands.Choice(name="S", value=1),
        app_commands.Choice(name="A+", value=2),
        app_commands.Choice(name="A", value=3),
        app_commands.Choice(name="B+", value=4),
        app_commands.Choice(name="B", value=5),
        # app_commands.Choice(name="C+", value=6),
        # app_commands.Choice(name="C", value=7),
        # app_commands.Choice(name="D+", value=8)
])
async def rank(
    interaction: discord.Interaction,
    rank: app_commands.Choice[int]=1,
    vo: r=0, da: r=0, vi: r=0
):
    res = cal.rankCal(rank.value,vo,da,vi)
    await interaction.response.send_message(f"Vo={vo},Da={da},Vi={vi}で、ランク{rank.name}に必要なスコアは{res}です")


client.run(os.environ['DISCORD_TOKEN'])
