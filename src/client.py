from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from plyer import notification
from messages.weather import WeatherResponse, WeatherRequest
import os

WEATHER_CLIENT_SEED = os.getenv(
    "WEATHER_CLIENT_SEED", "ijpoidugapsidu1231231023jdklajsd")

weather_client = Agent(
    name="weather_client",
    seed=WEATHER_CLIENT_SEED,
    endpoint="http://0.0.0.0:8080/submit",
    port=8080
)

fund_agent_if_low(weather_client.wallet.address())

# Update this Object with your city name and temperature range
weather_request = WeatherRequest(
    city="New Delhi", min_temp=7, max_temp=42)


@weather_client.on_event("startup")
async def startup(ctx: Context):
    weather_agent_address = input("Enter the weather agent address: ")
    city = input("Enter your city name (default is New Delhi): ")
    if city:
        weather_request.city = city.strip()
    min_temp = input("Minimum temperature (default is 7): ")
    if min_temp:
        weather_request.min_temp = float(min_temp)
    max_temp = input("Maxiumum temperature (default is 42): ")
    if max_temp:
        weather_request.max_temp = float(max_temp)
    await ctx.send(weather_agent_address, weather_request)


@weather_client.on_message(model=WeatherResponse)
async def receive_message(ctx: Context, _: str, msg: WeatherResponse):
    ctx.logger.info(f"Temperature: {msg.temperature}C")
    if msg.below_min:
        ctx.logger.warning("Temperature is below minimum!")
        notification.notify(title="TEMPERATURE ALERT!!",
                            timeout=2,
                            message="Temperature is below minimum!")
    elif msg.above_max:
        ctx.logger.warning("Temperature is above maximum!")
        notification.notify(title="TEMPERATURE ALERT!!",
                            timeout=2,
                            message="Temperature is below minimum!")


if __name__ == "__main__":
    weather_client.run()
