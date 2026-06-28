using Microsoft.Data.Sqlite;
using Core.Sqlite;
using Config;

public static class Program {
    static void Main(){
        // Objects
        var paths = new Paths();
        var standardDatabase = new StandardDatabase(paths.DATA_DIR, "LangTags.sqlite");

        // Init DB
        Console.WriteLine( $"Config dir: `{paths.CONFIG_DIR}`" );

        bool createDB = standardDatabase.CreateFile();
        Console.WriteLine( $"Create DB: {createDB}");

        foreach (string file in paths.SCHEMAS_FILES){
            // Crear DB si no existe, y poner sus schemas we.
            Console.WriteLine( $"Schema: `{file}`" );
            standardDatabase.LoadSchemaFromFile( file );
        }
    }
    //
}
