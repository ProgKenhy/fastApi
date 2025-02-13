from sqlalchemy import text, insert

from database import sync_engine, async_engine, session_factory, Base
from models import WorkersOrm


def create_tables():
    Base.metadata.drop_all(sync_engine)
    sync_engine.echo = True
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersOrm(username='Volk')
        worker_volk = WorkersOrm(username='Bobr')
        session.add_all([worker_bobr, worker_volk])
        session.commit()



