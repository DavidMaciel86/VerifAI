import streamlit as st
from core.analisador import analisar_texto

from core.score import (
    calcular_progresso,
    calcular_score_visual
)

st.set_page_config(
    page_title="VerifAI",
    page_icon="🛡️",
    layout="centered"
)

# =========================
# ESTILO VISUAL
# =========================

st.divider()
st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.stTextArea textarea {
    font-size: 16px;
}

.titulo {
    text-align: center;
    color: #00d4ff;
    font-size: 42px;
    font-weight: bold;
}

.subtitulo {
    text-align: center;
    font-size: 18px;
    color: #cfcfcf;
    margin-bottom: 25px;
}

.risco-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}

.alto {
    background-color: #5c1a1a;
    color: #ff4b4b;
}

.medio {
    background-color: #5c4b1a;
    color: #ffd24b;
}

.baixo {
    background-color: #1a5c2e;
    color: #4bff88;
}

</style>
""", unsafe_allow_html=True)

# =========================
# CABEÇALHO
# =========================

st.markdown(
    '<div class="titulo">🛡️ VerifAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Ferramenta de Verificação de Golpes Digitais</div>',
    unsafe_allow_html=True
)

st.write(
    "Cole abaixo uma mensagem, link, e-mail ou número suspeito para análise."
)

# =========================
# CAMPO DE TEXTO
# =========================

mensagem = st.text_area(
    "Conteúdo suspeito:",
    height=220,
    placeholder="Ex: URGENTE! Seu PIX foi bloqueado. Clique aqui para atualizar seus dados..."
)

# =========================
# BOTÃO
# =========================

if st.button("🔍 Analisar Conteúdo"):

    if mensagem.strip() == "":
        st.warning("Digite ou cole algum conteúdo para análise.")

    else:

        with st.spinner("🛡️ Analisando conteúdo suspeito..."):

            resultado = analisar_texto(mensagem)

        nivel = resultado["nivel_risco"]
        score = resultado["score"]

        # =========================
        # SCORE VISUAL
        # =========================

        st.markdown("## Score de Risco")

        progresso = calcular_progresso(score)
        st.progress(progresso)

        score_visual = calcular_score_visual(score)

        st.write(f"Pontuação de risco: **{score_visual}/10**")

        # =========================
        # ALERTA VISUAL
        # =========================

        if nivel == "ALTO":

            st.markdown(
                f'<div class="risco-box alto">🚨 RISCO ALTO</div>',
                unsafe_allow_html=True
            )

        elif nivel == "MÉDIO":

            st.markdown(
                f'<div class="risco-box medio">⚠️ RISCO MÉDIO</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f'<div class="risco-box baixo">✅ RISCO BAIXO</div>',
                unsafe_allow_html=True
            )

        # =========================
        # MOTIVOS
        # =========================

        st.markdown("## Motivos Encontrados")

        if resultado["motivos"]:
            for motivo in resultado["motivos"]:
                st.write(f"- {motivo}")
        else:
            st.write("Nenhum indício suspeito relevante foi encontrado.")

        # =========================
        # LINKS
        # =========================

        if resultado["links"]:

            st.markdown("## Links Detectados")

            for link in resultado["links"]:
                st.code(link)

        # =========================
        # E-MAILS
        # =========================

        if resultado["emails"]:

            st.markdown("## E-mails Detectados")

            for email in resultado["emails"]:
                st.code(email)

        # =========================
        # TELEFONES
        # =========================

        if resultado["telefones"]:

            st.markdown("## Telefones Detectados")

            for telefone in resultado["telefones"]:
                st.code(telefone)

        # =========================
        # RECOMENDAÇÃO FINAL
        # =========================

        st.markdown("## Recomendação Final")

        if nivel == "ALTO":

            st.error(
                "Não clique em links, não envie dados pessoais e confirme a informação pelos canais oficiais."
            )

        elif nivel == "MÉDIO":

            st.warning(
                "Tenha cautela. Verifique a autenticidade da mensagem antes de tomar qualquer ação."
            )

        else:

            st.success(
                "Mesmo com baixo risco, mantenha atenção e evite compartilhar dados sensíveis."
            )
