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

        public SqliteDataReader Query(string sql, params object[] parameters){
            /*
            Para commit y consultas.
            using var reader = db.Query("SELECT * FROM demo");
            while (reader.Read()){
                Console.WriteLine($"{reader.GetInt32(0)} - {reader.GetString(1)}");
            }
            */
            SqliteConnection connection = Connect();
            connection.Open();

            var command = connection.CreateCommand();
            command.CommandText = sql;

            for (int i=0; i < parameters.Length; i++){
                command.Parameters.AddWithValue($"@p{i}", parameters[i]);
            }

            return command.ExecuteReader( CommandBehavior.CloseConnection );
        }

        public void Execute(string sql, bool commit, params object[] parameters ){
            /*
            Un execute sin reader, porque no se puede para el rollback logic.
            */
            using SqliteConnection connection = Connect();
            connection.Open();
            using var transaction = connection.BeginTransaction();
            using var command = connection.CreateCommand();
            command.CommandText = sql;
            command.Transaction = transaction;

            for (int i = 0; i < parameters.Length; i++)
                command.Parameters.AddWithValue($"@p{i}", parameters[i]);

            command.ExecuteNonQuery();

            if (commit) transaction.Commit();
            else transaction.Rollback();
        }

        // Methods util querys
        public SqliteDataReader GetTables(){
            return Query(
                sql: "SELECT name FROM sqlite_master WHERE type='table';"
            );
        }

        public string[] GetTableNames(){
            var tableNames = new List<string>();
            using var reader = GetTables();
            while (reader.Read()){
                tableNames.Add(reader.GetString(0));
            }
            return tableNames.ToArray();
        }

        public bool ExistingTable(string name){
            return GetTableNames().Contains(name);
        }

        public bool DropTable(string name){
            Execute( $"DROP TABLE \"{name}\";", commit:true);
            return (ExistingTable(name) == false);
        }

        public bool DropTables(){
            foreach (string name in GetTableNames()){
                DropTable(name);
            }
            return GetTableNames().Length == 0;
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
                using SqliteConnection connection = Connect();
                connection.Open();
                connection.Close();
                return true;
            }
            return false;
        }

        public bool DeleteFile(){
            if (Exists()){
                File.Delete( GetPath() );
                return true;
            }
            return false;
        }
        //
    }
    //
}
