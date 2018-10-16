import discord
from discord.ext import commands
import sqlite3

class Database:
    def __init__(self, client):
        self.client = client


        con = sqlite3.connect("id.db")
        cursor = con.cursor()
        ekle = server.id
        cursor.execute("CREATE TABLE IF NOT EXISTS kisi (sunucu TEXT, prefix TEXT)")
        cursor.execute('INSERT INTO kisi(sunucu, prefix) VALUES ("{}", "{}")'.format(ekle, bot_prefix))
        oku = cursor.execute("SELECT sunucu, prefix FROM kisi")
        for sey in oku.fetchall():
            bot_prefix = ekle
        con.commit()
        con.close()
        print("herşey yolunda")




def setup(client):
    client.add_cog(Database(client))
