import disnake, random
from disnake.ext import commands

class invite(commands.Cog, name='invite', description="invite link for the bot"):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help = "Get the invite link of the bot")
    async def Invite(self, ctx):
        inviteEmbed = disnake.Embed(
            title = "Invite this Bot to your server",
            color = disnake.Colour.random(),
            description =f'[Invite To Server](https://discord.com/oauth2/authorize?client_id={self.client.user.id}&permissions=8589934591&scope=bot%20applications.commands) 👈 Click to invite this bot to other servers',
        )
        await ctx.send(embed = inviteEmbed)

def setup(client: commands.Bot):
    client.add_cog(invite(client))