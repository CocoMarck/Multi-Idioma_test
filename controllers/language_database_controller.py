from models import LanguageDataBase
from .database_controller import DataBaseController

class LanguageDataBaseController( DataBaseController ):
    def __init__(self, log_level="warning"):
        super().__init__( 
            database=LanguageDataBase(), verbose=True, return_message=False, save_log=True,
            log_level=log_level
        )