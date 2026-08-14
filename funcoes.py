data = []
def product_validations(csv_row):
    # VALIDACAO E TRATAMENTO DE DADOS AUSENTES - COL_PRODUCT_CATEGORY_NAME
    if csv_row['product_category_name'].strip() == '':
        csv_row['product_category_name'] = 'Sem Categoria' #CASO O NOME DA CATEGORIA ESTEJA VAZIO, ATRIBUIR O VALOR 'Sem Categoria'
    else:
        csv_row['product_category_name'] = csv_row['product_category_name'].strip()   
    return csv_row

def sort_cols_median_preparation(column_name):
    return sorted([
        float(row[column_name]) 
        for row in data if row[column_name] is not None and row[column_name].strip() != ''
        ])

def calculate_median(sorted_list):
    n = len(sorted_list)
    if n == 0:
        return None
     # Se a quantidade de elementos for ímpar, pega o elemento do meio exato
    if n % 2 != 0:
        return sorted_list[n // 2]
    # Se for par, faz a média dos dois elementos centrais
    else:
        mid1 = sorted_list[(n // 2) - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2
