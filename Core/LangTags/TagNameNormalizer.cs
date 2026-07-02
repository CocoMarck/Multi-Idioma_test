using System.Text.RegularExpressions;

// Utils
using Utils.Text;

namespace Core.LangTags {
    public static class TagNameNormalizer {
        public static string Normalize(string text){
            // Filtros
            string filteredText = text.Trim().ToLowerInvariant();

            // Filtro. Espacios múltiples a uno.
            filteredText = Regex.Replace(filteredText, @"\s+", " ");

            // Filtro. Quitar caracteres raros, dejando letras, números, espacio, _ y -.
            filteredText = Regex.Replace(filteredText, @"[^a-z0-9 _-]", "");
            
            // Texto final
            string newText = TextCase.ToKebabCase(filteredText);
            return newText;
        }
    }
}