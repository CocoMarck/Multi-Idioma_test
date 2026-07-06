using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Services.LangTags;

namespace Views {
    public class App : Application {
        public static LangTagsService LangTagsService { get; set; }
        public override void OnFrameworkInitializationCompleted() {
            if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop) {
                desktop.MainWindow = new MainWindow();
            }
            base.OnFrameworkInitializationCompleted();
        }
    }
}
