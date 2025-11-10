def format_report(test_code: str) -> str:
    """
    Limpia y formatea el texto generado por la IA
    para mostrarlo correctamente en Streamlit.
    """
    if not test_code:
        return "⚠️ No se recibieron resultados del modelo."

    if "```" in test_code:
        test_code = test_code.replace("```python", "").replace("```", "")
    return test_code.strip()
