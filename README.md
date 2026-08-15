Descrição do Projeto
Este projeto tem como objetivo realizar o tratamento e a sanitização da base de dados pública da Olist E-commerce, atendendo a um estudo de caso específico para melhoria da qualidade dos dados. O script desenvolvido processa os arquivos de produtos (olist_products_dataset.csv) e pedidos (olist_orders_dataset.csv) com os seguintes objetivos:

- Tratamento de Dados Ausentes: Identificação de nulos ou vazios na coluna product_category_name, preenchendo-os com a string "sem categoria". Dimensões físicas dos produtos, colunas ("product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"), com valores nulos ou ausentes foram feitas imputações estatísticas usando a mediana.
- Padronização: Aplicação de strip(), lower() e limpeza de caracteres especiais via Expressões Regulares (Regex) para normalizar os nomes das categorias de produtos.
- Regra de Negócio: Aplicação de lógica condicional para verificar pedidos com datas de entrega ausentes, confirmando a hipótese de que esses casos estão atrelados a pedidos com status de cancelado ("canceled").
- Formatação Temporal: Conversão da coluna order_approved_at do formato original para o padrão brasileiro simplificado (DD/MM/AAAA) utilizando o módulo datetime.
- Relatório de Status: Geração de um sumário estatístico manual contendo o total de linhas processadas, registros nulos tratados e o volume de pedidos cancelados identificados.

Guia de Execução

Importante: Precisa ter o Python 3.x instalado em sua máquina.

 Passo a Passo:
1. Obtenção dos arquivos: Clone ou baixe todos os arquivos do projeto (main.py, funcoes.py, olist_orders_dataset.csv e olist_products_dataset.csv).
2. Organização: Certifique-se de que todos os arquivos (scripts e datasets) estejam armazenados na mesma pasta.
3. Execução:
   - Abra o terminal (CMD, PowerShell ou terminal do VS Code).
   - Navegue até a pasta onde salvou os arquivos.
   - Execute o script principal digitando o comando: python main.py
4. Resultado: Ao final do processamento, o programa exibirá um sumário estatístico detalhando as linhas processadas, valores nulos tratados e uma lista dos pedidos cancelados com a devida comprovação.

Reflexão Teórica sobre Machine Learning:

O Data Cleaning (limpeza dos dados), assim como a análise exploratória, impactam diretamente na qualidade dos dados para a modelagem e processamento final em Machine Learning. A falta de tratamento adequado de dados ausentes pode causar falhas no pipeline de processamento. A imputação de valores (atribuir dados a campos faltantes) precisa ser feita com cautela, pois a métrica utilizada pode ser indevidamente influenciada por outliers (valores fora do padrão).

A negligência neste processo pode levar ao Overfitting, onde o algoritmo "decora" o ruído produzido pela falta de tratamento dos dados, perdendo sua capacidade de generalização. Por outro lado, pode-se criar um Viés, onde o modelo acaba encarando erros e inconsistências dos dados como um padrão real a ser replicado no processo interno, comprometendo a precisão e a imparcialidade das predições em cenários futuros.





