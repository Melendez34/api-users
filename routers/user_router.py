from uuid import uuid4
from datetime import datetime
from typing import List, Optional
from fastapi import Depends, Path, Query, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from config.database import Session
from services.user_service import UserService
from schemas.user_schema import User

user_router = APIRouter()


@user_router.get(
    "/users",
    tags=["Users"],
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
def get_users() -> List[User] | JSONResponse:
    """GET users method"""
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(result)
    )


@user_router.get("/users/{id}", tags=["Users"], response_model=User)
def get_user(id: int = Path(gt=0, le=200)) -> User | JSONResponse:
    """GET user con path parameter"""
    db = Session()
    result_query = UserService(db).get_user(id)
    if not result_query:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "not found"}
        )
    return JSONResponse(content=jsonable_encoder(result_query))


@user_router.get("/users/", tags=["Users"])
def get_user_by_username(username: Optional[str] = Query(min_length=4, max_length=25)):
    """GET user by username method"""
    db = Session()
    result_query = UserService(db).get_user_by_username(username)
    if not result_query:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"message": "not found"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(result_query)
    )


@user_router.post("/users", tags=["Users"], status_code=status.HTTP_200_OK)
def create_user(user: User) -> dict | JSONResponse:
    """POST create user method"""
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Se ha registrado User"},
    )


@user_router.put("/users/{id}", tags=["Users"])
def update_user(id: int, user: User):
    """PUT method new user or update user"""
    db = Session()
    result_query = UserService(db).get_user(id)
    if not result_query:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "not found"}
        )
    UserService(db).put_user(id, user)
    return JSONResponse(content={"message": "Se ha modificado User"})


@user_router.delete("/users/{id}", tags=["Users"])
def delete_user(id: int):
    db = Session()
    result_query = UserService(db).get_user(id)
    if not result_query:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "not found"}
        )
    UserService(db).delete_user(id)
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "Se ha eliminado User"}
    )
