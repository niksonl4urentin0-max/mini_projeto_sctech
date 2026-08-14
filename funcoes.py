import re

def product_validations(csv_row):
    # VALIDAÇÃO E TRATAMENTO DE DADOS AUSENTES - COL_PRODUCT_CATEGORY_NAME
    if csv_row['product_category_name'].strip() == '':
        csv_row['product_category_name'] = 'Sem Categoria' 
        return True  # Retorna True se o valor era nulo/vazio e foi tratado
    else:
        csv_row['product_category_name'] = csv_row['product_category_name'].strip()   
    return False     # Retorna False se já tinha valor

def calculate_median(column_name, data_list): 
    # JUSTIFICATIVA TÉCNICA: A MEDIANA FOI ESCOLHIDA PARA AS DIMENSÕES FÍSICAS POIS É UMA MEDIDA 
    # QUE GERALMENTE É MENOS SUSCETÍVEL A OUTLIERS 
    sorted_list = sorted([
        float(row[column_name]) 
        for row in data_list if row[column_name] is not None and row[column_name].strip() != ''
        ])    
    n = len(sorted_list)
    if n == 0:
        return None
    if n % 2 != 0:
        return sorted_list[n // 2]
    else:
        mid1 = sorted_list[(n // 2) - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

def median_agregation(column, medians_list, final_datalist):
    m1, m2, m3, m4 = medians_list    
    medians_dict = {
        "product_weight_g": m1,
        "product_length_cm": m2,
        "product_height_cm": m3,
        "product_width_cm": m4
    }    
    target_median = medians_dict.get(column)    
    for row in final_datalist:
        if row[column] is None or row[column].strip() == '':
            row[column] = str(target_median)            
    return final_datalist 

def clean_standart_string_str_lo_re (name_row):    
    #PADRONIZAÇÃO: LOWERCASE E REMOÇÃO DE CARACTERES ESPECIAIS VIA REGEX
    if name_row['product_category_name'] is not None and name_row['product_category_name']!= '':
        text = name_row['product_category_name'].strip().lower()
        name_row['product_category_name'] = re.sub(r'[^\w\s]', '', text)
    return name_row