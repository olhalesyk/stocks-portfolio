from flask import Flask, render_template, url_for
from application import app
import top_gainers
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

@app.route('/')
def index():
    stock_data = top_gainers.get_stock_data_from_api(api_key)
    if 'error' in stock_data:
        message = stock_data['error']
        return render_template('index.html', title='Home', message=message)
    else:
        return render_template('index.html', title='Home', stock_data=stock_data)

@app.route('/companies-comparing')
def companies_comparing():
    ticker_data = top_gainers.get_ticker_data_from_api(api_key)
    
    if 'error' in ticker_data:
        message = ticker_data['error']
        return render_template('companies-comparing.html', title='Companies comparing', message=message)
    else:
        return render_template('companies-comparing.html', title='Companies comparing', ticker_data=ticker_data)
    
@app.route('/portfolio')
def portfolio():    
    return render_template('portfolio_analysis.html', title='Portfolio analysis')

@app.route('/plot_isrgMsftStocks')
def plot_isrgMsftStocks():
    return render_template('plot_isrgMsftStocks.html')

@app.route('/plot_isrgMsftMovingAverage')
def plot_isrgMsftMovingAverage():
    return render_template('plot_isrgMsftMovingAverage.html')

@app.route('/plot_isrgMsftSlidingCorrelation')
def plot_isrgMsftSlidingCorrelation():
    return render_template('plot_isrgMsftSlidingCorrelation.html')

@app.route('/plot_isrgMsftCovariance')
def plot_isrgMsftCovariance():
    return render_template('plot_isrgMsftCovariance.html')

@app.route('/plot_blkMsftStocks')
def plot_blkMsftStocks():
    return render_template('plot_blkMsftStocks.html')

@app.route('/plot_blkMsftMovingAverage')
def plot_blkMsftMovingAverage():
    return render_template('plot_blkMsftMovingAverage.html')

@app.route('/plot_blkMsftSlidingCorrelation')
def plot_blkMsftSlidingCorrelation():
    return render_template('plot_blkMsftSlidingCorrelation.html')

@app.route('/plot_blkMsftCovariance')
def plot_blkMsftCovariance():
    return render_template('plot_blkMsftCovariance.html')