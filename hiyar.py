import discord
from discord.ext import commands

class Hiyar:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def atwer(self):
        await self.client.say("Bebişimi Takip Edin looo")
        await self.client.say("https://www.instagram.com/can_4238/")

    @commands.command(pass_context=True)
    async def burock(self):
        await self.client.say("Bebişimi Takip Edin looo")
        await self.client.say("https://www.instagram.com/burakvural00/")

    @commands.command(pass_context=True)
    async def saka(self):
        await self.client.say("Bebişimi Takip Edin looo")
        await self.client.say("https://www.instagram.com/m.erensaka/")


def setup(client):
    client.add_cog(Hiyar(client))
