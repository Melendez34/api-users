from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class User(BaseModel):
    """Clase User atributos"""

    name: str = Field(max_length=20, min_length=4)
    username: str = Field(max_length=10, min_length=4)
    email: str = Field(max_length=30, min_length=10)
    password: str = Field(min_length=5, max_length=30)
    im: str = Field(min_length=1, max_length=36)
    id: Optional[int] = None
    updated_at: Optional[datetime] = None
    #  created_at: str = Field()

    class Config:
        """Clase con esquema ejemplo de la clase"""

        schema_extra = {
            "example": {
                "id": 1,
                "name": "Juan Perez",
                "username": "Username",
                "email": "email@email.com",
                "password": "password",
                "im": "ABC-CDE-FGH",
                "created_at": "2039323902",
                "updated_at": "2323223323",
            }
        }
