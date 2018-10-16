import discord
from discord.ext import commands
import asyncio
import youtube_dl

class Music:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        await voice_client.disconnect()

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        #players[server.id]
        player.start()



def setup(client):
    client.add_cog(Music(client))
