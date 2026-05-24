import re
from utils.normalizacao import normalizar_texto
from urllib.parse import urlparse
from services.url_reputation import (
    validar_url,
    consultar_whois
)

from utils.regex_patterns import (
    REGEX_LINKS,
    REGEX_EMAILS,
    REGEX_TELEFONES
)

from core.score import (
    classificar_risco,
    somar_scores
)


from config.security_rules import (
    PALAVRAS_SUSPEITAS,
    PADROES_ENGENHARIA_SOCIAL,
    DOMINIOS_SUSPEITOS
)


def detectar_links(texto):
    return re.findall(REGEX_LINKS, texto)


def detectar_emails(texto):
    return re.findall(REGEX_EMAILS, texto)


def detectar_telefones(texto):
    return re.findall(REGEX_TELEFONES, texto)


def analisar_dominios(links):
    dominios = []

    for link in links:
        if not link.startswith("http"):
            link = "https://" + link

        dominio = urlparse(link).netloc
        dominios.append(dominio)

    return dominios


def analisar_texto(texto):
    motivos = []

    score_texto = 0
    score_links = 0
    score_social = 0
    score_reputacao = 0

    texto_normalizado = normalizar_texto(texto)

    for padrao in PADROES_ENGENHARIA_SOCIAL:
        if padrao in texto_normalizado:
            score_social += 2
            motivos.append(
                f"Possível técnica de engenharia social detectada: '{padrao}'"
            )

    for palavra in PALAVRAS_SUSPEITAS:
        if palavra in texto_normalizado:
            score_texto += 1
            motivos.append(f"Palavra suspeita encontrada: '{palavra}'")

    links = detectar_links(texto)
    emails = detectar_emails(texto)
    telefones = detectar_telefones(texto)

    if links:
        score_links += len(links) * 2
        motivos.append(f"Foram encontrados {len(links)} link(s) na mensagem.")

    # =========================
    # VALIDAÇÃO DE URL
    # =========================

    for link in links:

        reputacao = validar_url(link)
        whois_info = consultar_whois(link)

        if len(link) > 120:
            score_reputacao += 2

            motivos.append(
                "URL excessivamente longa detectada."
            )

        if "erro" not in whois_info:

            idade = whois_info.get("idade_dias")

            if idade is not None and idade < 30:
                score_reputacao += 3

                motivos.append(
                    f"Domínio criado recentemente ({idade} dias)."
                )

        else:

            score_reputacao += 1

            motivos.append(
                "Não foi possível validar informações WHOIS do domínio."
            )

        if not reputacao["valida"]:
            score_reputacao += 3
            motivos.append("URL inválida detectada.")

        if reputacao.get("encurtador"):
            score_reputacao += 2
            motivos.append(
                f"Encurtador suspeito detectado: {reputacao['dominio']}"
            )

    if emails:
        score_texto += len(emails)
        motivos.append(f"Foram encontrado(s) {len(emails)} e-mail(s) na mensagem.")

    if telefones:
        score_texto += len(telefones)
        motivos.append(f"Foram encontrado(s) {len(telefones)} telefone(s) na mensagem.")

    dominios = analisar_dominios(links)

    for dominio in dominios:
        for dominio_suspeito in DOMINIOS_SUSPEITOS:
            if dominio_suspeito in dominio:
                score_reputacao += 3
                motivos.append(f"Domínio potencialmente suspeito encontrado: {dominio}")

    if "http://" in texto.lower():
        score_links += 2
        motivos.append("Link sem HTTPS encontrado.")

    if "http://" in texto.lower() and not links:
        score_reputacao += 2
        motivos.append("Possível URL malformada detectada.")

    scores = {
        "texto": score_texto,
        "links": score_links,
        "engenharia_social": score_social,
        "reputacao": score_reputacao
    }

    score_total = somar_scores(scores)

    nivel = classificar_risco(score_total)

    return {
        "score": score_total,
        "nivel_risco": nivel,
        "scores": scores,
        "motivos": motivos,
        "links": links,
        "emails": emails,
        "telefones": telefones,
        "dominios": dominios
    }
