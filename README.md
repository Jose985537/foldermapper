# Folder Mapper

**Folder Mapper** es una aplicación de escritorio que te permite generar un archivo de texto con la estructura jerárquica de carpetas y archivos de cualquier directorio en tu sistema. Con una interfaz gráfica intuitiva y moderna, esta herramienta es ideal para documentar proyectos, analizar estructuras de archivos y mantener un registro organizado de tus directorios.

---

## Características Principales

- **Interfaz gráfica moderna:** Diseño profesional con colores corporativos y tipografía clara.
- **Selección de carpeta:** Elige cualquier carpeta de tu sistema para analizar su estructura.
- **Ruta de salida personalizable:** Guarda el archivo `.txt` en cualquier ubicación con el nombre que prefieras.
- **Formato claro:** Genera un archivo de texto con símbolos visuales (📁 para carpetas, 📄 para archivos) y estructura jerárquica.
- **Retroalimentación en tiempo real:** Mensajes de estado para éxito o errores.
- **Soporte multi-plataforma:** Funciona en Windows, macOS y Linux.
- **Versión ejecutable (.exe):** Disponible para Windows para un uso rápido sin necesidad de instalar Python.

---

## Instalación

### Requisitos Previos
- **Python 3.6 o superior** - [Descargar Python](https://www.python.org/downloads/) (solo si usas la versión de código fuente).

### Opción 1: Usar la Versión Ejecutable (.exe)

1. **Descarga el ejecutable:**
   - Ve a la sección de [Releases](https://github.com/Jose985537/foldermapper/releases) del repositorio.
   - Descarga el archivo `FolderMapper.exe`.

2. **Ejecuta la aplicación:**
   - Haz doble clic en `FolderMapper.exe` para iniciar la aplicación.
   - ¡No necesitas instalar Python ni dependencias adicionales!

### Opción 2: Usar la Versión de Código Fuente

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Jose985537/foldermapper.git
   cd foldermapper
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python folder_mapper_final.py
   ```

---

## Uso Rápido

1. **Selecciona una carpeta:**
   - Haz clic en "EXAMINAR" y elige la carpeta que deseas analizar.

2. **Elige la ruta de salida:**
   - Haz clic en "ELEGIR RUTA" para seleccionar la ubicación y nombre del archivo `.txt`.
   - Si no eliges una ruta, el archivo se guardará en la carpeta seleccionada con un nombre predeterminado.

3. **Genera el mapa:**
   - Haz clic en "GENERAR MAPA DE ESTRUCTURA".
   - El archivo `.txt` se generará en la ubicación especificada.

---

# Estructura del Proyecto

```
foldermapper/
├── folder_mapper.py   # Código principal de la aplicación
├── FolderMapper.exe         # Versión ejecutable para Windows
├── requirements.txt         # Dependencias necesarias
├── README.md                # Este archivo
```
---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

## Autor

- **J. Gabriel Calderón**  
  Desarrollador y mantenedor del proyecto.  
  GitHub: [Jose985537](https://github.com/Jose985537)  

---

## Agradecimientos

- A la comunidad de Python por las herramientas y librerías utilizadas.
- A los contribuidores y usuarios por sus sugerencias y reportes de errores.

---

¡Gracias por usar **Folder Mapper**! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en el repositorio. 😊# foldermapper
