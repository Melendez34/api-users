from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class User(BaseModel):
    """Clase User atributos"""

    id: Optional[int] = None
    name: str = Field(max_length=20, min_length=4)
    user_name: str = Field(max_length=10, min_length=4)
    email: str = Field(max_length=30, min_length=10)
    password: str = Field(min_length=5, max_length=30)
    im: str = Field(min_length=1, max_length=36)
    created_at: int = Field(int, max_digits=7, min_length=6)
    updated_at: Optional[int] = None

    class Config:
        """Clase con esquema ejemplo de la clase"""

        schema_extra = {
            "example": {
                "id": 1,
                "name": "Juan Perez",
                "user_name": "Username",
                "email": "email@email.com",
                "password": "password",
                "im": "ABC-CDE-FGH",
                "created_at": "2039323902",
                "updated_at": "2323223323",
            }
        }
