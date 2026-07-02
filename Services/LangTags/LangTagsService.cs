using Repositories.LangTags;

namespace Services.LangTags
{
    public class LangTagsService
    {
        // Variables
        private LanguageRepository _languageRepository;
        private TagRepository _tagRepository;
        private TranslationRepository _translationRepository;

        // Constructor
        public LangTagsService(
            LanguageRepository languageRepository, TagRepository tagRepository, TranslationRepository translationRepository)
        {
            _languageRepository = languageRepository;
            _tagRepository = tagRepository;
            _translationRepository = translationRepository;
        }

        public string GetText(string name, string code=null)
        {
            // Si no existe code, poner el default
            bool existsCode = false;
            if (code is null)
            {
                existsCode = false;
            }
            else
            {
                existsCode = _languageRepository.ExistsByCode(code);
            }
            if (!existsCode)
            {
                code = "en";
            }
            // Si no existe tag devolver texto crudo.
            bool existsTag = _tagRepository.ExistsByName(name);
            string text = name;
            if (existsTag && existsCode)
            {
                // Aca se hace log por si falla.
                text = _translationRepository.GetValueByTagNameAndLanguageCode(
                    name, code);
            }
            return text;
        }
    }
}