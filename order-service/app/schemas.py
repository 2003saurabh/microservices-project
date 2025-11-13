from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    total_price: float
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
