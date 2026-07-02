namespace Utils.Text
{
    public static class TextNumber
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
    }
}