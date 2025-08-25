from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from routers import story, job
from db.database import create_tables

# Create database tables
create_tables()

# Initialize FastAPI app
app = FastAPI(
    title="Choose Your Own Adventure Game API",
    description="API to generate cool stories",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ✅ CORS setup (allow React frontend to connect)
origins = [
    "http://localhost:5173",   # React local dev
    "http://127.0.0.1:5173",   # Sometimes React uses this
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],         # Allow all HTTP methods
    allow_headers=["*"],         # Allow all headers
)

# Include routers
app.include_router(story.router, prefix=settings.API_PREFIX)
app.include_router(job.router, prefix=settings.API_PREFIX)

# Run app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
