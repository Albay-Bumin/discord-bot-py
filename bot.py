import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import sqlite3
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
import requests

BOT_TOKEN="BOT_TOKEN"
bot_prefix="c*"
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

extensions = ["fun", "doviz", "hiyar", "info", "music", "ucak", "welcome"]
server_list = []
welcome = 0

async def change_presence():
    while True:
        await client.change_presence(game=discord.Game(name='c*help | c*yardim', type=2))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name='Currently on ' + str(len(client.servers)) + ' servers', type=2))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name='Currently accessing ' + str(len(set(client.get_all_members()))) + ' users', type=2))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print("Bot çevrimiçi!")
    print("İsim : {}".format(client.user.name))
    print("ID : {}".format(client.user.id))
    print(str(len(client.servers)) + " tane serverda çalışıyor!")
    print(str(len(set(client.get_all_members()))) + " tane kullanıcaya erişiyor!")
    print("Server List")
    print("-"*15)
    for server in client.servers:
        server_list.append(server)
        print(server)
    client.loop.create_task(change_presence())


@client.command(pass_context=True)
async def load(ctx, extension):
    role = "442688696886755338"
    if ctx.message.author.id == role:
        try:
            client.load_extension(extension)
            print("Loaded {}".format(extension))
        except Exception as error:
            print("{} cannot be loaded.[{}]".format(extension, error))

    else:
        await client.say("***You cannot use this command***")

@client.command(pass_context=True)
async def unload(ctx, extension):
    role ="442688696886755338"
    if ctx.message.author.id ==role:
        try:
            client.unload_extension(extension)
            print("Unloaded {}".format(extension))
        except Exception as error:
            print("{} cannot be unloaded.[{}]".format(extension, error))

    else:
        await client.say("***You cannot use this command***")

@client.command(pass_context=True)
async def reload(ctx, extension):
    role ="442688696886755338"
    if ctx.message.author.id ==role:
        try:
            client.unload_extension(extension)
            client.load_extension(extension)
            print("Reloaded {}".format(extension))
            await client.say("{} Adlı Modül yeniden başlatıldı.".format(extension))
        except Exception as error:
            print("{} cannot be reloaded.[{}]".format(extension, error))


    else:
        await client.say("***You cannot use this command***")


@client.event
async def on_server_join(server):
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
    embed = discord.Embed(
        colour = 0x547e34,
        title = ":inbox_tray: | Bot Added To New Server",
        description = ""
    )
    embed.set_thumbnail(url=server.icon_url)
    embed.add_field(name='__Server Name__', value=str(server))
    embed.add_field(name='__Owner__', value=str(server.owner))
    embed.add_field(name='__Member Count__', value=str(server.member_count))
    embed.add_field(name='__Server Region__', value=server.region)
    embed.add_field(name='__Roles (%s)__' % str(role_length), value=roles)
    embed.set_footer(text='Created: %s' % time)

    await client.send_message(client.get_channel('488375580723642379'), embed=embed)


@client.event
async def on_server_remove(server):
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
    embed = discord.Embed(
        colour = 0x8C111F,
        title = ":outbox_tray: | Bot Deleted From a Server",
        description = ""
    )
    embed.set_thumbnail(url=server.icon_url)
    embed.add_field(name='__Server Name__', value=str(server))
    embed.add_field(name='__Owner__', value=str(server.owner))
    embed.add_field(name='__Member Count__', value=str(server.member_count))
    embed.add_field(name='__Server Region__', value=server.region)
    embed.add_field(name='__Roles (%s)__' % str(role_length), value=roles)
    embed.set_footer(text='Created: %s' % time)

    await client.send_message(client.get_channel('488375580723642379'), embed=embed)

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print("{} cannot be loaded.[{}]".format(extension, error))

    @client.event
    async def on_member_join(member):
        server = member.server.id
        con = sqlite3.connect("welcome.db")
        cursor = con.cursor()
        oku = cursor.execute("SELECT kanal,sv FROM wel")
        row = oku.fetchone()
        if row[1] == server:
            print("yep")
        else:
            print("sad") 

        for sey in oku.fetchall():
            canal = client.get_channel('{}'.format(sey[0])) # ID of channel Welcome


        url = requests.get(member.avatar_url)

        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((130, 130));
        bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)

        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('avatar.png')

        avatar = Image.open('avatar.png')
        fundo = Image.open('bemvindo.png')
        fonte = ImageFont.truetype('font\Oswald-Regular.ttf', 45)
        escrever = ImageDraw.Draw(fundo)
        escrever.text(xy=(180, 165), text=member.name, fill=(53, 59, 72), font=fonte) # output name when the user join!
        fundo.paste(avatar, (40, 90), avatar)
        fundo.save('bv.png')
        await client.send_file(canal, 'bv.png')

    @client.event
    async def on_member_remove(member):
        con = sqlite3.connect("welcome.db")
        cursor = con.cursor()
        oku = cursor.execute("SELECT kanal FROM wel")
        for sey in oku.fetchall():
            canal = client.get_channel('{}'.format(sey[0])) # ID of channel Welcome

        url = requests.get(member.avatar_url)

        avatar = Image.open(BytesIO(url.content))
        avatar = avatar.resize((130, 130));
        bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)

        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('avatar.png')

        avatar = Image.open('avatar.png')
        fundo = Image.open('bye.png')
        fonte = ImageFont.truetype('font\Oswald-Regular.ttf', 45)
        escrever = ImageDraw.Draw(fundo)
        escrever.text(xy=(180, 165), text=member.name, fill=(53, 59, 72), font=fonte) # output name when the user join!
        fundo.paste(avatar, (40, 90), avatar)
        fundo.save('gule.png')
        await client.send_file(canal, 'gule.png')






client.run(BOT_TOKEN)
