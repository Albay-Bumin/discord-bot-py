import discord
from discord.ext import commands
import time
import sqlite3
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
import requests

class Welcome:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def hgkanal(self,ctx, channel:discord.Channel):
        server = ctx.message.server.id
        con = sqlite3.connect("welcome.db")
        cursor = con.cursor()
        ekle = channel.id
        cursor.execute("CREATE TABLE IF NOT EXISTS wel (kanal INT, sv INT)")
        cursor.execute('INSERT INTO wel(kanal, sv) VALUES ("{}", "{}")'.format(ekle, server))
        oku = cursor.execute("SELECT kanal, sv FROM wel")


        con.commit()
        con.close()
        print("herşey yolunda")





def setup(client):
    client.add_cog(Welcome(client))
