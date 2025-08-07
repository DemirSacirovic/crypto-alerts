import json
import websocket
import threading
from typing import Callable, Dict


class BinanceWebSocket:
    """Klasa za praćenje cena kripto valuta uživo"""

    def __init__(self):
        self.ws = None
        self.prices = {}

    def on_message(self, ws, message):
        """Kada stigne nova cena"""
        data = json.loads(message)
        symbol = data['s']
        price = float(data['c'])
        self.prices[symbol] = price
        print(f'{symbol}: ${price}')

    def on_error(self, ws, error):
        """AKo se desi greska"""
        print(f'WebSocket error: {error}')

    def on_close(self, ws, close_status_code, close_msg):
        """Kada se konekcija zatvori"""
        print('Websocket connection closed')

    def on_open(self, ws):
        """Kada se konekcija otvori"""
        print('WebSocket connection opened')

    def start(self, symbol: str = 'btcusdt'):
        """Pokreni WebSocket za pracenje cena"""
        url = f"wss://stream.binance.com:9443/ws/{symbol}@ticker"

        self.ws = websocket.WebSocketApp( url, on_open=self.on_open, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)

        wst = threading.Thread(target=self.ws.run_forever)
        wst.daemon = True
        wst.start()

    def get_price(self, symbol:str) -> float:
        """Vrati trenutnu cenu"""
        return self.prices.get(symbol.upper(), 0.0)

    def stop(self):
        """Zaustavi WebSocket"""
        if self.ws:
            self.ws.close()

binance_ws = BinanceWebSocket()


