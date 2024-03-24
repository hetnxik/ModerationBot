import disnake, random, datetime
from disnake.ext import commands

intents = disnake.Intents.all()
colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]


class editchannelname(commands.Cog, name='editchannelname', description="Edit the name of the channel"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="Change the name of the channel")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def EditChannelName(self, ctx, *, name):
        await ctx.channel.edit(name=name)
        editEmbed = disnake.Embed(title="command `*editChannelName` => success",
                                  description=f"The current channel name changed to {name}")
        await ctx.channel.send(embed=editEmbed)

    @EditChannelName.error
    async def editChannelName_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cdEmbed = disnake.Embed(title=f"Slow it down bro!",
                                    description=f"Try again in {error.retry_after:.2f}s.\nCooldown is of 20s",
                                    colour=random.choice(colors), timestamp=datetime.datetime.utcnow())
            await ctx.send(embed=cdEmbed)
        elif isinstance(error, commands.MissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*editChannelName` => Fail",
                                       description="You dont have permissions to manage channels")
            await ctx.send(embed=errorEmbed)
        elif isinstance(error, commands.BotMissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*editChannelName` => Fail",
                                       description="The bot doesnt have permissions to manage channels")
            await ctx.send(embed=errorEmbed)
        else:
            errorEmbed = disnake.Embed(title="Command `*editChannelName` => Fail", description="Some error occurred")
            await ctx.channel.send(embed=errorEmbed)


def setup(client: commands.Bot):
    client.add_cog(editchannelname(client))
