// SQLite
using Microsoft.Data.Sqlite;

// Core
using Core.Sqlite;
using Core.LangTags;
using Core.Common; // TextualDateTime

namespace Repositories.LangTags {
    public class TagRepository {
        // Variables
        private StandardDatabase _db;
        private StandardTable _table;

        // Constructor
        public TagRepository(StandardDatabase standardDatabase){
            _db = standardDatabase;
            _table = new StandardTable(_db, "tags");
        }

        // Propiedades
        public StandardTable Table { get {return _table;} }

        // Methods. No TRY, full crash si pasas cosas mal.
        public void Insert(string name, bool isActive){     
            // Solo create at y deleted at para insert. updated at solo update method.
            string now = TextualDateTime.ToText(DateTime.Now);
            object deletedAt = isActive ? DBNull.Value : now;
            string normalizedName = TagNameNormalizer.Normalize(name);
            _db.Execute(
                sql: "INSERT INTO tags (name, created_at, updated_at, deleted_at, is_active) VALUES (@p0, @p1, NULL, @p2, @p3);", commit: true,
                normalizedName, now, deletedAt, isActive ? 1 : 0
            );
        }

        public void Update(int tagId, string name, bool isActive )
        {
            // Solo update at si esta active.
            string now = TextualDateTime.ToText(DateTime.Now);
            object updatedAt = isActive ? now : DBNull.Value;
            object deletedAt = isActive ? DBNull.Value : now;
            string normalizedName = TagNameNormalizer.Normalize(name);
            _db.Execute(
                sql: "UPDATE tags SET name=@p0, updated_at=@p1, deleted_at=@p2, is_active=@p3 WHERE tag_id=@p4;", commit:true,
                normalizedName, updatedAt, deletedAt, isActive ? 1 : 0, tagId
            );
        }

        public bool ExistsById(int tagId){
            using var reader = _db.Query(
                sql: "SELECT 1 FROM tags WHERE tag_id=@p0 LIMIT 1;",
                tagId
            );
            return reader.Read();
        }
        public bool ExistsByName(string name){
            string normalizedName = TagNameNormalizer.Normalize(name);
            using var reader = _db.Query(
                sql: "SELECT 1 FROM tags WHERE name=@p0 LIMIT 1;",
                normalizedName
            );
            return reader.Read();
        }

        public int GetIdByName(string name){
            string normalizedName = TagNameNormalizer.Normalize(name);
            using var reader = _db.Query(
                sql: "SELECT tag_id FROM tags WHERE name=@p0 LIMIT 1;",
                normalizedName
            );
            reader.Read();
            return reader.GetInt32(0);
        }

        public string GetNameById(int tagId){
            using var reader = _db.Query(
                sql: "SELECT name FROM tags WHERE tag_id=@p0 LIMIT 1;",
                tagId
            );
            reader.Read();
            return reader.GetString(0);
        }

        public void Save(string name, bool isActive=true, int? tagId=null)
        {
            // Determinar que exista
            bool exists = false;
            int id = 0;
            if (tagId == null) {
                exists = ExistsByName(name);
                if (exists){
                    id = GetIdByName(name);
                }
            } else {
                id = tagId.Value;
                exists = ExistsById(id);
            }
            
            // Escribir data.
            if (exists) {
                Update(id, name, isActive);
            } else {
                Insert(name, isActive);
            }
        }

        public void Activate(int tagId)
        {
            string now = TextualDateTime.ToText(DateTime.Now);
            _db.Execute(
                sql: "UPDATE tags SET updated_at=@p0, deleted_at=NULL, is_active=1 WHERE tag_id=@p1;", commit:true,
                now, tagId
            );
        }
        public void Deactivate(int tagId)
        {
            string now = TextualDateTime.ToText(DateTime.Now);
            _db.Execute(
                sql: "UPDATE tags SET deleted_at=@p0, is_active=0 WHERE tag_id=@p1;", commit:true,
                now, tagId
            );
        }
        //
    }
}