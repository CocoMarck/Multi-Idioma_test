namespace Core.Common {
    public static class TextualDateTime
    {
        public const string FORMAT = "yyyy-MM-ddTHH:mm:ss";

        public static string ToText(DateTime dateTime)
        {
            return dateTime.ToUniversalTime().ToString(FORMAT);
        }

        public static DateTime FromText(string text)
        {
            return DateTime.SpecifyKind(
                DateTime.ParseExact(text, FORMAT, null),
                DateTimeKind.Utc
            );
        }
    }
}