from app.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.alert import Alert
from app.services.binance_api import get_binance_price



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
    

    alerts = db.query(Alert).filter(Alert.is_active == True).all()
   
    for alert in alerts:
        current_price = get_binance_price(alert.symbol)
        if current_price:

            print(f"{alert.symbol}: Current: ${current_price:.2f}, Target:${alert.target_price}")
            if alert.alert_type == 'above' and current_price >= alert.target_price:
                print(f"ALERT TRIGGERED! {alert.symbol} reached ${current_price:.2f}")
                alert.is_active = False
                db.commit()
             
        else:
            print(f"Could not get price for {alert.symbol}")
    db.close()
    return f"Checked {len(alerts)} alerts"

