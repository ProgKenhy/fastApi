import enum
from datetime import datetime
from typing import Optional, Annotated

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base, str_256


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow)]


class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    username: Mapped[str]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = 'resumes'
    id: Mapped[intpk]
    title: Mapped[str_256] = mapped_column(String(256))
    compensation: Mapped[Optional[str]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete='CASCADE'))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]















metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),

)
