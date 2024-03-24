import random
import disnake
from disnake.ext import commands

colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]

class say(commands.Cog, name='say', description="makes embed of the content passed"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(aliases = ["embed"], help="send text as embed.\nSyntax : *say [title];[text]\nTitle is optional ")
    async def Say(self, ctx, *, txt):
        txt = str(txt)
        await ctx.message.delete()
        if ";" in txt:
            text = txt.split(";")
            sayEmbed = disnake.Embed(title = f"{text[0]}", description = f"{text[1]}", color=random.choice(colors))
            await ctx.channel.send(embed=sayEmbed, allowed_mentions= disnake.AllowedMentions(everyone = False, roles = False))
        else:
            sayEmbed = disnake.Embed(description = txt)
            await ctx.channel.send(embed=sayEmbed, allowed_mentions= disnake.AllowedMentions(everyone = False, roles = False))

def setup(client: commands.Bot):
    client.add_cog(say(client))