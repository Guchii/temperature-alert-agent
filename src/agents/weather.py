from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

from messages.weather import WeatherRequest, WeatherResponse
from utils.weather import fetch_temperature

import os

WEATHER_AGENT_SEED = os.getenv(
    "WEATHER_AGENT_SEED", "12312fadljhfalksdhfierwer3123123"
)

weather_agent = Agent(
    name="weather_agent",
    seed=WEATHER_AGENT_SEED,
    endpoint=["http://0.0.0.0:8000/submit"]
)

fund_agent_if_low(weather_agent.wallet.address())


@weather_agent.on_message(model=WeatherRequest)
async def receive_message(ctx: Context, sender: str, msg: WeatherRequest):
    ctx.storage.set("city", msg.city)
    ctx.storage.set("min_temp", float(msg.min_temp))
    ctx.storage.set("max_temp", float(msg.max_temp))
    ctx.storage.set("sender", sender)


@weather_agent.on_interval(period=10.0)
async def get_weather(ctx: Context):
    ctx.logger.info("Getting weather...")
    if not ctx.storage.get("city"):
        ctx.logger.info("No city set!")
        return

    city = ctx.storage.get("city")
    min_temp, max_temp = ctx.storage.get(
        "min_temp"), ctx.storage.get("max_temp")

    temperature = float(fetch_temperature(city)[:-2])

    below_min, above_max = False, False

    print(f"Temperature: {temperature} C")

    if temperature < min_temp:
        below_min = True
    elif temperature > max_temp:
        above_max = True
    else:
        ctx.logger.info("Temperature is normal!")
        return

    weather_response = WeatherResponse(below_min=below_min, above_max=above_max,
                                       temperature=temperature)

    await ctx.send(ctx.storage.get("sender"), weather_response)
