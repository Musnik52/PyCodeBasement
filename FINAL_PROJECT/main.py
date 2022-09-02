from db_files.db_repo import DbRepo
from db_files.db_config import local_session
from facades.facade_anonymus import AnonymusFacade

# defining
repo = DbRepo(local_session)

# db_refresh
repo.reset_db()
print('DONE')
