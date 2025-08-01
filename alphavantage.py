import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=iex.ams&apikey=4M35HGZYSOR6J1X5'
r = requests.get(url)
data = r.json()

print(data)