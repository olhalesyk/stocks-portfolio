from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("API_KEY")

# Function to get stock data from the API and return it as a dictionary of lists of dictionaries for top gainers, top losers, and most actively traded stocks
def get_stock_data_from_api(api_key):
    api_url = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={api_key}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        
        # Check if the response contains the rate limit message
        if "Information" in data and "Thank you for using Alpha Vantage!" in data["Information"]:
            return {"error": data["Information"]}
        
        # Initialize dictionaries to store stock data
        stock_data = {
            'top_gainers': [],
            'top_losers': [],
            'most_actively_traded': []
        }
        
        # Extract data from top_gainers
        for item in data.get('top_gainers', []):
            stock_data['top_gainers'].append({
                'ticker': item['ticker'],
                'price': item['price'],
                'change_amount': item['change_amount'],
                'change_percentage': item['change_percentage'],
                'volume': item['volume']
            })
        
        # Extract data from top_losers
        for item in data.get('top_losers', []):
            stock_data['top_losers'].append({
                'ticker': item['ticker'],
                'price': item['price'],
                'change_amount': item['change_amount'],
                'change_percentage': item['change_percentage'],
                'volume': item['volume']
            })
        
        # Extract data from most_actively_traded
        for item in data.get('most_actively_traded', []):
            stock_data['most_actively_traded'].append({
                'ticker': item['ticker'],
                'price': item['price'],
                'change_amount': item['change_amount'],
                'change_percentage': item['change_percentage'],
                'volume': item['volume']
            })
        
        return stock_data
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Error occurred: {req_err}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
stock_data = get_stock_data_from_api(api_key)

# BLK MSFT ISRG Ticker data from API 
def get_ticker_data_from_api(api_key):
    symbols = ['blk', 'msft', 'isrg']
    img_urls = {
        'blk': 'static/img/logos/BLK.svg',
        'msft': 'static/img/logos/MSFT.svg',
        'isrg': 'static/img/logos/ISRG.svg'
    }
    base_url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'
    
    ticker_data = {}
    
    for symbol in symbols:
        api_url = base_url.format(symbol, api_key)
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()
            
            # Check if the response contains the rate limit message
            if "Information" in data:
                return {"error": data["Information"]}
            
            # Extract data for the given ticker
            item = data.get('Global Quote', {})
            ticker_data[symbol] = {
                'price': item.get('05. price', None),
                'change': item.get('10. change percent', None),
                'latest_trading_day': item.get('07. latest trading day', None),
                'volume': item.get('06. volume', None),
                'img_url': img_urls.get(symbol, None)
            }
        
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred for {symbol}: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred for {symbol}: {req_err}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred for {symbol}: {e}"}
    
    return ticker_data

ticker_data = get_ticker_data_from_api(api_key)
