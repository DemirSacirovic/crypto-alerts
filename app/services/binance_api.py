import requests

def get_binance_price(symbol):
    """
    Dobija trenutnu cenu sa Binance API
    symbol: 'BTCUSDT' ili 'btcusdt'
    returns: float cena ili None ako greska
    """

    #Konvertuj u uppercase
    symbol = symbol.upper().replace('/', '').replace('-','')
    url = "https://api.binance.com/api/v3/ticker/price"

    try:
        response = requests.get(url, params={"symbol":symbol})
        if response.status_code == 200:
            data = response.json()
            #Konvertuj string u float
            price = float(data["price"])
            return price
        else:
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"Exception: {e}")
        return None
