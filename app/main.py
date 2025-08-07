from app.services.binance import binance_ws
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router

app = FastAPI(title = 'Crypto Alert System', description = 'Real-time cryptocurrency price alerts', version ='1.0.0')

app.add_middleware (CORSMiddleware, allow_origins=['*'], allow_credentials = True, allow_methods=['*'], allow_headers=['*'],)

@app.get('/')
async def root():
    return {'message' : 'Crypto alert system API', 'status' : 'operational'}

@app.get('/health')
async def health_check():
    return {'status' : 'healthy', 'service' : 'crypto-alerts'}

app.include_router(api_router, prefix='/api')


@app.on_event('startup')
async def startup_event():
    binance_ws.start('btcusdt')
    print('Binance WebSocket stared!')


@app.on_event('shutdown')
async def shutdown_event():
    binance_ws.stop()
    print('Binance WebSocket stopped!')



