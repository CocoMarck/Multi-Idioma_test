using System.Text.RegularExpressions;

namespace Core.LangTags {
    public static class LanguageCodeNormalizer {
        public static string Normalize(string code){
            // Normalizar para asegurar `ISO 639-1` o `ISO 639-2`
            // Sin espacios
            string cleaned = code.Trim().ToLowerInvariant();

            // Solo abc
            cleaned = Regex.Replace(cleaned, @"[^a-z]", "");

            // Asegurar solo tres letras o menos
            if (cleaned.Length >= 3) {
                return cleaned.Substring(0, 3);
            }
            else {
                return cleaned;
            }
        }
    
    }
}