# Importação das bibliotecas a serem utilizadas
import pandas as pd
import logging 

# Função responsável por carregar o arquivo, caso exista, 
# que contém os dados a serem processados 
def carregar_dados(arquivo_entrada): 
    try:
        df = pd.read_json(arquivo_entrada)
        logging.info("Arquivo carregado")
        logging.info(f"Total de registros lidos: {len(df)}")
        return df
    
    except FileNotFoundError as erro:
        logging.error(f"Arquivo não encontrado:{erro}")
        raise

    except ValueError as erro:
        logging.error(f"Arquivo inválido:{erro}")
        raise

    except Exception as erro:
        logging.exception(f"Erro durante a leitura do arquivo:{erro}")
        raise

# Função responsável pela filtragem dos dados: recebe um dataframe com os dados que foram carregados, normaliza os dados, 
# identifica os dados inválidos e retorna um dataframe contendo somente os dados válidos. 
def filtragem(df):
    logging.info("Iniciando filtragem de valores inválidos")

    # normalização dos valores
    df = df.copy()

    df['cpf'] = df['cpf'].fillna('').str.strip()
    df['status'] = df['status'].fillna('').str.strip()

    # identificação dos registros inválidos
    for _, registro in df.iterrows():

        if registro['cpf'] == '':
            logging.warning(
                f"Registro {registro['id']} ignorado: CPF não informado"
            )

        elif registro['status'] != 'APROVADO':
            logging.warning(
                f"Registro {registro['id']} ignorado: Registro não aprovado"
            )

    # filtragem
    df_filtrado = df[
        (df['cpf'] != '') &
        (df['status'] == 'APROVADO')
    ]
    logging.info(f"Total de registros filtrados: {len(df) - len(df_filtrado)}")

    return df_filtrado

# Função responsável por gerar o arquivo final contendo somente os registros válidos
# que foram identificados durante a filtragem
def gerar_arquivo(df, nome_do_arquivo_saida):
    df.drop(['status'], axis='columns', inplace=True)

    try: 
        df.to_csv(nome_do_arquivo_saida, encoding='utf-8', index=False)
        logging.info(f"Arquivo [{nome_do_arquivo_saida}] criado com sucesso.")
        logging.info(f"Total de registros exportados:{len(df)}")
    
    except Exception :
        logging.exception("Erro durante a escrita do arquivo:[%s]")
        raise

# Função principal, responsável pela orquestração das funções de processamento. 
def main():
    # Configuração do logger
    logging.basicConfig(
        level=logging.INFO,
        filename="processamento.log",
        encoding="utf-8",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    arquivo_entrada = 'solicitacoes.json'
    arquivo_saida = 'aprovados.csv'

    try:
        logging.info("Inicio do processamento")
        df = carregar_dados(arquivo_entrada)
        df_aprovados = filtragem(df)
        gerar_arquivo(df_aprovados, arquivo_saida)
        logging.info("Fim do processamento")

    except Exception:
        logging.exception("Falha durante a execução do processamento.")
        raise

if __name__ == "__main__":
    main()