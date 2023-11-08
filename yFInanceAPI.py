import yfinance as yf

symbol = "MSFT"
sp500 = yf.Ticker(symbol)
historical_data = sp500.history(period="3y")  # Fetch data for the last year
selected_data = historical_data[['Open', 'High', 'Low', 'Close', 'Volume']]
selected_data['Date'] = historical_data.index.date  # Adding the 'Date' column
selected_data = selected_data.reindex(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

selected_data.to_csv('Microsoft_Data.csv', index=False)