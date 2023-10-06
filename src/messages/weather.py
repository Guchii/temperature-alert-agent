from pydantic import Field
from uagents import Model


class WeatherRequest(Model):
    city: str = Field(
        description="City name for which weather is requested")
    min_temp: str = Field(
        description="Minimum temperature below which the user will be notified")
    max_temp: str = Field(
        description="Maximum temperature above which the user will be notified")


class WeatherResponse(Model):
    temperature: str = Field(
        description="Temperature in the city")
    above_max: bool = Field(
        description="True if the temperature is above the maximum temperature")
    below_min: bool = Field(
        description="True if the temperature is below the minimum temperature")
