import re

def generate_search_field(text):
    """
    Genera el campo 'search' a partir del texto proporcionado.
    Se eliminan los espacios en blanco al principio y al final del texto,
    se convierte a minúsculas, se reemplazan los caracteres acentuados por sus equivalentes sin acento,
    y se reemplazan los espacios por guiones bajos.
    """
    text = text.lower()
    text = text.strip()
    text = text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n')
    
    return text

