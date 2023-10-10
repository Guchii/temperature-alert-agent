# uAgent-TempAlert

## Step 1: Prerequisites

Before you begin, please ensure that you have the following prerequisites installed:

- **Python:** You will need Python installed on your system. We recommend using Python 3.8 or later.

- **Poetry:** This project uses Poetry for packaging and dependency management. If you don't have Poetry installed, you can install it following the instructions [here](https://python-poetry.org/docs/#installation).

- **Weather Data Source:** Please note that this project relies on the wttr.in service for weather data. It's a free and convenient source for weather information. However, since it's not a paid API, there may be occasional downtime or disruptions. Be aware that in such cases, the project may not be able to fetch weather data.

### Step 2: Clone the repository

```bash
git clone https://github.com/Guchii/uAgent-TempAlert.git
cd uAgent-TempAlert
```


### Step 3: Install the Dependencies

```bash
cd src
poetry install
```

### Step 4: Run the main script

To run the project and its agents:

```bash
poetry run python src/main.py
```

You'll require a Weather Agent Address in the next step.
It'll be automatically copied to your clipboard, if not, copy it from the logs

### Step 5: Run the client script

You'll be prompted to enter

1. Weather agent address that was copied to your clipboard
2. Your city name
3. Max temperature after which you want to get notified
4. Min temperature after which you want to get notified

```bash
poetry run python src/client.py
```

Once you enter all the values, a request will be sent to wttr.in from the weather agent every 10 seconds, you'll recieve a desktop notification if the current temperature goes above or below your
