from fastapi import APIRouter
from app.api import users, alerts, prices


api_router = APIRouter()


api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(alerts.router, prefix='/alerts', tags=['alerts'])
api_router.include_router(prices.router, prefix='/prices', tags=['prices'])


