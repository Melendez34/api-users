from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from routers.user_router import User

login_router = APIRouter()

@login_router.post('/login', response_model=User, status_code=status.HTTP_200_OK, summary="Login a User", tags=['Auth'])
async def login(user: User):
  """POST login method"""
  if user.email == "admin@gmail.com" and user.password == "admin":
    token: str = create_token(dict(user))
    return JSONResponse(status_code=status.HTTP_200_OK, content=token)
