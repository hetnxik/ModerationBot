import disnake, requests
from disnake.ext import commands

colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]
afkdict = {}


class afk(commands.Cog, name='afk', description="go afk!"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def Afk(self, ctx, *, afkmsg=""):
        global afkdict
        if ctx.message.author in afkdict:
            afkdict.pop(ctx.message.author)
            try:
                if ctx.message.author.nick.startswith('[AFK] '):
                    await ctx.message.author.edit(nick=f"{ctx.message.author.nick[5:]}")
            except Exception as e:
                pass
            await ctx.channel.send('you are no longer afk')
        else:
            if afkmsg == "":
                afkdict[ctx.message.author] = [afkmsg, ctx.message.author.nick]

                try:
                    await ctx.message.author.edit(nick=f"[AFK] {ctx.message.author.nick}")
                except:
                    pass
                await ctx.channel.send(f"You are now afk.")

            else:
                afkdict[ctx.message.author] = [afkmsg, ctx.message.author.nick]
                await ctx.channel.send(f"You are now afk with excuse - {afkmsg}")
                try:
                    await ctx.message.author.edit(nick=f"[AFK] {ctx.message.author.nick}")
                except:
                    pass

    @commands.Cog.listener()
    async def on_message(self, message):
        global colors
        global afkdict

        if message.author in afkdict:
            if not message.content.startswith('*afk'):
                afkdict.pop(message.author)
                try:
                    if message.author.nick.startswith('[AFK] '):
                        await message.author.edit(nick=f"{message.author.nick[5:]}")
                except:
                    pass
                if message.author.nick == 'None':
                    mention = message.author.name
                else:
                    mention = message.author.nick
                await message.channel.send(f"Welcome back `{mention}`. Removed your afk")

        for member in message.mentions:
            if member != message.author:

                if member in afkdict:
                    afkmsg = afkdict[member][0]

                    if afkmsg == "":
                        await message.reply(f"`{member.nick}` is afk.")

                    else:
                        await message.channel.send(f"`{member.nick}` is afk - {afkmsg}")


def setup(client: commands.Bot):
    client.add_cog(afk(client))
