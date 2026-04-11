import yfinance as yf 
df = yf.download('^NSEI', start='2022-01-01', end='2026-01-01')
df.to_csv('Nifty50.csv')
