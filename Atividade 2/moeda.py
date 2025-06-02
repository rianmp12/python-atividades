import requests

def consultar_cotacao(moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
    response = requests.get(url)

    if response.status_code != 200:
        print('Erro ao consultar a cotação. Verifique se o código da moeda está correto.')
        return

    dados = response.json()
    chave = f'{moeda}BRL'

    if chave not in dados:
        print('Moeda não encontrada. Verifique o código informado.')
        return

    info = dados[chave]
    print(f"\nCotação de {moeda} para BRL:")
    print(f"Valor atual: R$ {info['bid']}")
    print(f"Valor máximo: R$ {info['high']}")
    print(f"Valor mínimo: R$ {info['low']}")
    print(f"Data da última atualização: {info['create_date']}")

if __name__ == "__main__":
    moeda = input('Informe o código da moeda estrangeira (ex: USD, EUR, GBP): ').upper()
    consultar_cotacao(moeda)