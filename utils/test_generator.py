import requests
import json
from utils.file_handler import detect_project_language

def generate_tests(code_snippet: str, file_paths=None) -> str:
    """
    Envía el código o descripción al modelo local de Ollama
    y genera pruebas según el lenguaje dominante del proyecto.
    """

    MODEL = "deepseek-coder:1.3b"

    # Detección automática de lenguaje
    lang = "py"
    if file_paths:
        lang = detect_project_language(file_paths)
    else:
        # Heurística básica por texto
        if "import React" in code_snippet or "function(" in code_snippet:
            lang = "js"

    # Prompt adaptativo
    if lang == "py":
        prompt = f"""
Eres un experto en desarrollo y testing en Python.
Genera **solo código de pruebas unitarias en Python** usando unittest o pytest.
No incluyas explicaciones, solo código.

Código del proyecto:
{code_snippet}

Responde únicamente con el código Python de las pruebas.
"""
    elif lang == "js":
        prompt = f"""
Eres un experto en desarrollo y testing en JavaScript.
Genera **solo código de pruebas unitarias en JavaScript** usando Jest.
No incluyas explicaciones, solo código.

Código del proyecto:
{code_snippet}

Responde únicamente con el código JavaScript de las pruebas.
"""
    else:
        prompt = f"""
Eres un experto en testing.
Genera pruebas unitarias para el siguiente código, en el lenguaje adecuado.
Solo entrega código.
{code_snippet}
"""

    # Llamada al modelo
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": MODEL, "prompt": prompt},
        stream=True
    )

    if response.status_code != 200:
        raise Exception(f"Error al comunicarse con Ollama: {response.text}")

    output = []
    for line in response.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line.decode("utf-8"))
            if "response" in data:
                output.append(data["response"])
        except json.JSONDecodeError:
            continue

    return "".join(output).strip()
