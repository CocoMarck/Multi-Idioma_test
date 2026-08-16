// SQLite
using Microsoft.Data.Sqlite;

// Core
using Core.Sqlite;
using Core.LangTags;
using Core.Common; // TextualDateTime

namespace Repositories.LangTags {
    public class TranslationRepository {
        // Variables
        private StandardDatabase _db;
        private StandardTable _table;
        private LanguageRepository _languageRepository;
        private TagRepository _tagRepository;

        // Constructor
        public TranslationRepository(
            StandardDatabase standardDatabase, 
            TagRepository tagRepository, LanguageRepository languageRepository )
        {
            _db = standardDatabase;
            _table = new StandardTable(_db, "translations");
            _tagRepository = tagRepository;
            _languageRepository = languageRepository;
        }

        // Propiedades
        public StandardTable Table { get {return _table;} }

        // Methods
        public void Insert(
            int tagId, int languageId, string value, bool isActive) 
        {
            string now = TextualDateTime.ToText(DateTime.Now);
            object deletedAt = isActive ? DBNull.Value : now;
            _db.Execute(
                sql: "INSERT INTO translations (tag_id, language_id, value, created_at, updated_at, deleted_at, is_active) VALUES (@p0, @p1, @p2, @p3, NULL, @p4, @p5);", commit: true,
                tagId, languageId, value, now, deletedAt, isActive ? 1:0
            );
        }
        public void Update(
            int translationId, int tagId, int languageId, string value, bool isActive) 
        {
            string now = TextualDateTime.ToText(DateTime.Now);
            object updatedAt = isActive ? now : DBNull.Value;
            object deletedAt = isActive ? DBNull.Value : now;
            _db.Execute(
                sql: "UPDATE translations SET tag_id=@p0, language_id=@p1, value=@p2, updated_at=@p3, deleted_at=@p4, is_active=@p5 WHERE translation_id=@p6;", commit: true,
                tagId, languageId, value, updatedAt, deletedAt, isActive ? 1:0, translationId
            );
        }

        public bool ExistsById(int translationId)
        {
            using var reader = _db.Query(
                sql: "SELECT 1 FROM translations WHERE translation_id=@p0 LIMIT 1;",
                translationId
            );
            return reader.Read();
        }
        public bool ExistsByTagIdAndLanguageId(int tagId, int languageId) 
        {
            using var reader = _db.Query(
                sql: "SELECT 1 FROM translations WHERE tag_id=@p0 AND language_id=@p1 LIMIT 1;",
                tagId, languageId
            );
            return reader.Read();
        }
        public bool ExistsByTagNameAndLanguageCode(string tagName, string languageCode) 
        {
            int tagId = _tagRepository.GetIdByName(tagName);
            int languageId = _languageRepository.GetIdByCode(languageCode);
            return ExistsByTagIdAndLanguageId(tagId, languageId);
        }

        public int GetIdByTagIdAndLanguageId(int tagId, int languageId)
        {
            using var reader = _db.Query(
                sql: "SELECT translation_id FROM translations WHERE tag_id=@p0 AND language_id=@p1 LIMIT 1;",
                tagId, languageId
            );
            reader.Read();
            return reader.GetInt32(0);
        }
        public int GetIdByTagNameAndLanguageCode(string tagName, string languageCode)
        {
            int tagId = _tagRepository.GetIdByName(tagName);
            int languageId = _languageRepository.GetIdByCode(languageCode);
            return GetIdByTagIdAndLanguageId(tagId, languageId);
        }
        public string GetValueByTagIdAndLanguageId(int tagId, int languageId)
        {
            using var reader = _db.Query(
                sql: "SELECT value FROM translations WHERE tag_id=@p0 AND language_id=@p1 LIMIT 1;",
                tagId, languageId
            );
            reader.Read();
            return reader.GetString(0);
        }
        public string GetValueByTagNameAndLanguageCode(string tagName, string languageCode)
        {
            int tagId = _tagRepository.GetIdByName(tagName);
            int languageId = _languageRepository.GetIdByCode(languageCode);
            return GetValueByTagIdAndLanguageId(tagId, languageId);
        }

        public void SaveByTagIdAndLanguageId(
            int tagId, int languageId, string value, bool isActive=true, int? translationId=null
        ) 
        {
            // Determinar que exista
            bool exists = false;
            int id = 0;
            if (translationId == null) {
                exists = ExistsByTagIdAndLanguageId(tagId, languageId);
                if (exists){
                    id = GetIdByTagIdAndLanguageId(tagId, languageId);
                }
            } else {
                id = translationId.Value;
                exists = ExistsById(id);
            }
            
            // Escribir data.
            if (exists) {
                Update(id, tagId, languageId, value, isActive);
            } else {
                Insert(tagId, languageId, value, isActive);
            }
        }
        public void SaveByTagNameAndLanguageCode(
            string tagName, string languageCode, string value, bool isActive=true, int? translationId=null
        )
        {
            int tagId = _tagRepository.GetIdByName(tagName);
            int languageId = _languageRepository.GetIdByCode(languageCode);
            SaveByTagIdAndLanguageId( tagId, languageId, value, isActive, translationId );
        }
        public string GetLanguageCodeById(int id){
            return _languageRepository.GetCodeById(id);
        }
        public string GetTagNameById(int id){
            return _tagRepository.GetNameById(id);
        }
    }
}