import disnake
from disnake.ext import commands


class mute(commands.Cog, name="mute", description="Mute other members."):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def Mute(self, ctx, member: disnake.Member):
        memberTopRole = member.top_role
        authorTopRole = ctx.message.author.top_role
        if memberTopRole < authorTopRole:
            guild = ctx.guild
            for role in guild.roles:
                if role.name.lower() != 'muted':
                    perms = disnake.Permissions(send_messages=False, speak=False)
                    role = await guild.create_role(name="Muted", permissions=perms)
                    await member.add_roles(role)
                    await ctx.send(f"Muted {member}")
                    break
                elif role.name.lower() == 'muted':
                    await member.add_roles(role)
                    await ctx.send(f"Muted {member}")
                    break
        else:
            await ctx.send(f"You dont have a role higher than {member.name}, so you cannot mute them.")

    @Mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Bruh. You have to mention a person to mute.")
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I dont have enough permissions to execute the command.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have enough permissions to execute the command.")


def setup(client: commands.Bot):
    client.add_cog(mute(client))
