import time
from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    """Clase User atributos"""

    id: Optional[int] = None
    name: str = Field(max_length=20, min_length=4)
    user_name: str = Field(max_length=10, min_length=4)
    email: str = Field(max_length=30, min_length=10)
    password: str = Field(min_length=5, max_length=30)
    im: str = Field(str(uuid4()), max_length=36)
    created_at: int = Field(int(time.time()), min_length=9)
    updated_at: Optional[int] = None

    class Config:
        """Clase con esquema ejemplo de la clase"""

        schema_extra = {
            "example": {
                "id": 1,
                "im": "a1b2c345-c1de-f2gh-3ijk-8d8b3b302d3p",
                "name": "Juan Perez",
                "user_name": "Juan123",
                "email": "email@email.com",
                "password": "hashed",
                "id_provider": "uuid4",
                "provider": "Google",
                "birthday_user": "datetime",
                "age_range": "string",
                "fullname": "Juan Perez Perez",
                "gender": "binare",
                "created_at": "239323902",
                "updated_at": "223223323",
            }
        }
