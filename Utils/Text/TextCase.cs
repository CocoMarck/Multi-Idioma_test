using System;
using System.Text;

namespace Utils.Text
{
    public static class TextCase
    {
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