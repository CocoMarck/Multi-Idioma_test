// Repositories
using Repositories.LangTags;

// Core
using Core.Sqlite;

// Config
using Config;

public static class Program {
    static void Main(){
        // Objects
        var paths = new Paths();
        var db = new StandardDatabase(paths.DATA_DIR, "LangTags.sqlite");
        var languageRepository = new LanguageRepository(db);
        var tagRepository = new TagRepository(db);
        var translationRepository = new TranslationRepository(
            db, tagRepository, languageRepository);

        // Init DB
        Console.WriteLine( $"Config dir: `{paths.CONFIG_DIR}`" );

        bool createDB = db.CreateFile();
        Console.WriteLine( $"Create DB: {createDB}");
        try {
            db.Execute(
                sql:"PRAGMA foreign_keys = ON;", commit:true
            );
        } catch (Exception e)
        {
            Console.WriteLine( $"ERROR: {e}");
        }
        foreach (string file in paths.SCHEMAS_FILES){
            // Crear DB si no existe, y poner sus schemas we.
            Console.WriteLine( $"Schema: `{file}`" );
            db.LoadSchemaFromFile( file );
        }
        foreach (string name in db.GetTableNames()){
            Console.WriteLine( name );
        }

        // Save first values
        languageRepository.Save("en", true);
        languageRepository.Save("es", true);
        languageRepository.Save("pt", false);
        languageRepository.Save("ru", true);
        languageRepository.Deactivate(4);
        Console.WriteLine( languageRepository.Table.CountRows() );

        tagRepository.Save("Hello   ", true );
        tagRepository.Save("happy moment", true);
        tagRepository.Save("Exit", true);
        tagRepository.Save("Settings", true);
        tagRepository.Save("Trajectories", true);
        Console.WriteLine( tagRepository.Table.CountRows() );

        translationRepository.SaveByTagNameAndLanguageCode(
            "hello", "en", "Hello");
        translationRepository.SaveByTagNameAndLanguageCode(
            "trajectories", "en", "Trajectories");
        translationRepository.SaveByTagNameAndLanguageCode(
            "hello", "es", "Hola");
        translationRepository.SaveByTagNameAndLanguageCode(
            "trajectories", "es", "Trayectorias");
        Console.WriteLine( translationRepository.Table.CountRows() );
    }
    //
}
