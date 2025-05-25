def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

try:
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

    valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)

    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    print(f"Valor total com gorjeta: R$ {valor_conta + valor_gorjeta:.2f}")

except ValueError:
    print("Entrada inválida. Digite números válidos para o valor e a porcentagem.")