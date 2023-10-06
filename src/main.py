from agents.weather import weather_agent
import clipboard

if __name__ == "__main__":
    print(f"Starting {weather_agent.name}... 🚀")
    print(f"Agent address: {weather_agent.address}")
    clipboard.copy(weather_agent.address)
    print("Copied agent address to clipboard!")
    weather_agent.run()
