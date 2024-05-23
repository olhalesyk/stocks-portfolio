import plotly.graph_objects as go
import functions as fn
import numpy as np
import msft
import database_queries as db
import plotly.offline as pyo

# Convert the data into a NumPy array for better numerical performance
apple_avg = db.get_company_daily_mean(1)

# Convert the data into a NumPy array for better numerical performance

rows = apple_avg.shape[0]
time_index = fn.time_avg(apple_avg)

# Calculate the moving average
apple_moving_avg = fn.moving_average(apple_avg, 12)
time_move_avg_apple = fn.time_avg(apple_moving_avg)

# Define the window size for the covariance
window_size_cov = 12
sliding_cov = fn.sliding_covariance(apple_moving_avg, msft.MSFT_moving_avg, window_size_cov)
# time_cov = np.arange(len(sliding_cov) + 1, -1, -1)
time_cov = fn.time_avg(sliding_cov)-0.125

# Return Pearson correlation coefficients
sliding_regr_coef = fn.sliding_regr_coef(apple_moving_avg, msft.MSFT_moving_avg, window_size_cov)
fn.plot_single_chart(time_cov, sliding_regr_coef, 'Pearson correlation coefficient', 'Pearson correlation coefficient of Apple and MSFT', 'Year', 'Correlation coefficient (r)')

fn.plot_double_charts(time_index, msft.time_index_MSFT, apple_avg,  msft.MSFT_avg, 'Apple_avg', 'MSFT_avg', 'Stock price: Apple vs MSFT', 'Year', 'Stock Price')

fn.plot_double_charts(time_move_avg_apple, msft.time_move_avg_MSFT, apple_moving_avg, msft.MSFT_moving_avg, 'Apple_moving_avg', 'MSFT_moving_avg', 'Moving average: Apple vs MSFT', 'Year', 'Stock Price')

#Creating the figure of average prices and moving average
fn.plot_single_chart(time_cov, sliding_cov, 'Apple and MSFT', 'Covariance of Apple and MSFT', 'Year', 'Covariance')
