import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

# from queries.orm import SyncOrm
from queries.core import SyncCore


SyncCore.create_tables()
SyncCore.insert_data()
# SyncOrm.select_workers()
# SyncOrm.update_worker()