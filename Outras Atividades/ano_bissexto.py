try:
    ano = int(input("Digite um ano: "))

    if ano <= 0:
        print("Ano inválido. Digite um ano positivo.")
    elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é BISSEXTO.")
    else:
        print(f"O ano {ano} NÃO é bissexto.")

except ValueError:
    print("Valor inválido. Digite um ano usando apenas números inteiros.")