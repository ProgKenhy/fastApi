import asyncio
import os
import sys
from fastapi import FastAPI
# from queries.core import SyncCore

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.orm import SyncOrm, AsyncOrm

app = FastAPI()

@app.post('setup/database')
async def main():
    await AsyncOrm.create_tables()
    SyncOrm.insert_data()
    SyncOrm.select_workers()
    SyncOrm.update_worker()

if __name__ == "__main__":
    asyncio.run(main())