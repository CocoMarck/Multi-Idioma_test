// Avalonia
using Avalonia;

// Repositories
using Repositories.LangTags;

// Core
using Core.Sqlite;
using Core.LangTags;

// Services
using Services.LangTags;

// Config
using Config;

// Views
using Views;


public static class Program {
    static void Main(string[] args){
        // Init
        var paths = new Paths();
        DatabaseContext dbContext = DatabaseInitializer.Initialize(paths);
        var langTagsService = new LangTagsService(
            dbContext.Language, dbContext.Tag, dbContext.Translation, dbContext.Setting);

        Console.WriteLine(
            langTagsService.GetText("languages", "en") + "\n" +
            langTagsService.GetText("Tags", "es") + "\n" +
            langTagsService.GetText("TransLations") + "\n" +
            langTagsService.GetText("Settings", "en") + "\n" +
            langTagsService.GetText("Get TExt", "es")
        );

        // Build App
        App.LangTagsService = langTagsService;
        AppBuilder.Configure<App>()
            .UsePlatformDetect().StartWithClassicDesktopLifetime(args);
    }
    //
}
