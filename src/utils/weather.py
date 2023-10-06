import requests
from bs4 import BeautifulSoup


def fetch_temperature(city: str):
    try:
        # Create the URL for the city on wttr.in
        url = f"https://wttr.in/{city.replace(' ', '+')}?format=%t"

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the temperature data
            temperature = soup.get_text().strip()

            return temperature
        else:
            return f"Failed to fetch temperature for {city}. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    city_name = "Delhi"
    temperature_info = fetch_temperature(city_name)
    print(f"Temperature in {city_name}: {temperature_info}")
