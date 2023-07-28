from pydantic import BaseModel


class JobRead(BaseModel):
    employee_id: int
    position_id: int
    division_id: int
    date_of_employment: str