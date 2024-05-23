import yfinance as yf
import pandas as pd
import numpy as np
from scipy.special import comb
import plotly.graph_objects as go
import itertools
from itertools import combinations
import plotly.io as pio
import functions as fn

# List of stock symbols
stock_symbols = ["AAPL", "JNJ", "JPM", "PG", "XOM", "NEE", "VZ", "CAT", "HD", "MSFT"]

# Rate range for the historical data
start_date = "2014-01-01"
end_date = "2024-01-01"

# Get historical data
stock_data = {}
for symbol in stock_symbols:
    stock_data[symbol] = yf.download(symbol, start=start_date, end=end_date)["Close"]

# Merge stocks into a single DataFrame
df = pd.DataFrame(stock_data)

# Correlation matrix
correlation_matrix = df.corr()

# Combination of 4 companies with the minimum average correlation
def find_min_correlation_stocks(correlation_matrix, num_stocks):
    possible_combinations = list(itertools.combinations(correlation_matrix.columns, num_stocks))
    min_avg_corr = float('inf')
    best_combination = []

    # Iterate through all combinations
    for comb in possible_combinations:
        # Calculate the sum of the current combination
        sub_matrix = correlation_matrix.loc[comb, comb]
        current_sum = (sub_matrix.values[np.triu_indices(num_stocks, k=1)].mean())
        # current_sum = np.sum(correlation_matrix.ravel()[list(comb)])
        
        # Check if the current sum is less than the minimal sum found so far
        if current_sum < min_avg_corr:
            min_avg_corr = current_sum
            best_combination = comb

    return best_combination

best_stocks = find_min_correlation_stocks(correlation_matrix, 4)
print("Best stocks for minimum correlation:", best_stocks)
filtered_correlation_matrix = correlation_matrix.loc[best_stocks, best_stocks]

fig_correlation_matrix = fn.plot_correlation_matrix(filtered_correlation_matrix.values,filtered_correlation_matrix.columns,filtered_correlation_matrix.columns,'Correlation Matrix of Selected Stocks')

# Save the plot HTML to a file
with open('application/templates/plot_correlation_matrix.html', 'w') as f:
    f.write(fig_correlation_matrix)

