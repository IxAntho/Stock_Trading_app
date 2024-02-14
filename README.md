# Tesla Stock Analyzer & News Notifier

This Python script analyzes the stock performance of Tesla and sends you a message containing the percentage change along with the latest news headlines related to the company.

## Overview

This project utilizes various APIs to fetch stock data and news articles related to Tesla. It calculates the percentage change in Tesla's stock price from the previous day and sends it along with three latest news headlines via SMS using the Twilio API.

## Technologies Used

This project leverages the following technologies:

- **Python**: The primary programming language used for scripting and data manipulation.
- **Requests Library**: Used for making HTTP requests to fetch data from APIs.
- **Twilio API**: Integrated to send SMS messages containing stock information and news updates.
- **Alpha Vantage API**: Utilized to retrieve real-time stock data for Tesla.
- **News API**: Employed to fetch the latest news articles related to Tesla.


## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `requests` library: For making HTTP requests
- `twilio` library: For sending SMS messages
- Alpha Vantage API Key: To fetch stock data
- News API Key: To fetch news articles
- Twilio Account SID and Authentication Token

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/tesla-stock-analyzer.git
   cd tesla-stock-analyzer
   
   pip install -r requirements.txt

Open the `main.py` file and update the following variables with your API keys and phone numbers:
- `STOCK_API_KEY`
- `NEWS_API_KEY`
- `ACCOUNT_SID`
- `AUTH_TOKEN`

Replace `"your account SID"` and `"Your authentication token"` with your actual Twilio account SID and authentication token.
Replace `["Your phone number"]` with your Twilio phone number from which the messages will be sent.
Replace `["Another phone number"]` with the recipient's phone number where you want to receive the messages.

## Usage

Simply run the Python script:

    python main.py

The script will fetch the percentage change in Tesla's stock price and the latest news articles. If today is not a weekend, it will send this information via SMS using Twilio.

## Notes

- The script will only execute on weekdays (Monday to Friday). If run on a weekend, it will not send any messages.
- Ensure that your Alpha Vantage and News API keys are valid and have sufficient quota for making requests.

## Disclaimer

This script is for educational purposes only. Always do your own research before making any financial decisions based on the information provided by this script.

## Contact

- Email: [isabar735@icloud.com]
- inkedIn: [https://www.linkedin.com/in/anthony-barrios-697a342a3/]