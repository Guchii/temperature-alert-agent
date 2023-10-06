# uAgent Temperature Alert

### Step 1: Prerequisites

Before starting, you'll need the following:

- Python (3.8+ is recommended)
- Poetry (a packaging and dependency management tool for Python)

### Step 2: Install Deps

```bash
cd src
poetry intall
```

### Step 3: Run the main script

To run the project and its agents:

```bash
poetry run python src/main.py
```

You'll require a Weather Agent Address in the next step.
It'll be automatically copied to your clipboard, if not, copy it from the logs

### Step 4: Run the client script

You'll be prompted to enter

1. Weather agent address that was copied
2. Your city name
3. Max temperature after which you want to get notified
4. Min temperature

```bash
poetry run python src/client.py
```

Once you enter all the values, a request will be sent to wttr.in from the weather agent every 10 seconds, you'll recieve a desktop notification if the current temperature goes above or below your
