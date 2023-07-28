from pydantic import BaseModel


class PositionRead(BaseModel):
    id: int
    title: str


class PositionCreate(BaseModel):
    title: str

class PositionDelete(BaseModel):
    id: int