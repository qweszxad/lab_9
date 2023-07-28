from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import Employee
from app.modules.employees.schema import EmployeeCreate, EmployeeDelete, EmployeeRead, EmployeeEdit

router = APIRouter(prefix='/employee')

@router.post('/create', status_code=status.HTTP_200_OK)
def create_employee(
        name: str,
        last_name: str,
        patronymic: str,
        birth_date: str,
        db: Session = Depends(get_session)
):
    employee = Employee(name=name, last_name=last_name,
                        patronymic=patronymic, birth_date=birth_date)
    try:
        db.add(employee)
        db.commit()
    except IntegrityError:
        db.rollback()
        return  status.HTTP_500_INTERNAL_SERVER_ERROR
    return employee.to_dict()

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_employee(
        id: int,
        db: Session = Depends(get_session)
):
    employee = db.get(Employee, id)

    if not employee:
        return  status.HTTP_404_NOT_FOUND
    return employee.to_dict()

@router.delete('/delete', status_code=status.HTTP_200_OK)
def delete_employee(
        id: int,
        db: Session = Depends(get_session)
):
    employee = db.delete(Employee, id)

    if not employee:
        return  status.HTTP_404_NOT_FOUND
    try:
        db.delete(employee)
        db.commit()
    except IntegrityError:
        db.rollback()
        return  status.HTTP_500_INTERNAL_SERVER_ERROR

@router.put('/edit', response_model=EmployeeRead, status_code=status.HTTP_200_OK)
def edit_employee(
        id: int,
        data: EmployeeEdit,
        db: Session = Depends(get_session)
):
    employee = db.edit(Employee, id, last_name)

    values - data.dict()
    employee.edit(**values)

    if not employee:
        return  status.HTTP_404_NOT_FOUND
    try:
        employee.last_name = request.args.get()
        db.add(employee)
        db.commit()
    except IntegrityError:
        db.rollback()

    return employee.to_dict()