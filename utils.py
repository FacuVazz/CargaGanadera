# utils.py

def validar_numero(valor_str):
    """
    Intenta convertir un string a float. Si falla, devuelve None.
    """
    try:
        return float(valor_str)
    except ValueError:
        return None

def validar_entero(valor_str):
    """
    Intenta convertir un string a int. Si falla, devuelve None.
    """
    try:
        return int(valor_str)
    except ValueError:
        return None

def formato_kg(valor):
    """
    Devuelve un string con el valor numérico formateado como kilogramos.
    """
    return f"{valor:,.2f} kg"

def formato_toneladas(valor):
    """
    Convierte kilogramos a toneladas y devuelve el string formateado.
    """
    toneladas = valor / 1000
    return f"{toneladas:,.2f} toneladas"

def pausar():
    """
    Pausa la ejecución para que el usuario vea los resultados antes de salir.
    Útil si el script se ejecuta haciendo doble clic.
    """
    input("\nPresioná ENTER para finalizar...")
