from models import LanguageDataBase
from controllers import LanguageDataBaseController

language_database = LanguageDataBaseController( log_level="error" )
language_database.start_database()