# 🛡️ VerifAI

Ferramenta de Verificação de Golpes Digitais desenvolvida no projeto extensionista **“Segurança e Cidadania Digital: Educação e Tecnologia”**, do curso de Gestão de TI da PUCPR.

## 🎯 Objetivo

O VerifAI tem como objetivo auxiliar na identificação preventiva de possíveis golpes digitais, mensagens suspeitas, links maliciosos, e-mails fraudulentos e tentativas de engenharia social.

O projeto também busca promover conscientização e educação em segurança digital, alinhado principalmente ao **ODS 16 — Paz, Justiça e Instituições Eficazes**.

## 🚀 Funcionalidades atuais

- Interface web com Streamlit
- Análise textual de mensagens suspeitas
- Detecção de palavras associadas a golpes
- Detecção de padrões de engenharia social
- Detecção de links
- Detecção de e-mails
- Detecção de telefones
- Identificação de domínios potencialmente suspeitos
- Classificação de risco: baixo, médio ou alto
- Score visual de risco
- Métricas por categoria
- Recomendação preventiva ao usuário

## 🧠 Como funciona

O VerifAI utiliza uma análise heurística baseada em:

- palavras suspeitas;
- presença de links;
- domínios suspeitos;
- ausência de HTTPS;
- padrões comuns de engenharia social;
- identificação de e-mails e telefones.

A ferramenta não substitui soluções profissionais de segurança, mas atua como apoio educativo e preventivo.

## 🛠️ Tecnologias utilizadas

- Python 3.11
- Streamlit
- Regex
- Unicodedata
- PyCharm Community

## 📁 Estrutura do projeto

```text
VerifAI/
├── assets/
├── core/
│   ├── analisador.py
│   └── score.py
├── docs/
├── services/
│   └── url_reputation.py
├── utils/
│   ├── normalizacao.py
│   └── regex_patterns.py
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/verifai.git
```

Acesse a pasta:

```bash
cd verifai
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
streamlit run app.py
```

## 📌 Roadmap do Projeto

- [x] MVP com Streamlit
- [x] Detecção de links
- [x] Detecção de e-mails
- [x] Detecção de telefones
- [x] Score visual de risco
- [x] Organização modular do projeto
- [ ] Validação real de URLs
- [ ] Detecção de encurtadores
- [ ] Integração com WHOIS
- [ ] Integração com VirusTotal
- [ ] Integração futura com WhatsApp Cloud API
- [ ] Painel educativo com dicas de segurança digital

## 🌍 Impacto social

O projeto busca contribuir para a cidadania digital, auxiliando pessoas a reconhecerem possíveis golpes e reduzindo riscos de fraudes digitais em comunidades, ONGs, escolas e igrejas.

## 👨‍💻 Autor

David Do Rosario Maciel  
Tecnologia em Gestão da Tecnologia da Informação — PUCPR
