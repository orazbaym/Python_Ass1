from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
print(cg.ping())
print(cg.get_price(ids = 'ethereum', vs_currencies = 'usd'))
