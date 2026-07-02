using System.Globalization;

namespace Core
{
    // Obtiene el ISO 639-1 del sistema operativo
    public static class SystemLanguage
    {
        public static string GetCode()
        {
            return CultureInfo.CurrentUICulture.TwoLetterISOLanguageName;
        }
    }
}