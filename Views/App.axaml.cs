using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Controllers.LangTags;
using Services.LangTags;

namespace Views {
    public class App : Application {
        public static LangTagsService LangTagsService { get; set; }
        public static LanguageController LanguageController { get; set; }
        public static TagController TagController { get; set; }
        public static TranslationController TranslationController { get; set; }
        
        public override void OnFrameworkInitializationCompleted() {
            if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop) {
                desktop.MainWindow = new MainWindow();
            }
            base.OnFrameworkInitializationCompleted();
        }
    }
}
