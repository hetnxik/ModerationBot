import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]


class kick(commands.Cog, name='kick', description="Kick users"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="Kick members")
    @commands.has_permissions(kick_members=True)
    async def Kick(self, ctx, member: disnake.Member, *, reason=None):
        memberTopRole = member.top_role
        authorTopRole = ctx.message.author.top_role
        if memberTopRole < authorTopRole:
            await member.kick(reason=reason)
            kickEmbed = disnake.Embed(title=f"{member} was kicked by {ctx.author}")
            await ctx.channel.send(embed=kickEmbed)
        else:
            errorEmbed = disnake.Embed(title="Command => `*kick` => Fail",
                                       description=f"You dont have a role higher than {member.mention}.")
            await ctx.send(embed=errorEmbed)

    @Kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*kick` => Fail",
                                       description="You dont have permissions to manage members")
            await ctx.send(embed=errorEmbed)
        elif isinstance(error, commands.MemberNotFound):
            errorEmbed = disnake.Embed(title="Command => `*kick` => Fail", description="No such member found")
            await ctx.send(embed=errorEmbed)
        elif isinstance(error, commands.BotMissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*kick` => Fail",
                                       description="The bot doesnt have permissions to manage members")
            await ctx.send(embed=errorEmbed)
        else:
            errorEmbed = disnake.Embed(title="Command `*kick` => Fail", description="Some error occurred")
            await ctx.channel.send(embed=errorEmbed)
            raise error


def setup(client: commands.Bot):
    client.add_cog(kick(client))
