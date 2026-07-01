// Utils
using Utils.Text;

namespace Core.LangTags {
    public static class TagNameNormalizer {
        public static string Normalize(string text){
            string filteredText = text;
            string newText = TextFormat.ToKebabCase(filteredText);
            return newText;
        }
    }
}