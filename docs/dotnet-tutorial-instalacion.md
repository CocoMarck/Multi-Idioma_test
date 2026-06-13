# Guía de Instalación y Compilación de .NET (CLI Puro)

Este documento detalla cómo instalar el SDK de .NET sin depender de Visual Studio, tanto en **Windows** como en **Debian**, y cómo gestionar el ciclo de vida del proyecto desde la terminal usando `dotnet CLI`.

---

##  1. Instalación del SDK (.NET 8.0 o superior)

### En Windows (Vía PowerShell o CMD)
Para mantenerlo limpio y sin instaladores pesados, se recomienda usar el backend oficial de Microsoft a través de un script o usar el gestor de paquetes de Windows (`winget`).

**Opción A: Usando WinGet (Recomendado)**
Abre una terminal (PowerShell o CMD) como Administrador y ejecuta:
```bash
winget install Microsoft.DotNet.SDK.8
```

**Opción B: Instalación Manual por Script (PowerShell)**

Si no tienes WinGet, puedes descargar y ejecutar el script oficial de despliegue:
```powershell
Invoke-WebRequest -Uri [https://dot.net/v1/dotnet-install.ps1](https://dot.net/v1/dotnet-install.ps1) -OutFile dotnet-install.ps1
./dotnet-install.ps1 -Channel 8.0
```

### En Debian (12 / 13)

En Debian es sumamente directo ya que los paquetes están incluidos en los repositorios oficiales de Microsoft o nativos dependiendo de tu versión.

Abre tu terminal y ejecuta los siguientes comandos como root o usando sudo:
```bash
# 1. Actualizar el índice de paquetes
sudo apt update

# 2. Instalar las dependencias necesarias y el SDK de .NET 8
sudo apt install -y dotnet-sdk-8.0
```

---
## 2. Verificación de la Instalación

Sin importar el sistema operativo, abre una nueva terminal y ejecuta el siguiente comando para comprobar que el CLI está listo y en el PATH:
```bash
dotnet --version
```
> Debería retornar el número de versión exacto (ej. 8.0.301).

---
## 3. Comandos de Compilación y Flujo de Trabajo
Al usar Avalonia UI e independencia de IDEs, todo el proyecto se gestiona con estos comandos nativos desde la raíz del directorio donde se encuentra el archivo de proyecto (`.csproj`):

**Restaurar Dependencias**

Descarga los paquetes NuGet necesarios (como `Microsoft.Data.Sqlite` y las librerías de Avalonia):
```bash
dotnet restore
```

**Compilar el Proyecto**

Compila el código fuente en modo de depuración (Debug) sin ejecutarlo:
```bash
dotnet build
```

**Ejecutar aplicación**
```bash
dotnet run
```

**Publicación de Producción (Generar el Binario Limpio)**

Para generar el ejecutable final optimizado, limpio y autocontenido (sin que el usuario final necesite tener .NET instalado), usa el comando publish:

Para Windows (Genera un `.exe` único):
```powershell
dotnet publish -c Release -r win-x64 --self-contained true /p:PublishSingleFile=true /p:PublishReadyToRun=true
```

Para Linux / Debian (Genera un binario nativo ejecutable):
```bash
dotnet publish -c Release -r linux-x64 --self-contained true /p:PublishSingleFile=true
```

Los binarios resultantes se guardarán listos para producción en la ruta interna: `bin/Release/net8.0/[rid]/publish/`
