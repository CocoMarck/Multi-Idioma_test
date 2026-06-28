using static System.Console;
using System.IO;

namespace Utils {
    public class ResourceLoader {
        /*
        Establecer las rutas principales de trabajo.
        Rutas de trabajo: Config/, Resources/, Logs/, Data/, Docs/
        
        baseDir, sera la ruta principal/base.
        */
        
        public readonly string baseDir;
        public readonly string configDir;
        public readonly string logsDir;
        public readonly string dataDir;
        public readonly string docsDir;
        public readonly string resourceDir;
        
        // Constructor de atributos | Establecer directorios de trabajo
        public ResourceLoader() {
            baseDir = Path.GetFullPath("./");
            configDir = Path.Combine( baseDir, "Config" );
            logsDir = Path.Combine( baseDir, "Logs" );
            dataDir = Path.Combine( baseDir, "Data" );
            docsDir = Path.Combine( baseDir, "Docs" );
            resourceDir = Path.Combine( baseDir, "Resources" );
        }
        
        // Metodos
        // Determina si existen los archivos. 
        
        /// Establece si es un dir o un file, o si no existe
        public string? GetPathType( string path ) {
            if ( File.Exists(path) ){
                return "file";
            } else if ( Directory.Exists(path) ){
                return "dir";
            } else {
                return null;
            }
        }
        
        /// Determina si existe un archivo
        public bool ExistsPath( string path ){
            return ( GetPathType(path:path) is string );
        }
        
        public bool ExistsResource() {
            return Directory.Exists(resourceDir);
        }
        
        public bool ExistsConfig() {
            return Directory.Exists(configDir);
        }

        /// Combinar `dir` con `file` Restrictivo, lo generado teiene que existir.
        /*
        Tiene que ser directorio, combinado con file o dir. O si no, no jala.
        */
        public string? RestrictiveCombineFile( string directory, string file) {
            string? final_path = null;
            if ( GetPathType(directory) == "dir" ) {
                final_path = Path.Combine( directory, file );
                if ( ExistsPath( final_path ) == false ){
                    final_path = null;
                }
            }
            return final_path;
        }

        // Combinar `Dir`, con `File` o `Dir`. Lo generado, no necesariamente tiene que exister.
        public string? CombineResourceFile(string file) {
            return Path.Combine( resourceDir, file );
        } 
        
        public string CombineConfigFile(string file) {
            return Path.Combine( configDir, file );
        }
        
        public string CombineLogFile(string file) {
            return Path.Combine( logsDir, file );
        }
        //
        public Dictionary<string, List<string>> GetRecursiveFiles(string directory, string pattern = "*")
        {
            // Diccionario de dirs y files encontrados.
            var dict = new Dictionary<string, List<string>>()
            {
                ["file"] = new List<string>(),
                ["dir"] = new List<string>()
            };

            List<string> files = Directory.GetFiles(
                directory, pattern, SearchOption.AllDirectories).ToList();
            foreach (string file in files)
            {
                dict["file"].Add(file);
            }
            List<string> dirs = Directory.GetDirectories(
                directory, "*", SearchOption.AllDirectories).ToList();
            foreach (string dir in dirs)
            {
                dict["dir"].Add(dir);
            }
            return dict;
        }
        //
    }
}
