import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
from io import BytesIO
import aiohttp
import os

class Info:
    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def id(self, ctx, member:discord.Member=None):
        """Gets your ID or if you @mention a user it gets their id"""
        if member is None:
            await self.client.say(ctx.message.author.name + " ID: " + ctx.message.author.id)
        else:
            await self.client.say(member.name + " ID:" + member.id)

    @commands.command(pass_context=True)
    async def serverinvite(self, ctx):
        invite = await self.client.create_invite(ctx.message.channel, max_uses=100, xkcd=True)
        await self.client.send_message(ctx.message.author, "Server Invite Link: {}".format(invite.url))
        await self.client.send_message(ctx.message.channel, ":inbox_tray:I've send server invite link.Check your PM's.")

        print("Sunucuda davet linki oluşturuldu", ctx.message.author, ctx.message.server.name)

    @commands.command(pass_context=True)
    async def sunucudavet(self, ctx):
        invite = await self.client.create_invite(ctx.message.channel, max_uses=100, xkcd=True)
        await self.client.send_message(ctx.message.author, "Sunucu Davet Linkin: {}".format(invite.url))
        await self.client.send_message(ctx.message.channel, ":inbox_tray:Sunucu davet linki gönderdim.Özel mesajlarını kontrol et.")

        print("Sunucuda davet linki oluşturuldu", ctx.message.author, ctx.message.server.name)

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        server = ctx.message.server
        roles = [x.name for x in server.role_hierarchy]
        role_length = len(roles)

        if role_length > 50:  # Just in case there are too many roles...
            roles = roles[:50]
            roles.append('>>>> Displaying[50/%s] Roles' % len(roles))

        roles = ', '.join(roles);
        channelz = len(server.channels);
        time = str(server.created_at);
        time = time.split(' ');
        time = time[0];

        join = discord.Embed(description='%s ' % (str(server)), title='Server Name', colour=0x547e34);
        join.set_thumbnail(url=server.icon_url);
        join.add_field(name='__Owner__', value=str(server.owner) + '\n' + server.owner.id);
        join.add_field(name='__ID__', value=str(server.id))
        join.add_field(name='__Member Count__', value=str(server.member_count));
        join.add_field(name='__Text/Voice Channels__', value=str(channelz));
        join.add_field(name='__Server Region__', value=server.region);
        join.add_field(name='__Roles (%s)__' % str(role_length), value=roles);
        join.set_footer(text='Created: %s' % time);

        return await self.client.send_message(ctx.message.channel, embed=join);

    @commands.command(pass_context=True)
    async def serverbilgi(self, ctx):
        server = ctx.message.server
        roles = [x.name for x in server.role_hierarchy]
        role_length = len(roles)

        if role_length > 50:  # Just in case there are too many roles...
            roles = roles[:50]
            roles.append('>>>> Displaying[50/%s] Roles' % len(roles))

        roles = ', '.join(roles);
        channelz = len(server.channels);
        time = str(server.created_at);
        time = time.split(' ');
        time = time[0];

        join = discord.Embed(description='%s ' % (str(server)), title='Sunucu Ismi', colour=0x547e34);
        join.set_thumbnail(url=server.icon_url);
        join.add_field(name='__Kurucu__', value=str(server.owner) + '\n' + server.owner.id);
        join.add_field(name='__ID__', value=str(server.id))
        join.add_field(name='__Kullanıcı Sayısı__', value=str(server.member_count));
        join.add_field(name='__Yazı/Ses Kanalı Sayısı__', value=str(channelz));
        join.add_field(name='__Sunucu Bölgesi__', value=server.region);
        join.add_field(name='__Roller (%s)__' % str(role_length), value=roles);
        join.set_footer(text='Sunucu Açılma Tarihi: %s' % time);

        return await self.client.send_message(ctx.message.channel, embed=join);

    @commands.command(pass_context=True)
    async def avatar(self, ctx, member:discord.Member=None):
        if member is None:
            author= ctx.message.author

            embed1 = discord.Embed(
                colour = 0x547e34,
                title = "Avatar",
                description = ":camera_with_flash: " + author.name + " Profile Photo"
                )
            avatar1 = author.avatar_url
            embed1.set_image(url=avatar1)

            await self.client.send_message(ctx.message.channel, embed=embed1)
        else:
            embed = discord.Embed(
                colour = 0x547e34,
                title = "Avatar",
                description = ":camera_with_flash: " + member.name + " Profile Photo"
                )
            avatar = member.avatar_url
            embed.set_image(url=avatar)

            await self.client.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    async def shrug(self, ctx, member : discord.Member = None):
        if member is None:
            url = requests.get(ctx.message.author.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            member = ctx.message.author
            image = Image.open("template.jpeg")
            font = ImageFont.truetype("font/primetime.ttf", 175)
            draw = ImageDraw.Draw(image)
            draw.text((250, 425),member.name,(255,255,255),font=font)
            area = (50, 50)
            image.paste(avatar, area)
            image.save("resimler/test.jpeg")
            await self.client.send_file(ctx.message.channel, "resimler/test.jpeg", content="", filename="test.jpeg")

        else:
            url = requests.get(member.avatar_url)
            avatar = Image.open(BytesIO(url.content))
            member = ctx.message.author
            image = Image.open("template.jpeg")
            font = ImageFont.truetype("font/primetime.ttf", 175)
            draw = ImageDraw.Draw(image)
            draw.text((250, 425),member.name,(255,255,255),font=font)
            area = (50, 50)
            image.paste(avatar, area)
            image.save("resimler/test.jpeg")
            await self.client.send_file(ctx.message.channel, "resimler/test.jpeg", content="", filename="test.jpeg")

    @commands.command(pass_context=True)
    async def userinfo(self, ctx, user: discord.Member):
        embed = discord.Embed(title="{}'s Info".format(user.name), description="Member", color=0x547e34)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def kullanicibilgi(self, ctx, user: discord.Member):
        embed = discord.Embed(title="{}' Adlı Kişi Hakkında Bilgi".format(user.name), description="Bot Bumin", color=0x547e34)
        embed.add_field(name="Isim", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Durum", value=user.status, inline=True)
        embed.add_field(name="En yüksek role", value=user.top_role)
        embed.add_field(name="Katıldığı Tarih", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await self.client.say(embed=embed)

    @commands.command(pass_context = True)
    async def memberstats(self, ctx):
        online = 0
        idle = 0
        offline = 0
        dnd = 0
        bots = 0
        server = ctx.message.server
        for member in server.members:
            if str(member.status) == "online":
                online += 1
            elif str(member.status) == "idle":
                idle += 1
            elif str(member.status) == "offline":
                offline += 1
            elif str(member.status) == "dnd":
                dnd += 1
        embed = discord.Embed(name="Members Stats", description="Members Stats list is here", color=0x547e34)
        embed.set_author(name="Members Stats")
        embed.add_field(name="Online Members", value="Members= "+str(online))
        embed.add_field(name="Idle", value="Members= "+str(idle))
        embed.add_field(name="Dnd", value="Members= "+str(dnd))
        embed.add_field(name="Offline", value="Members= "+str(offline))
        await self.client.say(embed=embed)

    @commands.command(pass_context = True)
    async def kullanicidurum(self, ctx):
        online = 0
        idle = 0
        offline = 0
        dnd = 0
        bots = 0
        server = ctx.message.server
        for member in server.members:
            if str(member.status) == "online":
                online += 1
            elif str(member.status) == "idle":
                idle += 1
            elif str(member.status) == "offline":
                offline += 1
            elif str(member.status) == "dnd":
                dnd += 1
        embed = discord.Embed(name="Sunucu Üye Durumları", description="Durum Listeleri", color=0x547e34)
        embed.set_author(name="Durumlar")
        embed.add_field(name="Online Kullanıcı Sayısı", value="Members= "+str(online))
        embed.add_field(name="Boşta Kullanıcı Sayısı", value="Members= "+str(idle))
        embed.add_field(name="Rahatsız Etmeyin Kullanıcı Sayısı", value="Members= "+str(dnd))
        embed.add_field(name="Offline Kullanıcı Sayısı", value="Members= "+str(offline))
        await self.client.say(embed=embed)





def setup(client):
    client.add_cog(Info(client))
