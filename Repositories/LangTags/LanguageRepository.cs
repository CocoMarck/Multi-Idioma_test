// SQLite
using Microsoft.Data.Sqlite;

// Entidades
using Entities.LangTags;

// Core
using Core.Sqlite;

// Utils
using Utils.Text;

namespace Repositories.LangTags {
    public class LanguageRepository {
        // Variables
        private StandardDatabase _db;
        private StandardTable _table;

        // Constructor
        public LanguageRepository(StandardDatabase standardDatabase){
            _db = standardDatabase;
            _table = new StandardTable(_db, "languages");
        }

        // Propiedades
        public StandardTable Table { get {return _table;} }

        // Methods. No TRY, full crash si pasas cosas mal.
        public void Insert(string code, bool isActive){     
            // Solo create at y deleted at para insert. updated at solo update method.
            string now = TextualDateTime.ToText(DateTime.Now);
            object deletedAt = isActive ? DBNull.Value : now;
            _db.Execute(
                sql: "INSERT INTO languages (code, created_at, updated_at, deleted_at, is_active) VALUES (@p0, @p1, NULL, @p2, @p3);", commit: true,
                code, now, deletedAt, isActive ? 1 : 0
            );
        }

        public void Update(int languageId, string code, bool isActive )
        {
            // Solo update at si esta active.
            string now = TextualDateTime.ToText(DateTime.Now);
            object updatedAt = isActive ? now : DBNull.Value;
            object deletedAt = isActive ? DBNull.Value : now;
            _db.Execute(
                sql: "UPDATE languages SET code=@p0, updated_at=@p1, deleted_at=@p2, is_active=@p3 WHERE language_id=@p4;", commit:true,
                code, updatedAt, deletedAt, isActive ? 1 : 0, languageId
            );
        }

        public bool ExistsById(int languageId){
            using var reader = _db.Query(
                sql: "SELECT 1 FROM languages WHERE language_id=@p0 LIMIT 1;",
                languageId
            );
            return reader.Read();
        }
        public bool ExistsByCode(string code){
            using var reader = _db.Query(
                sql: "SELECT 1 FROM languages WHERE code=@p0 LIMIT 1;",
                code
            );
            return reader.Read();
        }

        public int GetIdByCode(string code){
            using var reader = _db.Query(
                sql: "SELECT language_id FROM languages WHERE code=@p0 LIMIT 1;",
                code
            );
            reader.Read();
            return reader.GetInt32(0);
        }

        public string GetCodeById(int languageId){
            using var reader = _db.Query(
                sql: "SELECT code FROM languages WHERE language_id=@p0 LIMIT 1;",
                languageId
            );
            reader.Read();
            return reader.GetString(0);
        }

        public void Save(string code, bool isActive=true, int? languageId=null)
        {
            // Determinar que exista
            bool exists = false;
            int id = 0;
            if (languageId == null) {
                exists = ExistsByCode(code);
                if (exists){
                    id = GetIdByCode(code);
                }
            } else {
                id = languageId.Value;
                exists = ExistsById(id);
            }
            
            // Escribir data.
            if (exists) {
                Update(id, code, isActive);
            } else {
                Insert(code, isActive);
            }
        }

        public void Activate(int languageId)
        {
            string now = TextualDateTime.ToText(DateTime.Now);
            _db.Execute(
                sql: "UPDATE languages SET updated_at=@p0, deleted_at=NULL, is_active=1 WHERE language_id=@p1;", commit:true,
                now, languageId
            );
        }
        public void Deactivate(int languageId)
        {
            string now = TextualDateTime.ToText(DateTime.Now);
            _db.Execute(
                sql: "UPDATE languages SET deleted_at=@p0, is_active=0 WHERE language_id=@p1;", commit:true,
                now, languageId
            );
        }
        //
    }
}