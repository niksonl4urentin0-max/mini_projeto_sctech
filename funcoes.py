import re
import datetime

total_processed_rows = 0    #INSERI TRES CONTADORES PARA FAZER OS SUMARIO ESTATISTICO MANUAL
count_null = 0              #A CADA EVENTO SERA ADICIONADO "+1" DENTRO DA FUNCAO RESPECTICVA NO MODULO FUNCOES  
canceled_order = 0

def product_validations(csv_row):
    # VALIDACAO E TRATAMENTO DE DADOS AUSENTES - COL_PRODUCT_CATEGORY_NAME
    if csv_row['product_category_name'].strip() == '':
        csv_row['product_category_name'] = 'Sem Categoria' # 1. VALIDAÇÃO E TRATAMENTO DE DADOS AUSENTES - VALOR NULO/VAZIO NA COLUNA PRODUCT_CATEGORY_NAME PREENCHIDO COM A STRING "SEM CATEGORIA".        
        global count_null, total_processed_rows        
        count_null +=1
        total_processed_rows+=1 #CONTADOR GERAL DE PROCESSAMENTO      
    return csv_row


def calculate_median(column_name, data_list): 
    # 1 ...VALORES NULOS NAS DIMENSÕES FÍSICAS ("PRODUCT_WEIGHT_G","PRODUCT_LENGTH_CM","PRODUCT_HEIGHT_CM","PRODUCT_WIDTH_CM") ATRIBUÍDO MEDIANA EM DUAS ETAPAS
    sorted_list = sorted([
        float(row[column_name]) 
        for row in data_list if row[column_name] is not None and row[column_name].strip() != ''
        ])    
    n = len(sorted_list)
    if n == 0:
        return None
    # SE A QUANTIDADE DE ELEMENTOS FOR ÍMPAR, PEGA O ELEMENTO DO MEIO EXATO
    if n % 2 != 0:
        return sorted_list[n // 2]
    # SE FOR PAR, FAZ A MÉDIA DOS DOIS ELEMENTOS CENTRAIS
    else:
        mid1 = sorted_list[(n // 2) - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

def median_agregation(column, medians_list, final_datalist):
    global total_processed_rows
    total_processed_rows +=1 #CONTADOR GERAL DE PROCESSAMENTO
    # DESEMPACOTA A LISTA NAS VARIÁVEIS M1, M2, M3 E M4
    m1, m2, m3, m4 = medians_list     
    # MAPEIA CADA COLUNA PARA A SUA RESPECTIVA MEDIANA
    medians_dict = {
        "product_weight_g": m1,
        "product_length_cm": m2,
        "product_height_cm": m3,
        "product_width_cm": m4
    }    
    # PEGA A MEDIANA ESPECÍFICA DA COLUNA ATUAL
    target_median = medians_dict.get(column)    
    # SUBSTITUI O VALOR SE ESTIVER NULO OU VAZIO
    for row in final_datalist:
        if row[column] is None or row[column].strip() == '':
            row[column] = str(target_median)            
    return final_datalist 
    # 1 ATRIBUICAO DE MEDIANA AOS VALORES NULOS DAS DIMENSOES FISICAS DOS PRODUTOS, POIS GERALMENTE A MEDIANA SOFRE MENOR IMPACTO DE OUTLIERS


def clean_standart_string_str_lo_re (name_row):    
    if name_row['product_category_name'] is not None and name_row['product_category_name']!= '':
        global total_processed_rows
        total_processed_rows +=1 #CONTADOR GERAL DE PROCESSAMENTO
        text = name_row['product_category_name'].strip().lower() #2. PADRONIZAÇÃO DE STRINGS E REGEX:
        name_row['product_category_name'] = re.sub(r'[^\w\s]', '', text) #2 ...EXPRESSÕES REGULARES (MÓDULO RE) PARA LIMPAR EVENTUAIS CARACTERES ESPECIAIS OU PONTUAÇÕES INDEVIDAS DOS NOMES DAS CATEGORIAS
    return name_row