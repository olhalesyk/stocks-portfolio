import sqlite3
import requests
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# load_dotenv()
# api_key = os.getenv("API_KEY")

db = SQLAlchemy()

def get_company_daily_mean(company_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('tradingdata.db')
    cursor = conn.cursor()

    # Execute the query to fetch 'open' and 'close' columns
    cursor.execute('''
        SELECT low, high
        FROM stocks WHERE company_id = ?
    ''', (company_id,))

    # Fetch all rows
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert the data into a array and calculate the mean of 'open' and 'close' for each row
    data_array = np.array(data, dtype=float)
    daily_means = np.mean(data_array, axis=1)

    return daily_means

# def get_company_daily_mean(company_id):
#     # Connect to the SQLite database
#     conn = sqlite3.connect('tradingdata.db')
#     cursor = conn.cursor()

#     # Execute the query to fetch 'high' and 'low' columns
#     cursor.execute('''
#         SELECT (high + low) / 2.0 AS average
#         FROM stocks WHERE company_id = ?
#     ''', (company_id,))

#     # Fetch all rows
#     data = cursor.fetchall()

#     # Close the connection
#     conn.close()

#     # Convert the data into a NumPy array and calculate the mean of 'open' and 'close' for each row
#     data_array = np.array(data, dtype=float)

#     return data_array


# Parse JSON response
# response = requests.get('https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={api_key}}')
# data = response.json()
# print(data)
# # Extract relevant data from JSON
# time_series = data.get('Time Series (Daily)')

# # Create a connection to SQLite database
# conn = sqlite3.connect('tradingdata.db')
# print("Connected successfully")
# cursor = conn.cursor()

# # Create a table if not exists
# cursor.execute('''CREATE TABLE IF NOT EXISTS stock_prices (
#                     date TEXT PRIMARY KEY,
#                     open REAL,
#                     high REAL,
#                     low REAL,
#                     close REAL,
#                     volume INTEGER
#                 )''')
# print("Table created")

# # Insert data into the table
# for date, values in time_series.items():
#     open_price = float(values['1. open'])
#     high_price = float(values['2. high'])
#     low_price = float(values['3. low'])
#     close_price = float(values['4. close'])
#     volume = int(values['5. volume'])
#     cursor.execute('''INSERT OR REPLACE INTO stock_prices (date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?)''', (date, open_price, high_price, low_price, close_price, volume))
# # Commit changes and close connection
# print("Information added")
# conn.commit()
# conn.close()