from controllers import LanguageDatabaseController, LanguageTableController

language_database = LanguageDatabaseController( log_level="warning" )
language_database.start_database()


language_table = LanguageTableController()
print(
    language_table.get_all_columns(),
    language_table.get_all_values()
)

print( language_table.get_text( "Hello-pipol" ) )
print( language_table.save_tag( "exit", "es", "Salir" ) )
print( language_table.get_text( "exit", "es" ) )
print( language_table.save_tag( "exit", "es", "Toyota" ) )
print( language_table.get_text( "exit", "es" ) )