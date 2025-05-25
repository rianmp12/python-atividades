try:
    idade = int(input("Digite sua idade: "))

    if idade < 0:
        print("Idade inválida. Por favor, digite um número positivo.")
    elif idade <= 12:
        print("Você é uma CRIANÇA.")
    elif idade <= 17:
        print("Você é um ADOLESCENTE.")
    elif idade <= 59:
        print("Você é um ADULTO.")
    else:
        print("Você é um IDOSO.")

except ValueError:
    print("Valor inválido. Digite apenas números inteiros e positivos.")