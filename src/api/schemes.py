# Схемы, используемые в API

from pydantic import BaseModel


class ID(BaseModel):
    id: int


class StatusOK(BaseModel):
    status: str = "OK"
