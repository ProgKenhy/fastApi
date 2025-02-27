from sqlalchemy import text, insert, select, update

from database import sync_engine, async_engine, session_factory, Base
from models import WorkersOrm

class SyncOrm:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        sync_engine.echo = True
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True


    @staticmethod
    def insert_data():
        with session_factory() as session:
            worker_bobr = WorkersOrm(username='Volk')
            worker_volk = WorkersOrm(username='Bobr')
            session.add_all([worker_bobr, worker_volk])
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            query = select(WorkersOrm)
            result = session.execute(query)
            workers = result.scalars().all()
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = 'xuy bodrey'):
        with session_factory() as session:
            worker_bobr = session.get(WorkersOrm, worker_id)
            worker_bobr.username = new_username
            session.commit()


class AsyncOrm:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

