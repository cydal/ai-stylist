from fastapi import FastAPI
from .api.router import router as api_router

def create_application() -> FastAPI:
    app = FastAPI(title="AI Stylist Backend")
    app.include_router(api_router, prefix="/api")
    return app

app = create_application()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to the AI Stylist API!"}