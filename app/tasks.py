from app.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.alert import Alert
from app.services.binance import binance_ws



@celery_app.task
def check_price_alert(alert_id: int):
    db = SessionLocal()

    alert = db.query(Alert).filter(Alert.id == alert_id).first()

    if alert:
        print(f"Checking {alert.symbol} > {alert.target_price}")
    
    db.close()
    return f"Alert {alert_id} processed"


@celery_app.task
def check_all_alerts():
    """Check all active alerts"""
    db = SessionLocal()
    
    if not binance_ws.prices:
        binance_ws.start('btcusdt')
        import time
        time.sleep(3)

    alerts = db.query(Alert).filter(Alert.is_active == True).all()
    print(f"DEBUG - All prices in memory: {binance_ws.prices}")
    for alert in alerts:
        current_price =  binance_ws.get_price(alert.symbol)
        print(f"{alert.symbol}: Current: ${current_price}, Target:${alert.target_price}")

        if alert.alert_type == 'above' and current_price >= alert.target_price:
            alert.is_active = False
            db.commit()
    db.close()
    return f"Checked {len(alerts)} alerts"


