# folder_mapper_final.py
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import threading

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)

    def show(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        label = ttk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()

class EnhancedFolderMapper:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Mapper Pro")
        self.root.geometry("720x480")
        self.setup_styles()
        self.create_ui()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Colores corporativos
        self.style.configure("Primary.TFrame", background="#2B579A")
        self.style.configure("Secondary.TFrame", background="#FFFFFF")
        self.style.map("Primary.TButton",
            foreground=[("active", "white"), ("!active", "white")],
            background=[("active", "#1C3D6B"), ("!active", "#2B579A")])
        
        # Configuración de widgets
        self.style.configure("Primary.TButton", 
            font=("Segoe UI", 10), 
            borderwidth=0, 
            focusthickness=0,
            focuscolor="none",
            relief="flat",
            padding=6,
            bordercolor="#2B579A",
            anchor="center")
        
        self.style.configure("TEntry", 
            fieldbackground="white",
            bordercolor="#E1E1E1",
            lightcolor="#E1E1E1",
            darkcolor="#E1E1E1",
            padding=5)
        
        self.style.map("TEntry",
            bordercolor=[("focus", "#2B579A"), ("!focus", "#E1E1E1")])
            
    def create_ui(self):
        # Header
        header_frame = ttk.Frame(self.root, style="Primary.TFrame")
        header_frame.pack(fill=tk.X)
        
        ttk.Label(header_frame, 
                text="Document Mapper Pro", 
                font=("Segoe UI Semibold", 16), 
                foreground="white",
                background="#2B579A").pack(side=tk.LEFT, padx=20, pady=12)
        
        # Botón de ayuda
        help_btn = ttk.Button(header_frame, 
                            text="?", 
                            command=self.show_help,
                            style="Primary.TButton",
                            width=2)
        help_btn.pack(side=tk.RIGHT, padx=20)
        Tooltip(help_btn, "Ayuda de la aplicación\nCreado por: J. Gabriel Calderón")
        
        # Contenido principal
        main_frame = ttk.Frame(self.root, style="Secondary.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Campos de entrada
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, 
                text="CARPETA A ANALIZAR:", 
                font=("Segoe UI", 9, "bold"), 
                foreground="#2B579A").pack(anchor=tk.W)
                
        self.folder_path = tk.StringVar()
        folder_entry = ttk.Entry(input_frame, 
                               textvariable=self.folder_path, 
                               font=("Segoe UI", 10),
                               state="readonly",
                               width=50)
        folder_entry.pack(side=tk.LEFT, pady=5)
        Tooltip(folder_entry, "Selecciona la carpeta que deseas analizar")
        
        ttk.Button(input_frame, 
                 text="EXAMINAR", 
                 style="Primary.TButton",
                 command=self.select_folder).pack(side=tk.LEFT, padx=10)
        
        # Archivo de salida
        ttk.Label(main_frame, 
                 text="ARCHIVO DE SALIDA:", 
                 font=("Segoe UI", 9, "bold"), 
                 foreground="#2B579A").pack(anchor=tk.W, pady=(15,0))
                 
        self.output_path = tk.StringVar()
        output_entry = ttk.Entry(main_frame, 
                                textvariable=self.output_path, 
                                font=("Segoe UI", 10))
        output_entry.pack(fill=tk.X, pady=5)
        Tooltip(output_entry, "Ruta completa del archivo de salida (ej: C:/carpeta/estructura.txt)")
        
        ttk.Button(main_frame, 
                 text="ELEGIR RUTA", 
                 style="Primary.TButton",
                 command=self.select_output_path).pack(pady=5)
        
        # Botón principal
        self.generate_btn = ttk.Button(main_frame, 
                                     text="GENERAR MAPA DE ESTRUCTURA", 
                                     style="Primary.TButton",
                                     command=self.start_mapping)
        self.generate_btn.pack(pady=20)
        
        # Estado
        self.status_label = ttk.Label(main_frame, 
                                    text="", 
                                    font=("Segoe UI", 9),
                                    anchor=tk.CENTER)
        self.status_label.pack(fill=tk.X)
        
    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
            # Establecer ruta predeterminada de salida
            default_name = f"{os.path.basename(folder)}-estructura.txt"
            self.output_path.set(os.path.join(folder, default_name))
    
    def select_output_path(self):
        initial_dir = os.path.dirname(self.output_path.get()) if self.output_path.get() else os.getcwd()
        initial_file = os.path.basename(self.output_path.get()) if self.output_path.get() else "estructura-carpetas.txt"
        
        path = filedialog.asksaveasfilename(
            title="Guardar estructura como",
            defaultextension=".txt",
            initialfile=initial_file,
            initialdir=initial_dir,
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if path:
            self.output_path.set(path)
    
    def start_mapping(self):
        if not self.folder_path.get():
            self.show_status("¡Selecciona una carpeta primero!", "#D83B01")
            return
        
        threading.Thread(target=self.generate_structure, daemon=True).start()
        self.generate_btn.config(state=tk.DISABLED)
        
    def generate_structure(self):
        try:
            estructura = self.mapear_estructura(self.folder_path.get())
            output_path = self.output_path.get()
            
            # Crear directorios si no existen
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, "w", encoding="utf-8") as f:
                header = f"ESTRUCTURA DE CARPETAS\n{'='*25}\n"
                f.write(header + f"Ruta: {self.folder_path.get()}\nFecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n{estructura}")
            
            self.show_status(f"Archivo generado: {output_path}", "#00B050")
        except Exception as e:
            self.show_status(f"Error: {str(e)}", "#D83B01")
        finally:
            self.root.after(0, lambda: self.generate_btn.config(state=tk.NORMAL))
    
    def mapear_estructura(self, dir_path, prefix="", depth=0):
        try:
            items = sorted(os.listdir(dir_path))
            dirs, files = [], []
            
            for item in items:
                full_path = os.path.join(dir_path, item)
                if os.path.isdir(full_path):
                    dirs.append(item)
                else:
                    files.append(item)
            
            result = []
            for i, dir in enumerate(dirs):
                is_last = i == len(dirs)-1 and not files
                line = "└── " if is_last else "├── "
                next_prefix = "    " if is_last else "│   "
                
                result.append(f"{prefix}{line}📁 {dir}")
                full_path = os.path.join(dir_path, dir)
                result.append(self.mapear_estructura(full_path, prefix + next_prefix, depth + 1))
            
            for i, file in enumerate(files):
                line = "└── " if i == len(files)-1 else "├── "
                result.append(f"{prefix}{line}📄 {file}")
            
            return "\n".join(result)
        
        except Exception as e:
            return f"{prefix}[Error: {str(e)}]"
    
    def show_status(self, message, color):
        self.status_label.config(text=message, foreground=color)
        self.root.after(5000, lambda: self.status_label.config(text=""))
        
    def show_help(self):
        help_text = """Document Mapper Pro v1.0

Función:
Genera un mapa detallado de la estructura de carpetas y archivos en formato TXT.

Instrucciones:
1. Seleccionar carpeta con el botón EXAMINAR
2. Elegir ruta de salida con el botón ELEGIR RUTA
3. Generar el archivo con el botón principal

Elementos:
- Campo superior: Muestra la ruta seleccionada
- Archivo de salida: Ruta completa del reporte generado
- Estado: Mensajes temporales de éxito/error

Desarrollado por: J. Gabriel Calderón"""
        messagebox.showinfo("Ayuda del Sistema", help_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedFolderMapper(root)
    root.mainloop()
