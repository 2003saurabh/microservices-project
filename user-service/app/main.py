from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import routers

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="User Service", version="1.0.0")

# ? Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with specific domains later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routers.router, prefix="/api/v1/users", tags=["users"])

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "user-service"}
