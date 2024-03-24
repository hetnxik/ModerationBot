import random, requests
import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
colors = [0x0000EE, 0x00CD00, 0x05EDFF, 0x24D330, 0x5CACEE, 0x76EE00]

class weather(commands.Cog, name='weather', description="Gives weather of a city"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(help="get the weather of a city")
    async def Weather(self, ctx, city: str):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0c4ad4162ff8f2c9371a1492c62bf82b"
        a = requests.get(url)
        longitude = a.json()["coord"]["lon"]
        latitude = a.json()["coord"]["lat"]
        actualTemp = a.json()["main"]["temp"]
        feelTemp = a.json()["main"]["feels_like"]
        weatherEmbed = disnake.Embed(title = f"Weather => {city}", colour = random.choice(colors))
        weatherEmbed.add_field(name = "Temprature", value = f'{int(actualTemp - 273.15)}°C')
        weatherEmbed.add_field(name = "Feels like", value = f'{int(feelTemp - 273.15)}°C')
        weatherEmbed.add_field(name = "Longitude, Latitude", value = f'{longitude}, {latitude}')
        await ctx.channel.send(embed=weatherEmbed)

    @Weather.error
    async def weather_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            errorEmbed = disnake.Embed(title = "Command `*weather` => Fail", description = "Incorrect city name", color = random.choice(colors))
            await ctx.send(embed = errorEmbed)
            return error
        else:
            return error


def setup(client: commands.Bot):
    client.add_cog(weather(client))