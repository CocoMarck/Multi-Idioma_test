using Core.Sqlite;
using Config;
using Repositories.LangTags;

namespace Core.LangTags {
    public class DatabaseContext {
        public LanguageRepository Language { get; init; }
        public TagRepository Tag { get; init; }
        public TranslationRepository Translation { get; init; }
        public SettingRepository Setting { get; init; }
    }

    public static class DatabaseInitializer {
        public static DatabaseContext Initialize(Paths paths) 
        {
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

            // Init repos
            var languageRepository = new LanguageRepository(db);
            var tagRepository = new TagRepository(db);
            var translationRepository = new TranslationRepository(
                db, tagRepository, languageRepository);
            var settingRepository = new SettingRepository(db, languageRepository);

            // Return context
            var databaseContext = new DatabaseContext{
                Language = languageRepository,
                Tag = tagRepository,
                Translation = translationRepository,
                Setting = settingRepository
            };

            // Repos save first values
            SaveFirstValues( databaseContext );
            
            return databaseContext;
        }
        
        private static void SaveFirstValues(DatabaseContext databaseContext)
        {
            var languageRepository = databaseContext.Language;
            var tagRepository = databaseContext.Tag;
            var translationRepository = databaseContext.Translation;
            var settingRepository = databaseContext.Setting;

            languageRepository.Save("en", true);
            languageRepository.Save("es", true);
            languageRepository.Save("pt", false);
            languageRepository.Save("ru", true);
            languageRepository.Deactivate(4);
            Console.WriteLine( languageRepository.Table.CountRows() );

            tagRepository.Save("languages", true);
            tagRepository.Save("tags", true);
            tagRepository.Save("translations", true);
            tagRepository.Save("settings", true);
            tagRepository.Save("get-text", true);
            Console.WriteLine( tagRepository.Table.CountRows() );

            settingRepository.InitParameters();
            //settingRepository.UpdateSelectedLanguageCode("es");
            //settingRepository.EstablishDefaultLanguage();
            settingRepository.EstablishSystemLanguage();
            Console.WriteLine( settingRepository.GetDefaultLanguageCode() );
            Console.WriteLine( settingRepository.GetSelectedLanguageCode() );
            Console.WriteLine( settingRepository.GetSystemLanguageId() );
            Console.WriteLine( settingRepository.Table.CountRows() );
            
            translationRepository.SaveByTagNameAndLanguageCode(
                "languages", "en", "Languages");
            translationRepository.SaveByTagNameAndLanguageCode(
                "languages", "es", "Lenguajes");
            
            translationRepository.SaveByTagNameAndLanguageCode(
                "tags", "en", "Tags");
            translationRepository.SaveByTagNameAndLanguageCode(
                "tags", "es", "Etiquetas");
            
            translationRepository.SaveByTagNameAndLanguageCode(
                "translations", "en", "Translations");
            translationRepository.SaveByTagNameAndLanguageCode(
                "translations", "es", "Traducciones");
            
            translationRepository.SaveByTagNameAndLanguageCode(
                "settings", "en", "Settings");
            translationRepository.SaveByTagNameAndLanguageCode(
                "settings", "es", "Ajustes");

            translationRepository.SaveByTagNameAndLanguageCode(
                "get-text", "en", "Get text");
            translationRepository.SaveByTagNameAndLanguageCode(
                "get-text", "es", "Obtener texto");
            
            Console.WriteLine( translationRepository.Table.CountRows() );
        }
    }
}