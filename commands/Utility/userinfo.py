import random
import disnake
from disnake.ext import commands

colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]

class userinfo(commands.Cog, name='userinfo', description="Get info of the mentioned user"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(aliases = ["ui"], help = "Show info about a Member")
    async def Userinfo(self, ctx, user: disnake.Member = None):
        if user is None:
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = disnake.Embed(color = random.choice(colors), description = user.mention)
        embed.set_author(name = str(user), icon_url = user.avatar.url)
        embed.set_thumbnail(url = user.avatar.url)
        embed.add_field(name = "Joined", value = user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key = lambda m : m.joined_at)
        embed.add_field(name = "Join position", value = str(members.index(user) + 1))
        embed.add_field(name = "Registered", value = user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles] [1 :])
            embed.add_field(name = "Roles [{}]".format(len(user.roles) - 1), value = role_string, inline = False)

        embed.set_footer(text = 'ID: ' + str(user.id))
        await ctx.send(embed = embed)

    @Userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            uiError = disnake.Embed(title = "Command userinfo => Fail", description = "Mentioned user not found.")
            await ctx.channel.send(embed=uiError)


def setup(client: commands.Bot):
    client.add_cog(userinfo(client))