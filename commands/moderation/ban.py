import disnake, random, datetime
from disnake.ext import commands

intents = disnake.Intents.all()
colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]


class ban(commands.Cog, name='ban', description="Ban users"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="Ban members")
    @commands.has_permissions(ban_members=True)
    async def Ban(self, ctx, member: disnake.Member, *, reason=None):
        memberTopRole = member.top_role
        authorTopRole = ctx.message.author.top_role
        if memberTopRole < authorTopRole:
            await member.ban(reason=reason)
            banEmbed = disnake.Embed(title=f"{member} was banned by {ctx.author}")
            await ctx.channel.send(embed=banEmbed)

        else:
            errorEmbed = disnake.Embed(title="Command => `ban` => Fail",
                                       description=f"You dont have a role higher than {member.mention}.")
            await ctx.send(embed=errorEmbed)

    @Ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `*ban` => Fail",
                                       description="You dont have permissions to manage members")
            await ctx.send(embed=errorEmbed)

        elif isinstance(error, commands.MemberNotFound):
            errorEmbed = disnake.Embed(title="Command => `*ban` => Fail", description="No such member found")
            await ctx.send(embed=errorEmbed)
        elif isinstance(error, commands.BotMissingPermissions):
            errorEmbed = disnake.Embed(title="Command => `**ban` => Fail",
                                       description="The bot doesnt have permissions to manage members")
            await ctx.send(embed=errorEmbed)
        else:
            errorEmbed = disnake.Embed(title="Command `*ban` => Fail", description="Some error occurred")
            await ctx.channel.send(embed=errorEmbed)


def setup(client: commands.Bot):
    client.add_cog(ban(client))
