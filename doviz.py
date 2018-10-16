import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import aiohttp

class Doviz:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def dolar(self):
        dovizurl = "http://uzmanpara.milliyet.com.tr/doviz/"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("span",{"id":"usd_header_son_data"})
        name1 = gelen1_veri.text.strip()
        await self.client.say("**DOLAR: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def euro(self):
        dovizurl = "http://uzmanpara.milliyet.com.tr/doviz/"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("span",{"id":"eur_header_son_data"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**EURO: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def bist100(self):
        dovizurl = "http://uzmanpara.milliyet.com.tr/doviz/"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("span",{"id":"imkb_header_son_data"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**BIST100: **" + name1)

    @commands.command(pass_context=True)
    async def gold(self):
        dovizurl = "http://uzmanpara.milliyet.com.tr/doviz/"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("span",{"id":"gld_header_son_data"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Gold(gram): **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def altin(self):
        dovizurl = "http://uzmanpara.milliyet.com.tr/doviz/"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("span",{"id":"gld_header_son_data"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Gold(gram): **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def sterlin(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisGBP"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Sterlin: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def sterling(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisGBP"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Sterling: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def frank(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisCHF"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Frank: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def franc(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisCHF"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Franc: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def riyal(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisSAR"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Riyal: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def japonyeni(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisJPY"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Japon Yeni: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def japaneseyen(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisJPY"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Japanese Yen: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def rusruble(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisRUB"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Rus Rublesi: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def ruble(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisRUB"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Russian Ruble: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def hkdolar(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisHKD"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Hong Kong Doları: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def hkdollar(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisHKD"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Hong Kong Dollar: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def audolar(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisAUD"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Avustralya Doları: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def audollar(self):
        dovizurl = "https://anlikaltinfiyatlari.com/doviz"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("div",{"id":"satisAUD"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Australian Dollar: **" + name1 + " TRY")

    @commands.command(pass_context=True)
    async def bitcoin(self):
        dovizurl = "https://coinmarketcap.com/currencies/bitcoin/"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("span",{"class":"h2 text-semi-bold details-panel-item--price__value"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Bitcoin: **" + name1 + " USD")

    @commands.command(pass_context=True)
    async def ethereum(self):
        dovizurl = "https://coinmarketcap.com/currencies/ethereum/"
        r = requests.get(dovizurl)
        soup = BeautifulSoup(r.content, "html.parser")
        gelen1_veri = soup.find("span",{"class":"h2 text-semi-bold details-panel-item--price__value"})
        name1 = gelen1_veri.text.strip()
        #name = (gelen_veri[0].contents)
        await self.client.say("**Ethereum: **" + name1 + " USD")



def setup(client):
    client.add_cog(Doviz(client))
