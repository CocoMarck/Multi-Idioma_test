using Microsoft.Data.Sqlite;
using Core.Sqlite;
using Config;

public static class Program {
    static void Main(){
        // Objects
        var paths = new Paths();
        var db = new StandardDatabase(paths.DATA_DIR, "LangTags.sqlite");

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
    }
    //
}
