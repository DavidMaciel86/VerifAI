def classificar_risco(score_total):
    if score_total >= 8:
        return "ALTO"
    elif score_total >= 4:
        return "MÉDIO"
    else:
        return "BAIXO"


def calcular_score_visual(score_total, limite=10):
    return min(score_total, limite)


def calcular_progresso(score_total, limite=10):
    return min(score_total / limite, 1.0)


def somar_scores(scores):
    return sum(scores.values())