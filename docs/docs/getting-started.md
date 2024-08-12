Getting started
===============

## Setup

### Stathead Data
- Create an account with [stathead.com](https://stathead.com/basketball/)
- Purchase a 'Stathead Basketball Monthly' plan for $9.00/month with a one month free trial
- Add stathead username and password to .env file as in the format below:
  ```
  STATHEAD_USERNAME=your_username
  STATHEAD_PASSWORD=your_password
  ```
- Download [chromedriver](https://googlechromelabs.github.io/chrome-for-testing/) and make sure it is added to path

### Kaggle Data
- Create an account with [kaggle.com](https://kaggle.com) if you do not already have one
- In settings create an API token
- Add the username and API key to .env file as in the format below:
  ```
  KAGGLE_USERNAME=your_username
  KAGGLE_KEY=your_api_key
  ```

### Manual Collection
- International player statistics and a list of draft prospects must be collected manually as described in the release notes

## Build
1. Run build.py
2. Run college_player_comps.ipynb adding manual data where necessary