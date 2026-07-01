// SQLite
using Microsoft.Data.Sqlite;

namespace Core.Sqlite {
    // Para obtener datos de tabla de manera estandar. Solo depende del nombre de la tabla.
    public class StandardTable {
        // Variables
        private StandardDatabase _db;
        private string _name;

        // Constructor
        public StandardTable(StandardDatabase standardDatabase, string name){
            _db = standardDatabase;
            _name = name;
        }

        // Propiedades
        public string Name {
            get { return _name; }
        }

        // Methods
        public SqliteDataReader GetAllRows() {
            return _db.Query($"SELECT * FROM \"{_name}\";");
        }

        public int CountRows(){
            using var reader = _db.Query($"SELECT COUNT(*) FROM \"{_name}\";");
            reader.Read();
            return reader.GetInt32(0);
        }
    }
}