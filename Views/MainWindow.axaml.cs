// Avalonia
using Avalonia.Controls; // Window

// Service
using Services.LangTags;

namespace Views {
    public partial class MainWindow : Window {
        public MainWindow(LangTagsService langTagsService) {
            InitializeComponent();
            LanguagesTab.Header = langTagsService.GetText("Languages");
            TagsTab.Header = langTagsService.GetText("Tags");
            TranslationsTab.Header = langTagsService.GetText("Translations");
            SettingsTab.Header = langTagsService.GetText("Settings");
            GetTextTab.Header = langTagsService.GetText("Get text");
        }
    }
}
