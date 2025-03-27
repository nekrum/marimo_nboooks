# Marimo NoteBoooks

Pruebas con marimo como remplazo de jupyter notebook

[!Note]: Cada proyecto tiene su propio ambiente, una vez descargado el
repositorio se puede instalar mediante [uv](https://docs.astral.sh/uv/)

Se necesita entonces:

1. Instalar Python
2. Instalar gestor de paquete UV (OPCIONAL)

## 1. Instalar Python

Para Linux y macOS (sistemas operativos alternativos a Windows). Python viene
instalado de facto. Es posible que necesitemos instalar una versión específica,
pero en general esto no debe ser un problema para cualquiera de estos
**notebooks**.

### Instalar Python Instalador Oficial (Windows)

1. **Descargar el instalador de Python:**
   - Visita el sitio web oficial de Python: [python.org](https://www.python.org/).
   - Dirígete a la sección de descargas y selecciona la última versión de Python para Windows.

2. **Ejecutar el instalador:**
   - Una vez descargado el archivo, haz doble clic en él para ejecutarlo.
   - Asegúrate de marcar la opción "Add Python to PATH" antes de continuar.

3. **Seleccionar la instalación personalizada:**
   - Elige "Customize installation" para tener más control sobre el proceso de instalación.
   - Asegúrate de que las opciones "pip" y "tcl/tk and IDLE" estén seleccionadas.

4. **Elegir el directorio de instalación:**
   - Puedes dejar el directorio predeterminado o seleccionar uno diferente según tus preferencias.

5. **Completar la instalación:**
   - Haz clic en "Install" para comenzar la instalación.
   - Una vez finalizada, cierra el instalador.

6. **Verificar la instalación:**
   - Abre la terminal de comandos (CMD) y escribe `python --version` para verificar que Python se haya instalado correctamente.


### Instalar con winget (WIndows)

Winget es un instalador de paquetes de línea de comandos que viene incluido en
WInows, y funciona bastante bien.

1. **Abrir la terminal de comandos:**
   - Presiona `Win + R`, escribe `cmd` y presiona `Enter` para abrir la terminal de comandos.

2. **Buscar Python en Winget:**
   - Escribe el siguiente comando para buscar Python en el repositorio de `winget`:

     ```
     winget search Python
     ```

3. **Instalar Python:**
   - Una vez que encuentres el paquete de Python, instala la última versión disponible usando el siguiente comando:

     ```
     winget install Python.Python.3
     ```

4. **Verificar la instalación:**
   - Después de la instalación, verifica que Python se haya instalado correctamente escribiendo:

     ```
     python --version
     ```

### Otros métodos

-  **Microsoft Store:**
   - Python está disponible en la Microsoft Store, lo que permite una instalación fácil y rápida. Simplemente abre la Microsoft Store, busca "Python" y selecciona la versión que deseas instalar. Este método es ideal para usuarios que prefieren una instalación sin complicaciones y que no necesitan configuraciones avanzadas.

-  **Anaconda:**
   - Anaconda es una distribución de Python que incluye una gran cantidad de paquetes científicos y de análisis de datos. Es especialmente útil para usuarios que planean usar Python para ciencia de datos o aprendizaje automático. Puedes descargar Anaconda desde su [sitio web oficial](https://www.anaconda.com/products/distribution).

-  **Chocolatey:**
   - Chocolatey es otro gestor de paquetes para Windows que permite instalar aplicaciones desde la línea de comandos. Para instalar Python usando Chocolatey, primero necesitas instalar Chocolatey y luego ejecutar el comando `choco install python`.

En lo personal la instalación de la Microsoft Store me ha dado problemas con el
path de los binarios y paquetes de **Python**. **Anaconda** es muy sencillo pero
es un instalador muy pesado y en ocasiones causa conflictos entre sus librerías.
Chocolatey, es un instalador excelente pero requiere instalar un software de
terceros.


## 2. Instalar gestor de paquetes UV    

**uv** es un instalador de paquetes muy rápido y disponible para Linux, macOS y
Windows. Esta creado en rust o y hace un gran trabajo al instalar
y mantener las dependencias del paquete.

[En la pagina del instalador](https://docs.astral.sh/uv/configuration/installer/)  
explican y proporcionan un comando que logra instalarlo en cuestion de minutos.

> [!NOTE] ¿Porque UV? es un manejador de paquetes muy rapido y es una
> alternativa robusta a  pip, el instalador base de Python. Ademas es mas
> rápido que Poetry, Hatch, PDM y Rye... y aunque no maneja también como pdm la
> creación de paquetes de python. Si que es buen remplazo para pip y pipenv.


### ATAJO para correr el Notebook

En este punto con UV instalado se puede correr de manera directa el **NoteBook**
solo tienes que crear un directorio o carpeta y dentro de ella abrit una
terminal de Winows, Linux o macOS. Dentro de la carpeta ejecutar los siguientes
comandos:

```bash

uv init # Inicia la carpeta creando un ambiente virtual
uv add marimo # Instala marimo 
uv run marimo --sandbox editor <URL raw del notebook>

```

Esto usara el notebok, lo abrira e instalará las dependencias necesarias. Si
decides ejectuar esta opción puedes saltarte a hasta la sección de comandos para
cada uno de los **Notebooks**.


>[!IMPORTANT]
> No es necesario instalar UV, se puede instalar **marimo** sin problema
> alguno con `pip install marimo`. Pero es recomendable **uv** ya que es el
> unico que usa sandobox e instala automáticamente las librerías necesarias para
> el notebook. Ademas usa por default ambientes de python.

## Método manual

En caso de quere seguir un método mas ortodoxo, necesitamos descargar el repositorio
y si queremos no usar UV, con solo instalar marimo con pip o cualquier otro
gestor podemo usar

```bash
marimo edit
```

En el directorio de cualquier análisis y el mismo notebook nos pedira instalar
los paquetes para lo que hara uso de pip de forma automática.


## Comando de ejecución de Notebook

-  Child Screen Time

```bash
uv run marimo editor --sandbox https://raw.githubusercontent.com/nekrum/marimo_nboooks/refs/heads/main/child_screen/ChildScreenTime.py
```
