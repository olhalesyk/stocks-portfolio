import plotly.graph_objects as go
import functions as fn
import msft
import database_queries as db

# Convert the data into a NumPy array for better numerical performance
blk_avg = db.get_company_daily_mean(5)
print(blk_avg)
# Convert the data into a NumPy array for better numerical performance

rows = blk_avg.shape[0]
time_index = fn.time_avg(blk_avg)

# Calculate the moving average
blk_moving_avg = fn.moving_average(blk_avg, 12)
time_move_avg_blk = fn.time_avg(blk_moving_avg)

# Define the window size for the covariance
window_size_cov = 12
sliding_cov = fn.sliding_covariance(blk_moving_avg, msft.MSFT_moving_avg, window_size_cov)

time_cov = fn.time_avg(sliding_cov)-0.125

# Plot the BLK and MSFT average
fig_blkMsftStocks = fn.plot_double_charts(time_index, msft.time_index_MSFT, blk_avg,  msft.MSFT_avg, 'BLK average', 'MSFT average', 'Stock price: BLK and MSFT', 'Year', 'Stock Price')
# Save the plot HTML to a file
with open('application/templates/plot_blkMsftStocks.html', 'w') as f:
    f.write(fig_blkMsftStocks)

# Plot the blk and MSFT moving average
fig_blkMsftMovingAverage = fn.plot_double_charts(time_move_avg_blk, msft.time_move_avg_MSFT, blk_moving_avg, msft.MSFT_moving_avg, 'BLK moving average', 'MSFT moving average', 'Moving average: BLK and MSFT', 'Year', 'Stock Price')
# Save the plot HTML to a file
with open('application/templates/plot_blkMsftMovingAverage.html', 'w') as f:
    f.write(fig_blkMsftMovingAverage)

#Creating the Covariance
fig_blkMsftCovariance = fn.plot_single_chart(time_cov, sliding_cov, 'BLK and MSFT', 'Covariance of BLK and MSFT', 'Year', 'Covariance')
# Save the plot HTML to a file
with open('application/templates/plot_blkMsftCovariance.html', 'w') as f:
    f.write(fig_blkMsftCovariance)

# Return Pearson correlation coefficients
sliding_regr_coef = fn.sliding_regr_coef(blk_moving_avg, msft.MSFT_moving_avg, window_size_cov)
fig_blkMsftSlidingCorrelation = fn.plot_single_chart(time_cov, sliding_regr_coef, 'Pearson correlation coefficient', 'Pearson correlation coefficient of BLK and MSFT', 'Year', 'Correlation coefficient (r)')
# Save the plot HTML to a file
with open('application/templates/plot_blkMsftSlidingCorrelation.html', 'w') as f:
    f.write(fig_blkMsftSlidingCorrelation)