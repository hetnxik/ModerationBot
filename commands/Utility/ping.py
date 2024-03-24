import random
import disnake
from disnake.ext import commands

colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]

class ping(commands.Cog, name='ping', description="Shows the ping of the bot"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="Shows latency of the bot.")
    async def Ping(self, ctx):
        pingEmbed = disnake.Embed(
            colour=random.choice(colors),
            title="Latency of the Bot",
            description=f"The latency of the bot is {round(self.client.latency * 1000)}ms"
        )

        await ctx.send(embed=pingEmbed)

def setup(client: commands.Bot):
    client.add_cog(ping(client))