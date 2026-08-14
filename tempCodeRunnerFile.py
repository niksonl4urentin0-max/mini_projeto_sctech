import csv
import re
import datetime

physical_dims = {'product_weight_g':'dim1', 'product_length_cm':'dim2', 'product_height_cm':'dim3', 'product_width_cm':'dim4'}
dim1, dim2, dim3, dim4 = [],[],[],[]

def product_validations(csv_row):
    # VALIDACAO E TRATAMENTO DE DADOS AUSENTES - COL_PRODUCT_CATEGORY_NAME
    if csv_row['product_category_name'].strip() == '':
        csv_row['product_category_name'] = 'Sem Categoria' #CASO O NOME DA CATEGORIA ESTEJA VAZIO, ATRIBUIR O VALOR 'Sem Categoria'
    else:
        csv_row['product_category_name'] = csv_row['product_category_name'].strip()
   
    return csv_row

  
#ABRINDO O ARQUIVO COM FUNCAO NATIVA PYTHON WITH OPEN
with open ('olist_products_dataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)    
    for row in data:        
        print(product_validations(row)) #CHAMANDO FUNCAO PARA TRATAR VALORES NULOS DE COLUNA product_category_name

    for col, dim in physical_dims.items():
        dim = [row[col] for row in data]