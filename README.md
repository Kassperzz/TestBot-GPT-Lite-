<h1 align="center">🤖 TestBot-GPT (Lite)</h1>
<p align="center">
  <em>Generador local de pruebas unitarias impulsado por IA — 100 % offline, sin API keys</em><br>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python"/>
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit"/>
  <img src="https://img.shields.io/badge/Model-Ollama%20%7C%20Deepseek%20Coder-green"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow"/>
</p>

---

## 🧠 ¿Qué es TestBot-GPT?

**TestBot-GPT** es una herramienta *open-source* que genera **pruebas unitarias automáticas** a partir de código fuente usando modelos locales de **Ollama**.  
Funciona completamente **offline**, sin necesidad de claves de API ni conexión a Internet.

💡 Esta versión **Lite** está pensada para proyectos **pequeños o medianos**, ideales para:
- Estudiantes que están aprendiendo testing.  
- Testers que desean generar casos de prueba rápidamente.  
- Desarrolladores que buscan una herramienta ligera y privada.

> ⚠️ Para proyectos grandes (como apps Android o frameworks completos), se recomienda analizar por módulos o carpetas.

---

## ✨ Características

✅ Genera pruebas unitarias para **Python** o **JavaScript**  
✅ Acepta entrada manual o proyectos `.zip`  
✅ Funciona **100 % offline** con modelos locales (Deepseek, Llama, Mistral, etc.)  
✅ Filtra automáticamente los archivos fuente y evita binarios  
✅ Barra de progreso interactiva durante el análisis  
✅ Interfaz rápida e intuitiva desarrollada en **Streamlit**

---

## ⚙️ Requisitos

Antes de comenzar asegúrate de tener instalado:

### 🐍 Python

1. Descarga **Python 3.10 o 3.11** desde  
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Durante la instalación marca:
   ```
   ☑ Add Python to PATH  
   ☑ Install for all users
   ```
3. Verifica la instalación:
   ```bash
   python --version
   ```
   Debe mostrar algo como:
   ```
   Python 3.10.11
   ```

---

### 🧠 Ollama

TestBot-GPT usa **Ollama** para ejecutar modelos de lenguaje IA de forma local.

1. Descarga Ollama:  
   👉 [https://ollama.ai/download](https://ollama.ai/download)
2. Instálalo y prueba que funcione:
   ```bash
   ollama run llama3.2
   ```
   *(Deberías ver que el modelo responde.)*
3. Instala los modelos recomendados:
   ```bash
   ollama pull deepseek-coder:1.3b
   ollama pull llama3.2:1b
   ```

---

## 📦 Instalación del proyecto

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/<tu-usuario>/TestBot-GPT.git
   cd TestBot-GPT
   ```

2. **Crear un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Linux / Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## ▶️ Ejecución

Ejecuta el siguiente comando dentro de la carpeta del proyecto:

```bash
streamlit run app_lite.py
```

Se abrirá automáticamente tu navegador en:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 💻 Uso

### 🧾 Opción 1: Texto manual
1. Pega tu código o descripción directamente en el cuadro de texto.  
2. Haz clic en **🚀 Generar pruebas (texto manual)**.  
3. Espera unos segundos mientras la IA analiza y genera las pruebas.

---

### 📦 Opción 2: Proyecto ZIP
1. Sube un `.zip` con tu proyecto (máx. ≈ 300 KB de código fuente).  
2. TestBot-GPT analizará automáticamente los archivos relevantes (`.py`, `.js`, `.java`, `.ts`).  
3. Verás una barra de progreso con el análisis del proyecto.  
4. Se mostrarán las pruebas generadas en pantalla.

> ⚠️ *Esta versión Lite está pensada para proyectos pequeños o medianos.*  
> Si tu repositorio es grande, sube partes específicas (por ejemplo: `utils.zip` o `controllers.zip`).

---

### 💡 Ejemplo de salida:

```python
import unittest
from main import sumar

class TestSumar(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
```

---

## 🧩 Estructura del proyecto

```
TestBot-GPT/
├── app_lite.py              # Interfaz principal
├── requirements.txt         # Dependencias básicas
├── utils/
│   ├── file_handler.py      # Lectura y manejo de archivos ZIP
│   ├── test_generator.py    # Comunicación con Ollama
│   └── report_formatter.py  # Limpieza y formato del output
└── README.md
```

---

## 🧰 Archivos ignorados (.gitignore)

Estos archivos se generan automáticamente y **no deben subirse al repositorio**:

```
venv/
temp_project/
__pycache__/
*.pyc
*.zip
.DS_Store
Thumbs.db
```

---

## 💬 Retroalimentación

Si pruebas **TestBot-GPT**, tus sugerencias son muy bienvenidas 💡  
Puedes:
- Crear un **Issue** en GitHub para reportar errores 🐞  
- Sugerir mejoras (exportar a PDF/JSON, soporte multilenguaje, interfaz Pro)  
- Hacer un **Pull Request** con tus contribuciones 🚀

---

## 🛣️ Próximas versiones

🧩 **TestBot-GPT Pro** *(en desarrollo)*:  
- Procesamiento incremental para proyectos grandes.  
- Exportación de reportes en **PDF / JSON**.  
- Historial de ejecuciones por sesión.  
- Selector de modelo IA (GPT / Ollama).  
- Comparador de resultados entre modelos.  

---

## 📜 Licencia

Distribuido bajo licencia **MIT**.  
Hecho por **Kasperzzz**  
> v1.2 – TestBot-GPT (Lite)
