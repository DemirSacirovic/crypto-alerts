from fastapi import APIRouter
from app.services.binance import binance_ws


router = APIRouter()

@router.get('/current/{symbol}')
def get_current_price(symbol: str):
    """Vrati trenutnu cenu za simbol"""
    price = binance_ws.get_price(symbol)
    return { 'symbol': symbol.upper(),
        'price': price,
        'status': 'live' if price > 0 else 'waiting'
    }


@router.get('/current')
def get_all_prices():
    """Vrati sve trenutne cene"""
    return binance_ws.prices

 
