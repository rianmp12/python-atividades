import os
import pandas as pd
import json


def read_file(file_path):
    """Lê arquivos CSV, JSON ou TXT e retorna um DataFrame."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == '.csv':
            df = pd.read_csv(file_path)

        elif ext == '.json':
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if isinstance(data, list):
                    df = pd.DataFrame(data)
                elif isinstance(data, dict):
                    df = pd.DataFrame([data])
                else:
                    raise ValueError("Formato JSON inválido")

        elif ext == '.txt':
            try:
                df = pd.read_csv(file_path, delimiter='\t')
                if df.shape[1] == 1:
                    df = pd.read_csv(file_path, delimiter=',')
                if df.shape[1] == 1:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read().splitlines()
                    df = pd.DataFrame({'content': content})
            except Exception as e:
                raise ValueError(f"Erro ao ler TXT: {e}")

        else:
            raise ValueError("Formato não suportado. Use CSV, JSON ou TXT.")

        if df.empty:
            raise ValueError("O arquivo está vazio.")

        return df

    except Exception as e:
        raise RuntimeError(f"Erro ao ler arquivo: {e}")


def write_file():
    """Permite ao usuário criar e salvar dados em CSV, JSON ou TXT."""
    linhas = []
    print("\nDigite os dados no formato de colunas separados por vírgula.")
    print("Exemplo: nome,idade,cidade")
    header = input("Cabeçalho: ").split(',')

    print("Digite os dados linha por linha. Quando terminar, digite 'sair'.")

    while True:
        linha = input("Linha: ")
        if linha.strip().lower() == 'sair':
            break
        valores = linha.split(',')
        if len(valores) != len(header):
            print("Número de valores diferente do cabeçalho. Tente novamente.")
            continue
        linhas.append(valores)

    df = pd.DataFrame(linhas, columns=header)

    caminho_saida = input("\nInforme o caminho para salvar o arquivo (inclua extensão .csv, .json ou .txt): ")

    ext = os.path.splitext(caminho_saida)[1].lower()

    try:
        if ext == '.csv':
            df.to_csv(caminho_saida, index=False, encoding='utf-8')
        elif ext == '.json':
            df.to_json(caminho_saida, orient='records', force_ascii=False, indent=4)
        elif ext == '.txt':
            if 'content' in df.columns and df.shape[1] == 1:
                df['content'].to_csv(caminho_saida, index=False, header=False)
            else:
                df.to_csv(caminho_saida, index=False, sep='\t', encoding='utf-8')
        else:
            raise ValueError("Formato não suportado. Use CSV, JSON ou TXT.")

        print(f"Arquivo salvo com sucesso em: {caminho_saida}")

    except Exception as e:
        raise RuntimeError(f"Erro ao salvar arquivo: {e}")


if __name__ == "__main__":
    print("=== LEITOR E ESCRITOR DE ARQUIVOS CSV | JSON | TXT ===")

    operacao = input("\nO que deseja fazer? (ler/escrever): ").strip().lower()

    if operacao == 'ler':
        caminho_entrada = input("Informe o caminho do arquivo para leitura: ")

        try:
            df = read_file(caminho_entrada)
            print("\nArquivo lido com sucesso!\n")
            print(df)
        except Exception as erro:
            print(f"Ocorreu um erro: {erro}")

    elif operacao == 'escrever':
        try:
            write_file()
        except Exception as erro:
            print(f"Ocorreu um erro: {erro}")

    else:
        print("Operação inválida. Digite 'ler' ou 'escrever'.")
