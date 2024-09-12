from fastapi import FastAPI
from app import views

app = FastAPI()

app.include_router(views.router)