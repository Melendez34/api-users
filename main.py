"""Main file API Users"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base, engine
from middlewares.error_handler import Error_Handler
from routers.user_router import user_router
from routers.login_router import login_router

app = FastAPI()
app.title = "Aplicacion FastAPI"
app.version = "0.0.1"

app.add_middleware(Error_Handler)
app.include_router(user_router)
app.include_router(login_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['Home'])
def message():
  """message method"""
  return HTMLResponse('<h1>Hola Mundo!</h1>')

