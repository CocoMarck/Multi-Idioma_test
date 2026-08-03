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
using Controllers.LangTags;
using Entities.LangTags;

// Logger
using Microsoft.Extensions.Logging;


public static class Program {
    static void Main(string[] args){
        // Init
        var paths = new Paths();
        DatabaseContext dbContext = DatabaseInitializer.Initialize(paths);
        var langTagsService = new LangTagsService(
            dbContext.Language, dbContext.Tag, dbContext.Translation, dbContext.Setting);

        // Init logger
        using var loggerFactory = LoggerFactory.Create(builder => 
        {
            builder.AddConsole().SetMinimumLevel(LogLevel.Debug);
        });
        var languageEntity = new LanguageEntity();
        var tagEntity = new TagEntity();
        ILogger languageLogger = loggerFactory.CreateLogger<LanguageController>();
        ILogger tagLogger = loggerFactory.CreateLogger<TagController>();
        
        var languageController = new LanguageController( dbContext.Language, languageEntity, languageLogger);
        var tagController = new TagController( 
            dbContext.Tag, tagEntity, tagLogger 
        );

        // Debug
        Console.WriteLine(
            langTagsService.GetText("languages", "en") + "\n" +
            langTagsService.GetText("Tags", "es") + "\n" +
            langTagsService.GetText("TransLations") + "\n" +
            langTagsService.GetText("Settings", "en") + "\n" +
            langTagsService.GetText("Get TExt", "es")
        );

        // Build App
        App.LangTagsService = langTagsService;
        App.LanguageController = languageController;
        App.TagController = tagController;
        AppBuilder.Configure<App>()
            .UsePlatformDetect().StartWithClassicDesktopLifetime(args);
    }
    //
}
