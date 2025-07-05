from controllers import LanguageDatabaseController, LanguageTableController, LanguageConfigTableController

language_database = LanguageDatabaseController( log_level="warning" )
language_database.start_database()


language_table = LanguageTableController()
print( language_table.get_all_columns() )
print( language_table.get_all_values() )

language_table.save_tag( "exit", "es", "Salir" )
print( language_table.get_text( "exit", "es" ) )

language_config = LanguageConfigTableController()
print( language_config.get_all_columns() )
print( language_config.get_all_values() )
print( language_config.get_language() )
language_config.update_language( "es" )