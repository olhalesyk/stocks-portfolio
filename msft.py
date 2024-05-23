import functions as fn
import database_queries as db
import plotly.graph_objects as go

# Connect to the SQLite database
MSFT_avg = db.get_company_daily_mean(2)

# Convert the data into a NumPy array for better numerical performance
rows = MSFT_avg.shape[0]
time_index_MSFT = fn.time_avg(MSFT_avg)

# Calculate the moving average
MSFT_moving_avg = fn.moving_average(MSFT_avg, 12)
time_move_avg_MSFT = fn.time_avg(MSFT_avg)
time_move_avg_MSFT = time_move_avg_MSFT

# Plot the MSFT moving average
# fn.plot_single_chart(time_move_avg_MSFT, MSFT_moving_avg, 'MSFT_moving_avg', 'Plot of MSFT moving average', 'X-axis Years', 'Y-axis Price')

# # Plot the moving average
# fn.plot_double_charts(time_index_MSFT, time_move_avg_MSFT, MSFT_avg, MSFT_moving_avg, 'MSFT_avg', 'MSFT_moving_avg', 'Plot of MSFT moving average', 'X-axis Years', 'Y-axis Price')

# # Compute the cross-correlation
# cross_correlation = np.correlate(MSFT_moving_avg, MSFT_avg, mode='full')
# print(cross_correlation.shape)
