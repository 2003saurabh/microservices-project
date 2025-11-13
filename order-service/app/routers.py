from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.external_services import get_user, get_product

router = APIRouter()

@router.post("/", response_model=schemas.OrderResponse, status_code=201)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    user = await get_user(order.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    product = await get_product(order.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product["stock"] < order.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    total_price = product["price"] * order.quantity

    db_order = models.Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=total_price,
        status="confirmed"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/{order_id}", response_model=schemas.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/", response_model=list[schemas.OrderResponse])
def list_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    orders = db.query(models.Order).offset(skip).limit(limit).all()
    return orders
