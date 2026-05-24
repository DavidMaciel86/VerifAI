from datetime import datetime

import validators
import whois
import tldextract

from config.security_rules import ENCURTADORES_SUSPEITOS


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


def consultar_whois(url):

    try:

        dominio = tldextract.extract(url)

        dominio_completo = f"{dominio.domain}.{dominio.suffix}"

        dados = whois.whois(dominio_completo)

        data_criacao = dados.get("creation_date")

        if isinstance(data_criacao, list):
            data_criacao = data_criacao[0]

        idade_dias = None

        if data_criacao:
            idade_dias = (datetime.now() - data_criacao).days

        return {
            "dominio": dominio_completo,
            "data_criacao": data_criacao,
            "idade_dias": idade_dias,
            "registrador": dados.get("registrar")
        }

    except Exception:

        return {
            "erro": "Não foi possível consultar WHOIS"
        }
