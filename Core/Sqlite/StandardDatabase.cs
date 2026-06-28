// CSharp
using static System.Console;
using System.IO;

// SQLite
using Microsoft.Data.Sqlite;

namespace Core.Sqlite {
    /*
    Clase que permite manejar el trabajo basico con una base de datos sqlite.
    */
    public class StandardDatabase {
        // Variables
        private string _directory;
        private string _name;

        // Constructor
        public StandardDatabase(string directory, string name){
            _directory = directory;
            _name = name;
        }

        // Propiedades

        // Methods SQLite
        private SqliteConnection Connect(){
            return new SqliteConnection($"Data Source={GetPath()}");
        }

        public bool LoadSchemaFromFile( string schemaFile ){
            string scriptText = File.ReadAllText(schemaFile);

            try {
                using var connection = Connect();
                connection.Open();
                using var command = connection.CreateCommand();
                command.CommandText = scriptText;
                command.ExecuteNonQuery();
                connection.Close();
                return true;
            }
            catch (Exception e){
                return false;
            }
        }

        // Mehtods File
        public string GetPath(){
            return Path.Combine(_directory, _name);
        }

        public bool Exists(){
            return File.Exists(GetPath());
        }

        public bool CreateFile(){
            if ( !Exists() ){
                using var connection = Connect();
                connection.Open();
                connection.Close();
                return true;
            }
            return false;
        }
        //
    }
    //
}
