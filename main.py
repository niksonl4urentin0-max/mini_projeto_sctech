import csv
import datetime
from funcoes import (
    product_validations, 
    calculate_median, 
    median_agregation, 
    clean_standart_string_str_lo_re
)

count_null = 0 
canceled_order = 0
list_canceled_orders = []
list_not_canceled_orders = []

# ABRINDO O ARQUIVO DE PRODUTOS
with open('olist_products_dataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)     
    
    # O total de linhas processadas é o tamanho total do dataset
    total_processed_rows = len(data)  

    for row in data:               
        if product_validations(row): 
            count_null += 1
            
        clean_standart_string_str_lo_re(row) # COLOQUEI ESSA FUNCAO PARA PADRONIZAR, .STRIP(), .LOWER() E REGEX

    process_cols = ["product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"]    
    medians = [calculate_median(col, data) for col in process_cols] # NESSA PARTE A LIST COMPREHENSION JOGA PARA A FUNCAO ORDENAR, TIRAR A MEDIDA E ARMAZENAR NA VARIVAVEL MEDIANS    
    for col in process_cols:
        median_agregation(col, medians, data) #NESSA PARTE A SEGUNDA FUNCAO AGREGA AOS VALORES NULOS, POIS DESEMPACOTA O VALOR INTERNAMENTE EM QUATRO VARIAVEIS
        

# ABRINDO O ARQUIVO DE PEDIDOS
with open('olist_orders_dataset.csv', 'r', encoding='utf-8') as z:
    reader2 = csv.DictReader(z)
    data2 = list(reader2)
    for row2 in data2:
        if row2.get('order_approved_at') and row2['order_approved_at'].strip() != '':
            try:                
                dt_obj = datetime.datetime.strptime(row2['order_approved_at'], '%Y-%m-%d %H:%M:%S')
                row2['order_approved_at'] = dt_obj.strftime('%d/%m/%Y')
            except ValueError:
                pass
        if (row2['order_delivered_customer_date'] == '' or row2['order_delivered_customer_date'] is None) and row2['order_status'] == 'canceled':
            canceled_order += 1
            list_canceled_orders.append(row2)
        elif row2['order_delivered_customer_date'] == '' or row2['order_delivered_customer_date'] is None:
            list_not_canceled_orders.append(row2)

print()
print(f'{'-'*100} LISTA DE PEDIDOS CANCELADOS {'-'*100}', sep='\n\n')
print(*list_canceled_orders, sep='\n')
print("-" * 300)


print('SUMÁRIO ESTATÍSTICO')
print(f'Total de linhas processadas: {total_processed_rows}') 
print(f'Valores nulos tratados: {count_null}')
print(f'Total de pedidos cancelados: {canceled_order}')