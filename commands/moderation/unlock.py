import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]


class unlock(commands.Cog, name='unlock', description="Unlocks a channel"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="lock the channel")
    @commands.has_permissions(manage_channels=True)
    async def Unlock(self, ctx, channel: disnake.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        if overwrite.send_messages:
            modem = disnake.Embed(title="Command `unlock` => unaffected")
            modem.add_field(name="The command probably didn't work because:", value="1. Channel is already unlocked")
            await ctx.channel.send(embed=modem, delete_after=5)
            await channel.send(embed=modem, delete_after=5)
        else:
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            modem = disnake.Embed(title="Command `unlock` => Success")
            modem.add_field(name="The command executed", value="The channel is now unlocked")
            await ctx.channel.send(embed=modem, delete_after=5)
            await channel.send(embed=modem, delete_after=5)

    @Unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*unlock` => Fail",
                                       description="You dont have permissions to manage channels")
            await ctx.send(embed=errorEmbed)
        elif isinstance(error, commands.BotMissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*unlock` => Fail",
                                       description="The bot doesnt have permissions to manage channels")
            await ctx.send(embed=errorEmbed)
        else:
            errorEmbed = disnake.Embed(title="Command `*unlock` => Fail", description="Some error occurred")
            await ctx.channel.send(embed=errorEmbed)


def setup(client: commands.Bot):
    client.add_cog(unlock(client))
