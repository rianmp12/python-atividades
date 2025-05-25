pares = 0
par_list = []

impares = 0
impar_list = []

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1
            par_list.append(numero)
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1
            impar_list.append(numero)

    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros ou 'fim' para encerrar.")

print("\n=== RESUMO ===")
print(f"Quantidade de números PARES: {pares}")
print(f"Números PARES: {par_list}")
print(f"Quantidade de números ÍMPARES: {impares}")
print(f"Números ÍMPARES: {impar_list}")