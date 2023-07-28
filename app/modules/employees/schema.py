from pydantic import BaseModel


class EmployeeRead(BaseModel):
    id: int
    name: str
    last_name: str
    patronymic: str
    birth_date: str

class EmployeeCreate(BaseModel):
    name: str
    last_name: str
    patronymic: str
    birth_date: str

class EmployeeDelete(BaseModel):
    id: int

class EmployeeEdit(BaseModel):
    id: int
    last_name: str