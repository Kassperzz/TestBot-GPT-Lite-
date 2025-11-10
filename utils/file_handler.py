import zipfile
import io
import os
import streamlit as st

def extract_zip(uploaded_file, extract_to="temp_project"):
    """Extrae el archivo .zip en una carpeta temporal."""
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    else:
        # Limpia carpeta anterior
        for f in os.listdir(extract_to):
            path = os.path.join(extract_to, f)
            try:
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    import shutil
                    shutil.rmtree(path, ignore_errors=True)
            except Exception:
                pass

    with zipfile.ZipFile(io.BytesIO(uploaded_file.read()), 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    return extract_to


def collect_source_files(folder):
    """Recorre el proyecto y obtiene rutas de archivos fuente (excluye binarios y carpetas pesadas)."""
    source_files = []
    valid_exts = (".py", ".js", ".java", ".kt", ".ts")
    skip_dirs = ("build", "gradle", "node_modules", "ios", "android", "venv", "__pycache__")

    for root, dirs, files in os.walk(folder):
        # Evita carpetas pesadas o irrelevantes
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for f in files:
            if f.endswith(valid_exts):
                source_files.append(os.path.join(root, f))
    return source_files


def read_files(file_paths, limit_kb=300):
    """
    Lee y concatena los archivos seleccionados hasta un límite de tamaño total.
    Incluye barra de progreso para mostrar avance del análisis.
    """
    contents = []
    total_size = 0
    max_size = limit_kb
    progress = st.progress(0, text="📖 Analizando archivos del proyecto...")
    total_files = len(file_paths)
    processed = 0

    for path in file_paths:
        processed += 1
        size_kb = os.path.getsize(path) / 1024
        if total_size + size_kb > max_size:
            break

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                contents.append(f"\n# Archivo: {os.path.basename(path)}\n" + f.read())
            total_size += size_kb
        except Exception:
            continue

        # Actualiza la barra de progreso
        percent = int((processed / total_files) * 100)
        progress.progress(percent, text=f"📂 Procesando archivo {processed}/{total_files} ({percent}%)")

    progress.empty()
    st.success(f"✅ Archivos analizados: {processed} de {total_files} — Total leído: {int(total_size)} KB")
    return "\n".join(contents)


def detect_project_language(file_paths):
    """Detecta el lenguaje principal del proyecto según extensiones."""
    ext_count = {"py": 0, "js": 0, "java": 0, "kt": 0, "ts": 0}
    for path in file_paths:
        if path.endswith(".py"): ext_count["py"] += 1
        elif path.endswith(".js") or path.endswith(".jsx"): ext_count["js"] += 1
        elif path.endswith(".java"): ext_count["java"] += 1
        elif path.endswith(".kt"): ext_count["kt"] += 1
        elif path.endswith(".ts"): ext_count["ts"] += 1

    # Retorna el lenguaje con más archivos
    return max(ext_count, key=ext_count.get)
