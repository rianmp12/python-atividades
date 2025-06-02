import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" not in dados:
            print(f"\nLogradouro: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade: {dados.get('localidade')}")
            print(f"Estado: {dados.get('uf')}\n")
        else:
            print("CEP não encontrado.\n")
    else:
        print("Erro na consulta.\n")

if __name__ == "__main__":
    while True:
        cep = input("Digite o CEP (apenas números): ").strip()

        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. Digite exatamente 8 números.\n")
            continue

        consultar_cep(cep)
        break