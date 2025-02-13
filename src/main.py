import os
import sys
from queries.core import SyncCore

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.orm import SyncOrm


SyncCore.create_tables()
SyncCore.insert_data()
SyncOrm.select_workers()
SyncOrm.update_worker()
