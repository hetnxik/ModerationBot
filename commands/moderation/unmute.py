import disnake
from disnake.ext import commands


class unmute(commands.Cog, name="unmute", description="Unmute other members."):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def Unmute(self, ctx, member: disnake.Member):

        memberTopRole = member.top_role
        authorTopRole = ctx.message.author.top_role
        if memberTopRole < authorTopRole:
            for role in member.roles:
                role_list = list()
                role_list.append(role.name.lower())
            print(role_list)
            if 'muted' in role_list:
                await member.remove_roles(role)
                await ctx.send(f"unmuted {member}")
            else:
                await ctx.send(f"{member} is not muted.")
        else:
            await ctx.send(f"You dont have a role higher than {member.name}, so you cannot unmute them.")

    @Unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Bruh. You have to mention a person to mute.")
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I dont have enough permissions to execute the command.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have enough permissions to execute the command.")


def setup(client: commands.Bot):
    client.add_cog(unmute(client))
