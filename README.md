# Python_Ass1

- Assignment 1


- Installation
    git clone https://github.com/man-c/pycoingecko.git
    cd pycoingecko
    python setup.py install


- Usage
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()
    
    
- Examples
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()
    print(cg.ping())
    
    {'gecko_says': '(V3) To the Moon!'}
    {'bitcoin': {'usd': 43400}}
    
      
      
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()
    print(cg.ping())
    print(cg.get_price(ids = 'ethereum', vs_currencies = 'usd'))

    {'gecko_says': '(V3) To the Moon!'}
    {'ethereum': {'usd': 3061.74}}
