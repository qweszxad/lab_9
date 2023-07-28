from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import Job
from app.modules.jobs.schema import JobRead

router = APIRouter(prefix='/division')


@router.post('/employment', status_code=status.HTTP_200_OK)
def employment(
        employee_id: int,
        position_id: int,
        division_id: int,
        date_of_employment: str,
        db: Session = Depends(get_session)
):
    job = Job(employee_id=employee_id, position_id=position_id,
              division_id=division_id, date_of_employment=date_of_employment)
    try:
        db.add(job)
        db.commit()
    except IntegrityError:
        db.rollback()
        return  status.HTTP_500_INTERNAL_SERVER_ERROR
    return job.to_dict()


