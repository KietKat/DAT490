import yfinance as yf
import pandas_datareader.data as web
import datetime

sp500_data = yf.download("SPY", start="1999-01-01", end="2024-08-19")
vix_data = yf.download("^VIX", start="1999-01-01", end="2024-08-19")

# Define date range
start_date = datetime.datetime(1999, 1, 1)
end_date = datetime.datetime(2024, 8, 19)

# Interest Rates (10-Year Treasury)
interest_rates = web.DataReader('DGS10', 'fred', start_date, end_date)

# Inflation Rates (CPI)
inflation_rates = web.DataReader('CPIAUCSL', 'fred', start_date, end_date)

# GDP Growth Rates
gdp_growth_rates = web.DataReader('A191RL1Q225SBEA', 'fred', start_date, end_date)

# Employment Data (Unemployment Rate)
employment_data = web.DataReader('UNRATE', 'fred', start_date, end_date)

# Consumer Sentiment Index
consumer_sentiment = web.DataReader('UMCSENT', 'fred', start_date, end_date)

# Save data to CSV
sp500_data.to_csv("sp500_data.csv")
interest_rates.to_csv("interest_rates.csv")
inflation_rates.to_csv("inflation_rates.csv")
gdp_growth_rates.to_csv("gdp_growth_rates.csv")
employment_data.to_csv("employment_data.csv")
consumer_sentiment.to_csv("consumer_sentiment.csv")
vix_data.to_csv("vix_data.csv")