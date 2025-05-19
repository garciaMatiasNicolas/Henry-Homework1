## 🧑‍💻 User Management App Terminal

Este proyecto es una aplicación de línea de comandos (CLI) escrita en Python que permite:

- Registrar nuevos usuarios  
- Listar todos los usuarios registrados  
- Eliminar usuarios por ID  
- Buscar usuarios por email  
- Guardar los datos en un archivo JSON

---

### 📁 Estructura del proyecto

```bash
project/
├── app/
│ ├── data/
│ │ └── users.json # Archivo donde se almacenan los usuarios
│ ├── utils/
│ │ └── utils.py # Funciones de lectura/escritura JSON
│ ├── users.py # Lógica de operaciones con usuarios
│ └── main.py # Menú principal (este archivo)
└── README.md


---

### ⚙️ Requisitos

- Python 3.7 o superior

---

### ▶️ Cómo ejecutarlo

1. Cloná o descargá el repositorio.  
2. Navegá al directorio donde se encuentra `main.py`.  
3. Ejecutá el menú principal con: python main.py
