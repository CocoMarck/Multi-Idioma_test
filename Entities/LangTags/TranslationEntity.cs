namespace Entities.LangTags {
    public class TranslationEntity : Entities.LangTags.ControlFields {
        public int TranslationId { get; protected set; }
        public int TagId { get; protected set; }
        public int LanguageId { get; protected set; }
        public string Value { get; protected set; }
    }
}