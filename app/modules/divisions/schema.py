from pydantic import BaseModel


class DivisionRead(BaseModel):
    id: int
    title: str


class DivisionCreate(BaseModel):
    title: str

class DivisionDelete(BaseModel):
    id: int