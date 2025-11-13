import os
import httpx
from typing import Optional

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8001")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8002")

async def get_user(user_id: int) -> Optional[dict]:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{USER_SERVICE_URL}/api/v1/users/{user_id}")
            if response.status_code == 200:
                return response.json()
    except Exception as e:
        print(f"Error fetching user: {e}")
    return None

async def get_product(product_id: int) -> Optional[dict]:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{PRODUCT_SERVICE_URL}/api/v1/products/{product_id}")
            if response.status_code == 200:
                return response.json()
    except Exception as e:
        print(f"Error fetching product: {e}")
    return None
