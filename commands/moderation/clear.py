import disnake, random, datetime
from disnake.ext import commands

colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]


class clear(commands.Cog, name='clear', description="Purge messages"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(aliases=["purge", "delete"], help="Purge multiple messages")
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def Clear(self, ctx, amt: int = 1):
        await ctx.channel.purge(limit=amt + 1)
        purge = disnake.Embed(title="Command `*purge` => Success", colour=random.choice(colors))
        purge.add_field(name="The command executed", value=f"Purged `{amt}` message(s)")
        await ctx.channel.send(embed=purge, delete_after=5)

    @Clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cdEmbed = disnake.Embed(title=f"Slow it down bro!",
                                    description=f"Try again in {error.retry_after:.2f}s.\nCooldown is of 4s",
                                    colour=random.choice(colors), timestamp=datetime.datetime.utcnow())
            await ctx.send(embed=cdEmbed)
        elif isinstance(error, commands.MissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*clear` => Fail",
                                       description="You dont have permissions to delete messages")
            await ctx.send(embed=errorEmbed)
        elif isinstance(error, commands.BotMissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*clear` => Fail",
                                       description="The bot doesnt have permissions to delete messages")
            await ctx.send(embed=errorEmbed)
        else:
            errorEmbed = disnake.Embed(title="Command `*clear` => Fail", description="Some error occurred")
            await ctx.channel.send(embed=errorEmbed)


def setup(client: commands.Bot):
    client.add_cog(clear(client))
