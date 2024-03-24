import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]


class lock(commands.Cog, name='lock', description="locks the mentioned channel"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="Lock the channel.")
    @commands.has_permissions(manage_channels=True)
    async def Lock(self, ctx, channel: disnake.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        if overwrite.send_messages or overwrite.send_messages is None:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            lockEmbed = disnake.Embed(title="Command `*lock` => executed")
            lockEmbed.add_field(name="The command executed", value=f"{channel.mention} is now locked")
            await ctx.channel.send(embed=lockEmbed, delete_after=5)
            await channel.send(embed=lockEmbed)
        else:
            lockEmbed = disnake.Embed(title="Command `*lock` => unaffected")
            lockEmbed.add_field(name="The command probably didn't work because:",
                                value="1. Channel is already unlocked")
            await ctx.channel.send(embed=lockEmbed, delete_after=5)
            await channel.send(embed=lockEmbed)

    @Lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*lock` => Fail",
                                       description="You dont have permissions to manage channels")
            await ctx.send(embed=errorEmbed)
        elif isinstance(error, commands.BotMissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*lock` => Fail",
                                       description="The bot doesnt have permissions to manage channels")
            await ctx.send(embed=errorEmbed)
        else:
            errorEmbed = disnake.Embed(title="Command `*lock` => Fail", description="Some error occurred")
            await ctx.channel.send(embed=errorEmbed)


def setup(client: commands.Bot):
    client.add_cog(lock(client))
