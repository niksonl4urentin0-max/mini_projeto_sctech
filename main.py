import csv
from funcoes import (product_validations, 
                     calculate_median, 
                     median_agregation, 
                     clean_standart_string_str_lo_re, 
                     total_processed_rows, count_null, canceled_order)



#ABRINDO O ARQUIVO COM FUNCAO NATIVA PYTHON WITH OPEN
with open ('olist_products_dataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)    
    for row in data:        
        product_validations(row) # CHAMANDO FUNCAO PARA TRATAR VALORES NULOS DA COLUNA PRODUCT_CATEGORY_NAME        
        clean_standart_string_str_lo_re(row) # CHAMANDO FUNCAO PARA PADRONIZAR COLUNA PRODUCT_CATEGORY_NAME .STRIP(), .LOWER(), REGEX PARA RETIRAR CARACTERES ESPECIAIS

    process_cols = ["product_weight_g","product_length_cm","product_height_cm","product_width_cm"]    
    medians = [calculate_median(col, data) for col in process_cols]
    results = [median_agregation(col, medians, data) for col in process_cols] #SUBSTITUI OS VALORES NULOS PELAS MEDIANAS

# for result in results:
#     for value in result:
#         print(value, end='\n')

print(total_processed_rows, count_null, canceled_order)
#3. LÓGICA DE REGRA DE NEGÓCIO (FILTROS E VALIDAÇÃO)
#ABRINDO O ARQUIVO COM FUNCAO NATIVA PYTHON WITH OPEN DA PLANILHA 
# with open ('olist_orders_dataset.csv', 'r', encoding='utf-8') as z:
#     reader2 = csv.DictReader(z)
#     data2 = list(reader2)
#     for row2 in data2:
#         print(row2)