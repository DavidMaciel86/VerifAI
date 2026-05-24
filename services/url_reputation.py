from config.security_rules import ENCURTADORES_SUSPEITOS
import validators
import tldextract


def validar_url(url):

    if not validators.url(url):
        return {
            "valida": False,
            "motivo": "URL inválida"
        }

    dominio = tldextract.extract(url)

    dominio_completo = f"{dominio.domain}.{dominio.suffix}"

    suspeita = dominio_completo in ENCURTADORES_SUSPEITOS

    return {
        "valida": True,
        "dominio": dominio_completo,
        "encurtador": suspeita
    }
