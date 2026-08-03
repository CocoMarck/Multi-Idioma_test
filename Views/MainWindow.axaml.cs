// Avalonia
using Avalonia.Controls; // Window
using Views.Forms;

namespace Views {
    public partial class MainWindow : Window {
        
        // Constructor
        public MainWindow() {
            InitializeComponent();
            LanguagesTab.Content = new Languages(App.LanguageController);
            TagsTab.Content = new Tags(App.TagController);
            RefreshText();
        }

        private string GetText(string text, string code=null) =>
            App.LangTagsService.GetText(text, code);

        // Methods
        private void RefreshText()
        {
            LanguagesTab.Header = GetText("Languages");
            TagsTab.Header = GetText("Tags");
            TranslationsTab.Header = GetText("Translations");
            SettingsTab.Header = GetText("Settings");
            GetTextTab.Header = GetText("Get text");
        }
    }
}
