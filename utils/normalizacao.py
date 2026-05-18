import re
import unicodedata


def normalizar_texto(texto):
    texto = texto.lower()

    texto = re.sub(r"\s+", " ", texto)

    texto = texto.strip()

    texto_sem_acentos = "".join(
        char for char in unicodedata.normalize("NFD", texto)
        if unicodedata.category(char) != "Mn"
    )

    return texto_sem_acentos