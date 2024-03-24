import asyncio
import disnake, requests
from disnake.ext import commands

async def score(ctx, link):
    pass

class Crickbuzz(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def crickbuzz(self, ctx, link):
        # await score(ctx, link)
        info = requests.get(f'https://cricket-api.vercel.app/cri.php?url={link}').json()
        msg = await ctx.send(f"{link}")
        while True:
            if link == 'false':
                await ctx.send('false')
                break
            else:
                if info ['success'] != 'true':
                    info = info ['livescore']
                    embed = disnake.Embed(
                        title = info ['title'],
                        description = info ['current'],
                        color = disnake.Color.dark_orange()
                    )
                    embed.add_field(
                        name = f"Batsman : {info ['batsman']}",
                        value = f"Runs : {info ['batsmanrun']}\nBalls faced : {info ['ballsfaced']}",
                        inline = False
                    )
                    embed.add_field(
                        name = f"Bowler : {info ['bowler']}",
                        value = f"Wickets : {info ['bowlewickets']}\nOvers : {info ['bowlerover']}",
                        inline = False
                    )
                    embed.add_field(
                        name = f"runrate : {info ['runrate']}",
                        value = f"last wicket : {info ['lastwicket']}\nrecent balls : {info ['recentballs']}",
                        inline = False
                    )
                    await msg.edit(embed = embed)
                    await asyncio.sleep(10)
                else:
                    await msg.edit('Some error occured.')
                    break

def setup(client: commands.Bot):
    client.add_cog(Crickbuzz(client))