from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

try:
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    idade_dias = calcular_idade_em_dias(ano_nascimento)
    print(f"Sua idade aproximada em dias é: {idade_dias} dias.")

except ValueError:
    print("Entrada inválida. Digite um ano válido.")