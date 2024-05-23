import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

def covariance(x, y):
    return np.cov(x, y, bias=True)[0, 1]

def sliding_covariance(arr1, arr2, window_size):
    covariances = []
    for i in range(len(arr1) - window_size + 1):
        window_x = arr1[i:i + window_size]
        window_y = arr2[i:i + window_size]
        cov = covariance(window_x, window_y)
        covariances.append(cov)
    return np.array(covariances)

def sliding_regr_coef(arr1, arr2, window_size):
    regr_coefs = []
    for i in range(len(arr1) - window_size + 1):
        window_x = arr1[i:i + window_size]
        window_y = arr2[i:i + window_size]
        # regr_coef = np.polyfit(window_x, window_y, 1)[0]
        regr_coef = np.corrcoef(window_x, window_y, 1)[0, 1]
        regr_coefs.append(regr_coef)
    return np.array(regr_coefs)

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

def time_avg(data):
    time_avg = np.array([0 for i in range(len(data))], dtype=float)
    for i in range(len(data)):
        time_avg[i] = 2024 + 0.4 - i/52
    return time_avg

def plot_double_charts(time_index1, time_index2, avg1, avg2, name1, name2, title, xaxis_title, yaxis_title):
    fig = go.Figure()
    # Adding the first trace
    fig.add_trace(go.Scatter(
        x=time_index1, 
        y=avg1,
        mode='lines+markers',
        marker=dict(
                color="darkturquoise",
           ),
        fill='tonexty',
        name=name1
    ))

    # Adding the second trace
    fig.add_trace(go.Scatter(
        x=time_index2, 
        y=avg2, 
        mode='lines+markers',
        marker=dict(
                color="lightcoral",
           ),
        fill='tozeroy',
        name=name2
    ))

    # Adding title and labels
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title
    )
    # Display the traces plot
    return pio.to_html(fig, full_html=False)

# Plot a single chart
def plot_single_chart(time_index, data, name, title, xaxis_title, yaxis_title):
    fig = go.Figure()
    # Adding the trace
    fig.add_trace(go.Scatter(
        x=time_index, 
        y=data, 
        mode='lines+markers',
        marker=dict(
                color="dodgerblue",
           ),
        name=name
    ))

    # Adding title and labels
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title
    )
    # Display the plot
    # fig.show()
    return pio.to_html(fig, full_html=False)

def plot_correlation_matrix(values,columns_x,columns_y,title):
    # Plot the correlation matrix
    fig = go.Figure(data=go.Heatmap(
        z=values,
        x=columns_x,
        y=columns_y,
        colorscale='bupu',
        zmin=-1, zmax=1,
        colorbar=dict(title="Correlation")
    ))
    fig.update_layout(
        title=title,
        xaxis_nticks=36
    )
    return pio.to_html(fig, full_html=False)

