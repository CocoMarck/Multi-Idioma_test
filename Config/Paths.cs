// csharp
using static System.Console;
using System.IO;

// cm
using Utils;

namespace Config {
    public class Paths{
        public readonly string DATA_DIR;
        public readonly string CONFIG_DIR;
        public readonly string SCHEMAS_DIR;
        public readonly List<string> SCHEMAS_FILES;
        public ResourceLoader resourceLoader;

        public Paths() {
            resourceLoader = new ResourceLoader();

            DATA_DIR = resourceLoader.dataDir;
            CONFIG_DIR = resourceLoader.configDir;
            SCHEMAS_DIR = Path.Combine( resourceLoader.baseDir, "Schemas", "LangTags" );

            Dictionary<string, List<string>> schemasDictFiles = resourceLoader.GetRecursiveFiles(
                SCHEMAS_DIR);
            SCHEMAS_FILES = schemasDictFiles["file"];
        }
        //
    }
}
