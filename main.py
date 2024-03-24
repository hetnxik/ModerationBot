import disnake, os, random, asyncio
from disnake.ext import commands

intents = disnake.Intents.all()
client = commands.Bot(command_prefix="*",
                      intents=intents,
                      case_insensitive=True,
                      owner_id=807655087643557919,
                      )

me = client.get_user(807655087643557919)


async def change_presence():
    await client.wait_until_ready()
    while not client.is_closed():
        await client.change_presence(
            status=disnake.Status.dnd,
            activity=disnake.Activity(
                type=disnake.ActivityType.listening,
                name=f"*help in {len(client.guilds)} servers"
            )
        )

        await asyncio.sleep(30)
        cultured_artists = ["Corpse", "Prznt", "Eminem", "Weeknd", "Pop Smoke", "Drake", "2Scratch", "Logic", "NF",
                            "Post Malone", "Neffex", "XXXTENTATCION"]
        await client.change_presence(
            status=disnake.Status.idle,
            activity=disnake.Activity(
                type=disnake.ActivityType.listening,
                name=f"{random.choice(cultured_artists)} on Spotify"
            )
        )
        await asyncio.sleep(30)


colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]


@client.event
async def on_ready():
    print("ready")
    print(os.getenv("OwnerId"))


class Dropdown(disnake.ui.Select):
    def __init__(self):

        options = list()

        for category in os.listdir('./commands'):
            if category != '.DS_Store' and category != 'Owner' and category != 'Listeners':
                options.append(disnake.SelectOption(label=f"{category}",
                                                    description=f"view all the commands in {category} category."))

            super().__init__(placeholder='Choose A category to view other commands', min_values=1, max_values=1,
                             options=options)

    async def callback(self, interaction: disnake.MessageInteraction):
        cmdList = list()

        category_help_embed = disnake.Embed(title=f"Detailed stats of {self.values[0]}", color=disnake.Colour.random())

        if self.values[0] != 'Listeners':
            for cmd in os.listdir(f"./commands/{self.values[0]}"):
                if cmd.endswith('.py') and not cmd.startswith('_') and not cmd.startswith(
                        '.') and cmd != 'top5hq.py' and cmd != 'sabregeh.py':
                    cog = client.get_cog(name=cmd[:-3].lower())
                    cmdList.append(cmd[:-3])
                    if cog is not None:
                        command = cog.get_commands()[0]
                        aliases = command.aliases
                        if len(aliases) > 0:
                            alias_str = "`" + f"`, `".join(aliases) + "`"
                        else:
                            alias_str = "`N/A`"
                        category_help_embed.add_field(name=cmd[:-3],
                                                      value=f"⇒ {cog.description}\n**Aliases**: {alias_str}",
                                                      inline=True)
        await interaction.response.send_message(embed=category_help_embed, ephemeral=True)


class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=30)
        self.add_item(Dropdown())


class MyHelp(commands.HelpCommand):
    async def send_command_help(self, command):
        embed = disnake.Embed(
            title=command.name,
            color=disnake.Color.random()
        )
        embed.add_field(
            name="Description",
            value=command.help
        )

        alias = command.aliases
        if alias:
            embed.add_field(
                name="Aliases",
                value=", ".join(alias),
                inline=False
            )

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_bot_help(self, mapping):
        channel = self.get_destination()

        helpEmbed = disnake.Embed(
            title="Help command",
            description="Choose a category from the drop-down menu to get the list of all commands.",
            color=disnake.Color.random()
        )
        view = DropdownView()
        msg = await channel.send(embed=helpEmbed, view=view)
        if await view.wait():
            for options in view.children:
                options.disabled = True
            await msg.edit(view=view)

    async def send_cog_help(self, cog):
        if cog.description == 'All the music commands':
            channel = self.get_destination()
            cogEmbed = disnake.Embed(
                title=cog.description,
                description=f"The commands in {cog.description}",
                color=disnake.Color.random()
            )

            for i in range(0, len(cog.get_commands())):
                cogEmbed.add_field(
                    name=f"{cog.get_commands()[i]}",
                    value=f"type `*help {cog.get_commands()[i]}` for more info",
                    inline=False
                )

            await channel.send(embed=cogEmbed)


client.help_command = MyHelp()

print(
    """
 █████╗   █████╗   ██████╗   ██████╗
██╔══██╗ ██╔══██╗ ██╔════╝  ██╔════╝
██║  ╚═╝ ██║  ██║ ██║  ██╗  ╚█████╗ 
██║  ██╗ ██║  ██║ ██║  ╚██╗  ╚═══██╗
╚█████╔╝ ╚█████╔╝ ╚██████╔╝ ██████╔╝
 ╚════╝   ╚════╝   ╚═════╝  ╚═════╝ 
 ------------------------------------
 """
)

for folder in os.listdir('./commands'):
    if folder != '.DS_Store' and folder != 'Economy':  # and folder != 'vc-interactions':
        print(folder)
        for file in os.listdir(f'./commands/{folder}'):
            if file.endswith('.py') and not file.startswith('_') and not file.startswith('.'):
                client.load_extension(f'commands.{folder}.{file[:-3]}')
                print(f'Loaded the category: {file}')

print("=================================")

client.loop.create_task(change_presence())
client.run("TOKEN")
