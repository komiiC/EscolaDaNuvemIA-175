import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {media_tempo}")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo} segundos")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")

nome_arquivo = input("Digite o nome do arquivo de log: ")
processar_logs_treinamento(nome_arquivo)