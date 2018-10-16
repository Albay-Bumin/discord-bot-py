import discord
from discord.ext import commands
import random

sayaci = []

class Ucak:
    def __init__(self, client):
        self.client = client

    @commands.group(pass_context=True)
    async def planecrashinfo(self):
        await self.client.say("Plane Crash Info: http://planecrashinfo.com")

    @planecrashinfo.command(pass_context=True)
    async def worst(self, ctx):
            kanal=ctx.message.channel
            embed1 = discord.Embed(
                colour = 0x547e34,
                title = "Plane Crash Info",
                description = "http://planecrashinfo.com"
            )
            embed1.add_field(name="planecrashinfo", value="100 WORST AVIATION DISASTERS")
            embed1.add_field(name="planecrashinfo", value="Fatal | Date | Location | Carrier | Type")
            embed1.add_field(name="1.", value="2907 | 09/11/2001 | New York City, New York | American /United Airlines | B767 / B767")
            embed1.add_field(name="2.", value="583 | 03/27/1977 | Tenerife, Canary Islands | Pan Am / KLM | B747")
            embed1.add_field(name="3.", value="520 | 08/12/1985 | Mt. Osutaka, Japan | Japan Air Lines | B747 / Il76")
            embed1.add_field(name="4.", value="349 | 11/12/1996 | New Delhi, India | Saudi / Kazastan | DC10")
            embed1.add_field(name="5.", value="346 | 03/03/1974 | Bois d' Ermenonville, France | Turkish Airlines | B747")
            embed1.add_field(name="6.", value="329 | 06/23/1985 | Atlantic Ocean West of Ireland | Air India | L1011")
            embed1.add_field(name="7.", value="301 | 08/19/1980 | Riyadh, Saudi Arabia | Saudi Arabian Airlines | L1011")
            embed1.add_field(name="8.", value="298 | 07/17/2014 | Hrabove, Ukraine | Malaysia Airlines | B-777")
            embed1.add_field(name="9.", value="290 | 07/03/1988 | Persian Gulf | Iran Air | A300")
            embed1.add_field(name="10.", value="275 | 02/19/2003 | Shahdad, Iran | Islamic Revolution's Guards Co. | Il-76MD")

            avatar = ctx.message.author.avatar_url
            embed1.set_thumbnail(url=avatar)
            await self.client.send_message(kanal, embed=embed1)

    @planecrashinfo.command(pass_context=True)
    async def voice(self, ctx):
        member = ctx.message.channel
        urll = ["ucak-ses/1.mp3" ,
                "ucak-ses/2.mp3" ,
                "ucak-ses/3.mp3" ,
                "ucak-ses/4.mp3" ,
                "ucak-ses/5.mp3" ,
                "ucak-ses/6.mp3" ,
                "ucak-ses/7.mp3" ,
                "ucak-ses/8.mp3" ,
                "ucak-ses/9.mp3" ,
                "ucak-ses/10.mp3" ,
               ]
        await self.client.send_file(member, random.choice(urll), content="", filename=random.choice(urll))


def setup(client):
    client.add_cog(Ucak(client))
