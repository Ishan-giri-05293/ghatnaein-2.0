from fastapi import FastAPI
from app.api.news import router as news_router

app = FastAPI(
    title="Ghatnaein 2.0 API",
    description="Backend API for the new Ghatnaein news platform",
    version="0.1.0",
)
app.include_router(news_router)


@app.get("/")
def root():
    return {
        "message": "Ghatnaein 2.0 API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ghatnaein-api",
    }