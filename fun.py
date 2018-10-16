import discord
from discord.ext import commands
import random
import asyncio
import requests
from bs4 import BeautifulSoup
import aiohttp
import time

class Fun:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        embed = discord.Embed(colour=0x547e34)
        t1 = time.perf_counter()
        await self.client.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        embed.description = "My ping is `{}`ms.".format(round((t2-t1)*1000))
        await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author= ctx.message.author

        embed1 = discord.Embed(
            colour = 0x547e34,
            title = "Help Commands",
            description = ":inbox_tray:I've send commands list.Check your PM's."
        )
        avatar = author.avatar_url
        embed1.set_thumbnail(url=avatar)

        embed = discord.Embed(
            colour = 0x547e34,
            title = "Bot Commands",
            description = "Bot Owner:ALBAY BUMIN#9138\n\nRequired to use commands prefix:`c*`\n "
        )

        embed.set_footer(text="Albay Bumin")
        embed.add_field(name=":ping_pong:Fun", value="`ping`\n`dog`\n`cigarette`")
        embed.add_field(name=":money_with_wings:Currency",
        value="\n`dolar`\n`euro`\n`bist100`\n`gold`\n`sterling`\n`franc`\n`riyal`\n`japaneseyen`\n`ruble`\n`hkdollar`\n`audollar`\n`bitcoin`\n`ethereum`")
        embed.add_field(name=":information_source:Information", value="`userid`\n`serverinfo`\n`userinfo`\n`memberstats`\n`avatar`\n`serverinvite`\n`ban`\n`kick`\n`clear`")
        embed.add_field(name=":airplane:Plane Crash Info", value="`planecrashinfo`\n`planecrashinfo worst`\n`planecrashinfo voice`")
        embed.add_field(name="Follow Me",
        value="[Instagram](https://instagram.com/albay_bumin/) | [ Steam](https://steamcommunity.com/id/albaybumin) | [ Invite Bot](https://discordapp.com/api/oauth2/authorize?client_id=482845466766344192&permissions=8&scope=bot)", inline=False)

        await self.client.send_message(author, embed=embed)
        await self.client.send_message(ctx.message.channel, embed=embed1)

    @commands.command(pass_context=True)
    async def yardim(self, ctx):
        author= ctx.message.author

        embed1 = discord.Embed(
            colour = 0x547e34,
            title = "Yardım Komutları",
            description = ":inbox_tray:Komut listesini gönderdim.Özel Mesajları Kontrol Et."
        )
        avatar = author.avatar_url
        embed1.set_thumbnail(url=avatar)

        embed = discord.Embed(
            colour = 0x547e34,
            title = "Bot Komutları",
            description="Bot Yapımcısı:ALBAY BUMIN#9138\n\nKomutları kullanmak için tanımlı prefix:`c*`\n "
        )

        embed.set_footer(text="Albay Bumin")
        embed.add_field(name=":ping_pong:Eğlence", value="`ping`\n`kopek`\n`sigara`")
        embed.add_field(name=":money_with_wings:Döviz",
        value="\n`dolar`\n`euro`\n`bist100`\n`altin`\n`sterlin`\n`frank`\n`riyal`\n`japonyeni`\n`rusrublesi`\n`hkdolar`\n`audolar`\n`bitcoin`\n`ethereum`")
        embed.add_field(name=":information_source:Bilgilendirme", value="`userid`\n`serverbilgi`\n`kullanicibilgi`\n`kullanicidurum`\n`avatar`\n`sunucudavet`\n`ban`\n`kick`\n`sil`")
        embed.add_field(name=":airplane:Plane Crash Info", value="`planecrashinfo`\n`planecrashinfo worst`\n`planecrashinfo voice`")
        embed.add_field(name="Follow Me",
        value="[Instagram](https://instagram.com/albay_bumin/) | [ Steam](https://steamcommunity.com/id/albaybumin) | [ Botu Davet Et](https://discordapp.com/api/oauth2/authorize?client_id=482845466766344192&permissions=8&scope=bot)", inline=False)

        await self.client.send_message(author, embed=embed)
        await self.client.send_message(ctx.message.channel, embed=embed1)

    @commands.command(pass_context=True)
    async def kopek(self, ctx):
        author= ctx.message.channel
        urll = ["https://random.dog/1925d792-11db-4778-8b2b-c43ac6d7e871.gif" ,
                "https://random.dog/de674643-9f77-477c-89dd-e8043976db87.jpg" ,
                "https://random.dog/ace571c3-c47e-4c52-93f3-9e3247c62ca9.jpg" ,
                "https://random.dog/de674643-9f77-477c-89dd-e8043976db87.jpg" ,
                "https://random.dog/2059c82d-452f-4d80-bb11-818da1451511.jpg" ,
                "https://random.dog/06ec5d00-6da0-46cb-ab4a-f6ea1e6a461f.gif" ,
                "https://random.dog/e6e4f32c-bc93-461c-b785-e8a20c1c0be3.jpg" ,
                "https://random.dog/237e527f-df94-48a4-89b1-2e2f7d844627.gif" ,
                "https://random.dog/164d07b8-fdd6-4fd3-9356-e635d4859555.JPG" ,
                "https://random.dog/2b77b03c-3073-454e-957b-867580b3d005.jpg" ,
                "https://random.dog/c22c077e-a009-486f-834c-a19edcc36a17.jpg" ,
                "https://random.dog/258e44d2-14df-4b46-b032-52754c3d0d3e.jpg" ,
                "https://random.dog/751f84b1-524f-4da7-b6f6-aadae5ef9cc1.jpeg" ,
                "https://random.dog/d467a3b8-ade5-4d68-810a-95fbb32a3cfc.jpg" ,
                "https://random.dog/d28047c5-1bce-4b94-988a-d05d5c15d5fb.jpeg" ,
                "https://random.dog/6b3100c1-34a0-4795-8de6-82da13eec2af.jpg" ,
                "https://random.dog/abb31449-1a18-48e4-8fb6-1f92eb731b99.jpg" ,
                "https://random.dog/2505f628-614d-4521-a26b-70897a51d4fd.JPG" ,
                "https://random.dog/35d14852-2c6e-4cb6-94af-7de46ffc36d0.jpg" ,
                "https://random.dog/037c01a0-99b3-4757-90b5-04df9be427a6.JPG" ,
                "https://random.dog/e9c94b72-4f92-4d65-b43a-e6decf24976f.jpg" ,
                "https://random.dog/0886de63-9a5d-41c5-b750-4e7633f63ce1.jpg" ,
                "https://random.dog/5c9f8baf-7918-4545-bd86-8f441cf96f3e.jpg" ,
                "https://random.dog/b1e63fd1-1136-4aec-8b21-3d6e60d6134f.jpg" ,
                "https://random.dog/a18ee053-2efe-4da9-b18e-3aef7dad1fa3.jpeg" ,
               ]
        embed = discord.Embed(title="Rastgele Köpek Resmi", color=0x547e34)
        embed.set_image(url=random.choice(urll))
        await self.client.send_message(author, embed=embed)

    @commands.command(pass_context=True)
    async def dog(self, ctx):
        author= ctx.message.channel
        urll = ["https://random.dog/1925d792-11db-4778-8b2b-c43ac6d7e871.gif" ,
                "https://random.dog/de674643-9f77-477c-89dd-e8043976db87.jpg" ,
                "https://random.dog/ace571c3-c47e-4c52-93f3-9e3247c62ca9.jpg" ,
                "https://random.dog/de674643-9f77-477c-89dd-e8043976db87.jpg" ,
                "https://random.dog/2059c82d-452f-4d80-bb11-818da1451511.jpg" ,
                "https://random.dog/06ec5d00-6da0-46cb-ab4a-f6ea1e6a461f.gif" ,
                "https://random.dog/e6e4f32c-bc93-461c-b785-e8a20c1c0be3.jpg" ,
                "https://random.dog/237e527f-df94-48a4-89b1-2e2f7d844627.gif" ,
                "https://random.dog/164d07b8-fdd6-4fd3-9356-e635d4859555.JPG" ,
                "https://random.dog/2b77b03c-3073-454e-957b-867580b3d005.jpg" ,
                "https://random.dog/c22c077e-a009-486f-834c-a19edcc36a17.jpg" ,
                "https://random.dog/258e44d2-14df-4b46-b032-52754c3d0d3e.jpg" ,
                "https://random.dog/751f84b1-524f-4da7-b6f6-aadae5ef9cc1.jpeg" ,
                "https://random.dog/d467a3b8-ade5-4d68-810a-95fbb32a3cfc.jpg" ,
                "https://random.dog/d28047c5-1bce-4b94-988a-d05d5c15d5fb.jpeg" ,
                "https://random.dog/6b3100c1-34a0-4795-8de6-82da13eec2af.jpg" ,
                "https://random.dog/abb31449-1a18-48e4-8fb6-1f92eb731b99.jpg" ,
                "https://random.dog/2505f628-614d-4521-a26b-70897a51d4fd.JPG" ,
                "https://random.dog/35d14852-2c6e-4cb6-94af-7de46ffc36d0.jpg" ,
                "https://random.dog/037c01a0-99b3-4757-90b5-04df9be427a6.JPG" ,
                "https://random.dog/e9c94b72-4f92-4d65-b43a-e6decf24976f.jpg" ,
                "https://random.dog/0886de63-9a5d-41c5-b750-4e7633f63ce1.jpg" ,
                "https://random.dog/5c9f8baf-7918-4545-bd86-8f441cf96f3e.jpg" ,
                "https://random.dog/b1e63fd1-1136-4aec-8b21-3d6e60d6134f.jpg" ,
                "https://random.dog/a18ee053-2efe-4da9-b18e-3aef7dad1fa3.jpeg" ,
               ]
        embed = discord.Embed(title="Random Dog Picture", color=0x547e34)
        embed.set_image(url=random.choice(urll))
        await self.client.send_message(author, embed=embed)

    @commands.command(pass_context=True)
    async def sigara(self, context):
        embed1 = discord.Embed(title="SİGARA", color=0x547e34, description=":smoking::cloud::cloud:", colour=0x547e34)  # 🌕 🌑 🌓
        embed2 = discord.Embed(title="SİGARA", color=0x547e34, description=":smoking::cloud:", colour=0x547e34)
        embed3 = discord.Embed(title="SİGARA", color=0x547e34, description=":smoking:", colour=0x547e34)
        embed4 = discord.Embed(title="SİGARA", color=0x547e34, description="***Sigaranız bitti.***", colour=0x547e34)

        #channel = bot.get_channel("447674516278345729")
        channel = context.message.channel
        gamble_msg = await self.client.send_message(channel, embed=embed1)
        await asyncio.sleep(0.5)
        await self.client.edit_message(gamble_msg, embed=embed2)
        await asyncio.sleep(0.5)
        await self.client.edit_message(gamble_msg, embed=embed3)
        await asyncio.sleep(0.5)
        await self.client.edit_message(gamble_msg, embed=embed4)

    @commands.command(pass_context=True)
    async def cigarette(self, context):
        embed1 = discord.Embed(title="CIGARETTE", color=0x547e34, description=":smoking::cloud::cloud:", colour=0x547e34)  # 🌕 🌑 🌓
        embed2 = discord.Embed(title="CIGARETTE", color=0x547e34, description=":smoking::cloud:", colour=0x547e34)
        embed3 = discord.Embed(title="CIGARETTE", color=0x547e34, description=":smoking:", colour=0x547e34)
        embed4 = discord.Embed(title="CIGARETTE", color=0x547e34, description="***Your cigarette is over.***", colour=0x547e34)

        #channel = bot.get_channel("447674516278345729")
        channel = context.message.channel
        gamble_msg = await self.client.send_message(channel, embed=embed1)
        await asyncio.sleep(0.5)
        await self.client.edit_message(gamble_msg, embed=embed2)
        await asyncio.sleep(0.5)
        await self.client.edit_message(gamble_msg, embed=embed3)
        await asyncio.sleep(0.5)
        await self.client.edit_message(gamble_msg, embed=embed4)

    @commands.command(pass_context=True)
    async def kick(self ,ctx, user:discord.Member, *, reason:str=None):
        """Kicks someone from the server"""
        if reason is None:
            reason = "Ban çekicini konuştu."
            try:
                await self.client.kick(user)
            except discord.errors.Forbidden:
                    await self.client.say("Either I do no have permission, or you do not")
                    return

    @commands.command(pass_context=True)
    async def ban(self ,ctx, user:discord.Member, *, reason:str=None):
        """Kicks someone from the server"""
        if reason is None:
            reason = "Ban çekicini konuştu."
            try:
                await self.client.ban(user)
            except discord.errors.Forbidden:
                    await self.client.say("Either I do no have permission, or you do not")
                    return

    @commands.command(pass_context=True)
    async def sil(self, context, number : int):
        if number < 501:
       	    deleted = await self.client.purge_from(context.message.channel, limit=number)
       	    await self.client.send_message(context.message.channel, 'Bot Bumin {} mesaj sildi.'.format(len(deleted)))

        else:
            await self.client.say("Maximum 500 mesaj silebilirsin.")

    @commands.command(pass_context=True)
    async def clear(self, context, number : int):
        if number < 501:
       	    deleted = await self.client.purge_from(context.message.channel, limit=number)
       	    await self.client.send_message(context.message.channel, 'Bot Bumin delete {} message.'.format(len(deleted)))

        else:
            await self.client.say("You can delete maximum 500 message.")







def setup(client):
    client.add_cog(Fun(client))
