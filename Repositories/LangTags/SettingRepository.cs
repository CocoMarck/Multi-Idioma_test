// Core 
using Core;
using Core.Sqlite;

namespace Repositories.LangTags
{
    public class SettingRepository
    {
        // Variables
        private StandardDatabase _db;
        private StandardTable _table;
        private LanguageRepository _languageRepository; 
        
        // Constructor
        public SettingRepository(StandardDatabase standardDatabase, LanguageRepository languageRepository)
        {
            _db = standardDatabase;
            _table = new StandardTable(_db, "settings");
            _languageRepository = languageRepository;
        }

        public void InitParameters()
        {
            if (!ExistsByParameterName("default_language"))
            {
                Save("default_language", 1);
            }
            if (!ExistsByParameterName("selected_language"))
            {
                Save("selected_language", 1);
            }
            if (!ExistsByParameterName("system_language"))
            {
                Save("system_language", 0);
            }
        }

        // Propiedades
        public StandardTable Table { get{ return _table;} }

        // Methods
        public void Insert(string parameterName, int languageId)
        {
            _db.Execute(
                sql: "INSERT INTO settings (parameter_name, language_id) VALUES(@p0, @p1);", 
                commit:true, parameterName, languageId 
            );
        }
        public void Update(int settingId, string parameterName, int languageId)
        {
            _db.Execute(
                sql: "UPDATE settings SET language_id=@p0 WHERE parameter_name=@p1;", 
                commit:true, languageId, parameterName 
            );
        }

        public bool ExistsById(int settingId)
        {
            using var reader = _db.Query(
                sql: "SELECT 1 FROM settings WHERE setting_id=@p0 LIMIT 1;",
                settingId
            );
            return reader.Read();
        }
        public bool ExistsByParameterName(string parameterName)
        {
            using var reader = _db.Query(
                sql: "SELECT 1 FROM settings WHERE parameter_name=@p0 LIMIT 1;", 
                parameterName
            );
            return reader.Read();
        }

        public int GetIdByParameterName(string parameterName){
            using var reader = _db.Query(
                sql: "SELECT setting_id FROM settings WHERE parameter_name=@p0 LIMIT 1;",
                parameterName
            );
            reader.Read();
            return reader.GetInt32(0);
        }
        public string GetParameterNameById(int settingId){
            using var reader = _db.Query(
                sql: "SELECT parameter_name FROM settings WHERE setting_id=@p0 LIMIT 1;",
                settingId
            );
            reader.Read();
            return reader.GetString(0);
        }
        public int GetLanguageIdByParameterName(string parameterName){
            using var reader = _db.Query(
                sql: "SELECT language_id FROM settings WHERE parameter_name=@p0 LIMIT 1;",
                parameterName
            );
            reader.Read();
            return reader.GetInt32(0);
        }
        public string GetParameterNameByLanguageId(int languageId){
            using var reader = _db.Query(
                sql: "SELECT parameter_name FROM settings WHERE language_id=@p0 LIMIT 1;",
                languageId
            );
            reader.Read();
            return reader.GetString(0);
        }

        public void Save(string parameterName, int languageId, int? settingId=null)
        {
            // Determinar que exista
            bool exists = false;
            int id = 0;
            if (settingId == null) {
                exists = ExistsByParameterName(parameterName);
                if (exists){
                    id = GetIdByParameterName(parameterName);
                }
            } else {
                id = settingId.Value;
                exists = ExistsById(id);
            }
            
            // Escribir data.
            if (exists) {
                Update(id, parameterName, languageId);
            } else {
                Insert(parameterName, languageId);
            }
        }


        public int GetSelectedLanguageId()
        {
            return GetLanguageIdByParameterName( "selected_language" );
        }
        public string GetSelectedLanguageCode()
        {
            int id = GetSelectedLanguageId();
            if (id == GetSystemLanguageId())
            {
                return GetSystemLanguageCode();
            }
            else 
            {
                return _languageRepository.GetCodeById(id);
            }
        }
        public void UpdateSelectedLanguageId(int languageId)
        {
            int id = GetIdByParameterName("selected_language");
            Update(id, "selected_language", languageId);
        }
        public void UpdateSelectedLanguageCode(string code)
        {
            int id = _languageRepository.GetIdByCode(code);
            UpdateSelectedLanguageId(id);
        }

        public int GetDefaultLanguageId()
        {
            return GetLanguageIdByParameterName( "default_language" );
        }
        public string GetDefaultLanguageCode()
        {
            int id = GetDefaultLanguageId();
            return _languageRepository.GetCodeById(id);
        }
        public int GetSystemLanguageId()
        {
            return GetLanguageIdByParameterName( "system_language" );
        }
        public string GetSystemLanguageCode()
        {
            return SystemLanguage.GetCode();
        }

        public void EstablishDefaultLanguage()
        {
            UpdateSelectedLanguageId(GetDefaultLanguageId());
        }
        public void EstablishSystemLanguage()
        {
            UpdateSelectedLanguageId(GetSystemLanguageId());
        }
    }
}