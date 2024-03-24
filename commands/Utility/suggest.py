import random, disnake, datetime
from disnake.ext import commands

colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]

class suggest(commands.Cog, name='suggest', description="use this to create a yes/no poll"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="suggest something (adds tick and cross reaction)")
    async def Suggest(self, ctx, *, suggestion):
        await ctx.message.delete()
        suggestionEmbed = disnake.Embed(title = f"suggestion by {ctx.author}", description = suggestion, colour = random.choice(colors), timestamp = datetime.datetime.utcnow())
        s = await ctx.channel.send(embed = suggestionEmbed)
        await s.add_reaction("✅")
        await s.add_reaction("❎")

def setup(client: commands.Bot):
    client.add_cog(suggest(client))