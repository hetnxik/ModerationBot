import disnake
import requests, urllib
from disnake.ext import commands

colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]

class shortenurl(commands.Cog, name='shortenurl', description="Shorten a url"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="shorten a log url")
    async def Shortenurl(self, ctx, urlts, suffix):
        key = 'fcbfd96544b2e5d7b0be060cdb1022c927168'
        urllib.parse.quote(urlts)
        status = requests.get(f'http://cutt.ly/api/api.php?key={key}&short={urlts}&name={suffix}')

        if status.json()["url"]["status"] == 1:
            await ctx.channel.send("Link is already shortened.")
        elif status.json()["url"]["status"] == 2:
            await ctx.channel.send("Enter a valid link.")
        elif status.json()["url"]["status"] == 3:
            await ctx.channel.send("Suffix already taken, please change it.")
        elif status.json()["url"]["status"] == 4:
            await ctx.channel.send("There was a problem connecting to the api.\nContact developer for more info.")
        elif status.json()["url"]["status"] == 5:
            await ctx.channel.send("Link has invalid characters.")
        elif status.json()["url"]["status"] == 6:
            await ctx.channel.send("Can't shorten urls from that domain.")
        elif status.json()["url"]["status"] == 7:
            shortenurlEmbed = disnake.Embed(title = "Command `*shortenurl` => Success", value = f"This is the shortened url: https://cutt.ly/{suffix} .")
            await ctx.channel.send(embed=shortenurlEmbed)


def setup(client: commands.Bot):
    client.add_cog(shortenurl(client))