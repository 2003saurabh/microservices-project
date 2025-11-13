from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import routers

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Service", version="1.0.0")

# ? Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://43.204.232.120:3000"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(routers.router, prefix="/api/v1/products", tags=["products"])

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "product-service"}
