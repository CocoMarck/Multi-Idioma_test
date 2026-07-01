using System;
using System.Text;

namespace Utils.Text
{
    public static class TextFormat
    {
        public static bool TryReadDouble(string text, out double value)
        {
            text = (text ?? "").Trim();

            if (double.TryParse(text, System.Globalization.NumberStyles.Float,
                                System.Globalization.CultureInfo.CurrentCulture, out value))
                return true;

            if (double.TryParse(text, System.Globalization.NumberStyles.Float,
                                System.Globalization.CultureInfo.InvariantCulture, out value))
                return true;

            text = text.Replace(',', '.');

            return double.TryParse(text, System.Globalization.NumberStyles.Float,
                                   System.Globalization.CultureInfo.InvariantCulture, out value);
        }

        public static double ReadDouble(string text, double defaultValue = 0.0)
        {
            double value;
            return TryReadDouble(text, out value) ? value : defaultValue;
        }

        public static string FormatDouble(double value)
        {
            if (double.IsNaN(value) || double.IsInfinity(value)) return "0.0";

            return value.ToString("0.#####",
                System.Globalization.CultureInfo.CurrentCulture);
        }

        public static string ToSnakeCase(string text)
        {
            string[] replaceChars = new string[] { " ", "-" };
            string newText = text.Trim().ToLower();
            foreach (string character in replaceChars)
            { 
                newText = newText.Replace(character, "_");
            }
            return newText;
        }

        public static string ToKebabCase(string text)
        {
            string[] replaceChars = new string[] { " ", "_" };
            string newText = text.Trim().ToLower();
            foreach (string character in replaceChars)
            { 
                newText = newText.Replace(character, "-");
            }
            return newText;
        }
    }
}