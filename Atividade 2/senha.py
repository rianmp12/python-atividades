import random
import string

def gerar_senha(tamanho=12):
    if tamanho < 4:
        raise ValueError("A senha precisa ter no mínimo 4 caracteres.")

    grupos = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

    senha = [random.choice(grupo) for grupo in grupos]

    todos = ''.join(grupos)
    senha += random.choices(todos, k=tamanho - 4)

    random.shuffle(senha)
    return ''.join(senha)

tamanho = int(input("Informe o tamanho da senha: "))
print("Senha gerada:", gerar_senha(tamanho))