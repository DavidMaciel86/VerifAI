from core.analisador import analisar_texto

print("=== VerifAI - Verificação de Golpes Digitais ===\n")

mensagem = input("Digite a mensagem suspeita:\n\n")

resultado = analisar_texto(mensagem)

print("\n===== RESULTADO DA ANÁLISE =====")
print(f"Nível de risco: {resultado['nivel_risco']}")

print("\nMotivos encontrados:")

for motivo in resultado['motivos']:
    print(f"- {motivo}")
