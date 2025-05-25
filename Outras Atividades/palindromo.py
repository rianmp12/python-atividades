def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("-", "")
    return texto == texto[::-1]

entrada = input("Digite uma palavra ou frase: ")

if verificar_palindromo(entrada):
    print("Sim")
else:
    print("Não")