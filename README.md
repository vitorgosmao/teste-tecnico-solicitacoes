# Teste técnico - processamento de solicitações

## Explicação breve da solução

Este projeto implementa, em Python, a leitura de um arquivo JSON com solicitações, aplica regras de validação de negócio e exporta os registros aprovados para um arquivo CSV.

A lógica principal está concentrada em `main.py` e é composta por três etapas:

- `carregar_dados()`: lê o arquivo `solicitacoes.json` e valida a estrutura do conteúdo;
- `filtragem()`: normaliza os campos `cpf` e `status`, ignora registros com CPF vazio ou sem status `APROVADO` e retorna apenas os registros válidos;
- `gerar_arquivo()`: remove a coluna `status` e salva o resultado em `aprovados.csv`.

A função `main()` orquestra a execução, registra eventos no log e gera a saída final do processo.

## Pré-requisitos

Para executar o projeto, é necessário ter:

- Python 3.10 ou superior;
- `pip` instalado e configurado no ambiente;
- acesso à pasta do projeto via terminal ou editor;
- as dependências listadas em `requirements.txt` instaladas localmente.

Dependências do projeto:

- `pandas`
- `logging`

## Instruções para executar o projeto

1. Abra o terminal na raiz do repositório.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o script principal:

```bash
python main.py
```

4. Após a execução, os arquivos abaixo serão gerados na raiz do projeto:

- `aprovados.csv`
- `processamento.log`

## Premissas adotadas

- O arquivo de entrada está no diretório raiz do projeto e se chama `solicitacoes.json`.
- O processo considera como válidos apenas os registros em que:
  - o campo `cpf` não está vazio;
  - o campo `status` é exatamente `APROVADO`.
- Registros com CPF ausente ou com status diferente de `APROVADO` são descartados do resultado final.
- O arquivo final contém apenas os campos relevantes para a operação: `id`, `nome` e `cpf`.
- O processamento gera um log em `processamento.log` para registrar início, avisos, exportação e encerramento da execução.

## Decisões relevantes

### Separador utilizado no CSV

O arquivo CSV foi gerado com o separador padrão do Pandas: a vírgula `,`.

Essa escolha foi adotada porque:

- é o padrão mais comum para arquivos CSV;
- os dados do projeto não exigem um separador diferenciado;
- a estrutura dos campos (`id,nome,cpf`) se organiza de forma clara em colunas separadas por vírgulas.

### Tratamento de normalização

Antes da filtragem, o código aplica:

- `fillna('')` para transformar valores nulos em string vazia;
- `str.strip()` para remover espaços em branco antes e depois dos textos;

Isso evita que registros com entradas aparentemente válidas, mas com espaços ou valores vazios, sejam considerados adequados.

### Exportação final

- a coluna `status` foi removida antes da gravação do arquivo;
- a exportação usa `encoding='utf-8'`;
- o parâmetro `index=False` foi utilizado para evitar a inclusão de um índice adicional no CSV.

## Ferramentas de consulta ou IA utilizadas

Neste projeto, a implementação foi elaborada com base na leitura do enunciado, nos arquivos disponibilizados no repositório e na documentação oficial da linguagem Python e da biblioteca Pandas.

Não houve uso de IA para gerar a regra de negócio principal do processamento; 

Foi utilizado IA (ChatGPT e GitHub Copilot) para: 
- Aprender a utilizar e configurar a biblioteca logging;
- Otimizar o uso de try/except;
- Correção de bugs; 
- Desenvolvimento da documentação/README.


## Integração com processos (RESPOSTA)

Acredito que se levarmos essa solução para um processo BPM, os registros recebidos via formulário podem seguir sendo normalizados e filtrados(identificar solicitações com dados faltantes) de forma automática antes de serem enviados para etapa de aprovação pela pessoa responsável. Após a etapa de aprovação, as solicitações são novamente filtradas para então gerar um CSV somente com as solicitações APROVADAS. 

- Formulário preenchido;
- Aplicação de normalização nos dados e filtragem (solicitações com dados faltantes);
- Etapa de aprovação;
- Filtragem para identificar solicitações não aprovadas;
- Gerar arquivo CSV com solicitações aprovadas.