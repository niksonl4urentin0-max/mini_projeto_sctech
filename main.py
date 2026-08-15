import csv
import datetime
from funcoes import (
    product_validations, 
    calculate_median, 
    median_agregation, 
    clean_standart_string_str_lo_re
) #IMPORTACOES DO MODULO FUNCOES.PY

#CONTADORES PARA SUMARIO ESTATISTICO 
count_null = 0 
canceled_order = 0
total_processed_rows = 0
list_canceled_orders = []

# ABRINDO O ARQUIVO DE PRODUTOS
with open('olist_products_dataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f) #USO O DICTREADER PARA ABRIR COMO DICIONARIO
    data = list(reader)    #USO O DATA COMO LISTA DE DICIONARIOS
    for row in data:

        #1. Validação e Tratamento de Dados Ausentes:   
        valid = product_validations(row)
        if valid:
            count_null += 1 #CASO O VALOR RETORNE TRUE SOMA O CONTADOR NULO        
            
        #2. Padronização de Strings e Regex:
        clean_standart_string_str_lo_re(row) # COLOQUEI ESSA FUNCAO PARA PADRONIZAR, .STRIP(), .LOWER() E REGEX
        total_processed_rows += 1 #SOMA TOTAL CONTADOR

    process_cols = ["product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"]    
    medians = [calculate_median(col, data) for col in process_cols] # NESSA PARTE A LIST COMPREHENSION JOGA PARA A FUNCAO ORDENAR, 
    #TIRAR A MEDIDA E ARMAZENAR NA VARIVAVEL MEDIANS    

    for col in process_cols:
        total_processed_rows += 1 #SOMA TOTAL CONTADOR PARA MEDIANA INSERIDO EM VALORES NULOS DE DIMENSOES FISICAS

        # 1 ...Para os valores nulos nas dimensões físicas (product_weight_g, product_length_cm, etc.):
        median_agregation(col, medians, data) #NESSA PARTE A SEGUNDA FUNCAO AGREGA AOS VALORES NULOS, 
        #POIS DESEMPACOTA O VALOR INTERNAMENTE EM QUATRO VARIAVEIS INTERNAMENTE NA FUNCAO MEDIAN_AGREGATION
        
# ABRINDO O ARQUIVO DE PEDIDOS
with open('olist_orders_dataset.csv', 'r', encoding='utf-8') as z:
    reader2 = csv.DictReader(z)
    data2 = list(reader2)
    for row2 in data2:
        if row2.get('order_approved_at') and row2['order_approved_at'].strip() != '':
            # 4. Formatação Temporal (Datetime) - SE O PEDIDO APROVADO NÃO ESTÁ VAZIO
            try:                
                dt_obj = datetime.datetime.strptime(row2['order_approved_at'], '%Y-%m-%d %H:%M:%S') # FAZ VALIDACAO DE DATA PARA BR
                row2['order_approved_at'] = dt_obj.strftime('%d/%m/%Y')
            except ValueError: # MONTA-SE UMA ESTRUTURA PARA EVITAR ERRO, POR FALTA DE INFORMAÇÃO (VAZIO OU NULO) NO CAMPO 
                pass
        # 2. Lógica de Regra de Negócio (Filtros e Validação):
        if (row2['order_delivered_customer_date'] == '' or row2['order_delivered_customer_date'] is None) and row2['order_status'] == 'canceled':
            canceled_order += 1 # SOMENTE CONTA PEDIDO CANCELADO SE CUMPRIR A LOGICA ACIMA,
            # DATA DO PEDIDO VAZIO OU NULO E STATUS PEDIDO - CANCELADO

            list_canceled_orders.append(row2) # ADICIONA A LINHA DO PEDIDO NA LISTA DE PEDIDOS CANCELADOS



print()
print(f'{'-'*100} LISTA DE PEDIDOS CANCELADOS {'-'*100}', sep='\n\n')
print(*list_canceled_orders, sep='\n')
print("-" * 300)

#5. Relatório de Status Manual:
print('SUMÁRIO ESTATÍSTICO')
print(f'Total de linhas processadas: {total_processed_rows}') 
print(f'Valores nulos tratados: {count_null}')
print(f'Total de pedidos cancelados: {canceled_order}')