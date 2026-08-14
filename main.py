import csv
import re
import datetime
from funcoes import calculate_median, sort_cols_median_preparation, product_validations


  
#ABRINDO O ARQUIVO COM FUNCAO NATIVA PYTHON WITH OPEN
with open ('olist_products_dataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)    
    for row in data:        
        product_validations(row) #CHAMANDO FUNCAO PARA TRATAR VALORES NULOS DE COLUNA product_category_name

    process_cols = ["product_weight_g","product_length_cm","product_height_cm","product_width_cm"]
    
    medians = [calculate_median(sort_cols_median_preparation(col)) for col in process_cols]
    # Desempacota a lista diretamente nas variáveis m1, m2, m3 e m4
    m1, m2, m3, m4 = medians
    print(f"M1 (Peso): {m1}")
    print(f"M2 (Comprimento): {m2}")
    print(f"M3 (Altura): {m3}")
    print(f"M4 (Largura): {m4}")

