from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db, Base, engine
from app.models import Alert, User
from app.schemas import AlertCreate, AlertResponse

router = APIRouter()

@router.post("/", response_model=AlertResponse)
def create_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db),
    current_user_id: int = 1  # TODO: Get from auth later
):
    # TYPE THIS PART - Your business logic:
    db_alert = Alert(
        user_id=current_user_id,
        symbol=alert.symbol,
        target_price=alert.target_price,
        alert_type=alert.alert_type 
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

@router.get("/", response_model=List[AlertResponse])
def get_alerts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user_id: int = 1  # TODO: Get from auth later
):
    try:
    
      # TYPE THIS PART - Your query:
      alerts = db.query(Alert).filter(
          Alert.user_id == current_user_id
      ).offset(skip).limit(limit).all()
      return alerts
    except Exception as e:
        print(f"ERROR in get_alerts: {e}")
        from app.core.database import engine, Base
        Base.metadata.create_all(bind=engine)
        return []
