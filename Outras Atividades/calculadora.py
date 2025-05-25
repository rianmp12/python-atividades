while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ["+", "-", "*", "/"]:
            print("Operação inválida. Escolha uma das seguintes: +, -, *, /")
            continue

        if operacao == "/" and numero2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            continue

        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2

        print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")
        break

    except ValueError:
        print("Entrada inválida. Digite apenas números válidos.")