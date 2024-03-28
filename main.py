from fastapi import FastAPI
from database import Base, engine
from transaction.currency_api import currency_router

app = FastAPI(docs_url='/')

app.include_router(currency_router)