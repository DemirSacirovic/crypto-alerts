from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional


class AlertBase(BaseModel):
    symbol: str
    target_price: float
    alert_type: str

    @validator('alert_type')
    def validate_alert_type(cls, v):
        if v not in ['above', 'bellow']:
            raise ValueError('alert_type must be "above" or "below"')
        return v

class AlertCreate(AlertBase):
    pass

class AlertResponse(AlertBase):
    id: int
    user_id: int
    is_active: bool
    triggered_at: Optional[datetime]
    created_at: datetime
    

    class Config:
        from_attributes = True
