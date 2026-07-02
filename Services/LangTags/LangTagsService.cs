// Repositories
using Repositories.LangTags;

namespace Services.LangTags
{
    public class LangTagsService
    {
        // Variables
        private LanguageRepository _languageRepository;
        private TagRepository _tagRepository;
        private TranslationRepository _translationRepository;
        private SettingRepository _settingRepository;

        // Constructor
        public LangTagsService(
            LanguageRepository languageRepository, TagRepository tagRepository, TranslationRepository translationRepository, SettingRepository settingRepository)
        {
            _languageRepository = languageRepository;
            _tagRepository = tagRepository;
            _translationRepository = translationRepository;
            _settingRepository = settingRepository;
        }

        // Methods helpers
        private string GetSelectedLanguageFixedCode()
        {
            int id = _settingRepository.GetSelectedLanguageId();
            bool exists = _languageRepository.ExistsById(id);
            if (exists)
            {
                return _languageRepository.GetCodeById(id);
            }
            else if (id == _settingRepository.GetSystemLanguageId())
            {
                // Obtener code de lenguaje del sistema, o si existe el default.
                string systemCode = _settingRepository.GetSystemLanguageCode();

                if (_languageRepository.ExistsByCode(systemCode))
                {
                    return systemCode;
                }
                return _settingRepository.GetDefaultLanguageCode();
            }
            else
            {
                return _settingRepository.GetDefaultLanguageCode();
            }
        }

        // Methods principales
        public string GetText(string name, string code=null)
        {
            // Si no existe code, poner el default
            bool existsCode = false;
            if (code is string)
            {
                existsCode = _languageRepository.ExistsByCode(code);
            }
            if (!existsCode)
            {
                // Aca se usa settings para obtener el default.
                code = GetSelectedLanguageFixedCode();
                existsCode = _languageRepository.ExistsByCode(code);
            }
            // Si no existe tag devolver texto crudo.
            bool existsTag = _tagRepository.ExistsByName(name);
            string text = name;
            bool existsTranslation = false;
            if (existsTag && existsCode)
            {
                existsTranslation = 
                    _translationRepository.ExistsByTagNameAndLanguageCode(name, code);
            }
            if (existsTranslation)
            {
                // Aca se hace log por si falla.
                text = _translationRepository.GetValueByTagNameAndLanguageCode(name, code);   
            }
            return text;
        }
    }
}