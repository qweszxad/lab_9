from sqlalchemy import inspect, Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class BaseMixin(Base):
    __abstract__ = True

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in
                inspect(self).mapper.column_attrs}


class Employee(BaseMixin):
    __tablename__ = "VAD_employees"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    patronymic = Column(String(30), nullable =False)
    address = Column(String(100), nullable=False)
    birth_date = Column(String, nullable=False)


class Position(BaseMixin):
    __tablename__ = "VAD_positions"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)


class Division(BaseMixin):
    __tablename__ = "VAD_divisions"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)


class Job(BaseMixin):
    __tablename__ = "VAD_jobs"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('VAD_employees.id'))
    position_id = Column(Integer, ForeignKey('VAD_positions.id'))
    division_id = Column(Integer, ForeignKey('VAD_divisions.id'))
    date_of_employment = Column(String, nullable=False)
    date_of_dismissal = Column(String)