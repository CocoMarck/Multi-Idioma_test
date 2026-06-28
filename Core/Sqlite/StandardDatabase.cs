// CSharp
using static System.Console;
using System.IO;
using System.Data;

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

        public SqliteDataReader Query(string statement, params object[] parameters){
            /*
            using var reader = db.Query("SELECT * FROM demo");
            while (reader.Read()){
                Console.WriteLine($"{reader.GetInt32(0)} - {reader.GetString(1)}");
            }
            */
            var connection = Connect();
            connection.Open();

            using var command = connection.CreateCommand();
            command.CommandText = statement;

            for (int i=0; i < parameters.Length; i++){
                command.Parameters.AddWithValue($"@p{i}", parameters[1]);
            }

            return command.ExecuteReader( CommandBehavior.CloseConnection );
        }

        public SqliteDataReader Execute(string statement, bool commit, params object[] parameters ){
            /*
            // Ejemplo con rollback
            using var reader = db.ExecuteQuery("SELECT * FROM demo WHERE nombre=@p0", false, "Simon");

            while (reader.Read()){
                Console.WriteLine($"{reader.GetInt32(0)} - {reader.GetString(1)}");
            }
            */
            var connection = Connect();
            connection.Open();

            using var transaction = connection.BeginTransaction();
            using var command = connection.CreateCommand();
            command.CommandText = statement;
            command.Transaction = transaction;

            // Agregar parámetros
            for (int i = 0; i < parameters.Length; i++){
                command.Parameters.AddWithValue($"@p{i}", parameters[i]);
            }

            var reader = command.ExecuteReader();

            if (commit){
                transaction.Commit();
            } else {
                transaction.Rollback();
            }

            // Reader necesita que la conexión siga viva
            return reader;
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
