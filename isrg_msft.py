import msft
import numpy as np
import functions as fn
import database_queries as db
from flask import Flask, render_template, send_file

# Convert the data into a NumPy array for better numerical performance
isrg_avg = db.get_company_daily_mean(6)

# Convert the data into a NumPy array for better numerical performance

rows = isrg_avg.shape[0]
time_index = fn.time_avg(isrg_avg)

# Calculate the moving average
isrg_moving_avg = fn.moving_average(isrg_avg, 12)
time_move_avg_isrg = fn.time_avg(isrg_moving_avg)

# Define the window size for the covariance
window_size_cov = 12
sliding_cov = fn.sliding_covariance(isrg_moving_avg, msft.MSFT_moving_avg, window_size_cov)
# time_cov = np.arange(len(sliding_cov) + 1, -1, -1)
time_cov = fn.time_avg(sliding_cov)-0.125

# Plot the ISRG and MSFT average
fig_isrgMsftStocks = fn.plot_double_charts(time_index, msft.time_index_MSFT, isrg_avg,  msft.MSFT_avg, 'ISRG average', 'MSFT average', 'Stock price: ISRG and MSFT', 'Year', 'Stock Price')
# Save the plot HTML to a file
with open('application/templates/plot_isrgMsftStocks.html', 'w') as f:
    f.write(fig_isrgMsftStocks)

# Plot the ISRG and MSFT moving average
fig_isrgMsftMovingAverage = fn.plot_double_charts(time_move_avg_isrg, msft.time_move_avg_MSFT, isrg_moving_avg, msft.MSFT_moving_avg, 'ISRG moving average', 'MSFT moving average', 'Moving average: ISRG and MSFT', 'Year', 'Stock Price')
# Save the plot HTML to a file
with open('application/templates/plot_isrgMsftMovingAverage.html', 'w') as f:
    f.write(fig_isrgMsftMovingAverage)

# Return Pearson correlation coefficients
sliding_regr_coef = fn.sliding_regr_coef(isrg_moving_avg, msft.MSFT_moving_avg, window_size_cov)
fig_isrgMsftSlidingCorrelation = fn.plot_single_chart(time_cov, sliding_regr_coef, 'Pearson correlation coefficient', 'Pearson correlation coefficient of ISRG and MSFT', 'Year', 'Correlation coefficient (r)')
# Save the plot HTML to a file
with open('application/templates/plot_isrgMsftSlidingCorrelation.html', 'w') as f:
    f.write(fig_isrgMsftSlidingCorrelation)

#Creating the figure of average prices and moving average
fig_isrgMsftCovariance = fn.plot_single_chart(time_cov, sliding_cov, 'ISRG and MSFT', 'Covariance of ISRG and MSFT', 'Year', 'Covariance')
sum_of_sliding_regr_coef = np.sum(sliding_regr_coef)/len(sliding_regr_coef)

# Save the plot HTML to a file
with open('application/templates/plot_isrgMsftCovariance.html', 'w') as f:
    f.write(fig_isrgMsftCovariance)


