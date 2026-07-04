using System.Collections.Generic;

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
            using SqliteDataReader reader = _db.Query($"SELECT COUNT(*) FROM \"{_name}\";");
            reader.Read();
            return reader.GetInt32(0);
        }

        public int CountColumns(){
            using SqliteDataReader reader = GetAllRows();
            return reader.FieldCount;
        }

        public string[] GetColumnNames() {
            using SqliteDataReader reader = GetAllRows();
            var names = new string[reader.FieldCount];
            for (int i = 0; i <names.Length; i++){
                names[i] = reader.GetName(0);
            }
            return names;
        }

        public List<string[]> GetRowValues() {
            using SqliteDataReader reader = GetAllRows();
            var rows = new List<string[]>();
            int cols = reader.FieldCount;
            while (reader.Read()) {
                var row = new string[cols];
                for (int i = 0; i < cols; i++){
                    row[i] = reader.IsDBNull(i) ? null : reader.GetValue(i).ToString();
                }
                rows.Add(row);
            }
            return rows;
        }

    }
}
