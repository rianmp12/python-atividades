try:
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))

    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser maiores que zero.")
    else:
        imc = peso / (altura ** 2)
        imc_formatado = round(imc, 1)

        print("Seu IMC é:", imc_formatado)

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 25:
            print("Classificação: Peso normal")
        elif imc < 30:
            print("Classificação: Sobrepeso")
        elif imc < 35:
            print("Classificação: Obesidade grau I")
        elif imc < 40:
            print("Classificação: Obesidade grau II")
        else:
            print("Classificação: Obesidade grau III (obesidade mórbida)")

except ValueError:
    print("Valor inválido. Digite números válidos usando ponto para decimais.")