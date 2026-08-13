import csv
import re
import datetime



def read_data(csv_row):
    for key, value in csv_row.items():
        if csv_row['product_category_name'].strip() == '':
            csv_row['product_category_name'] = 'Sem Categoria'
        else:
            csv_row['product_category_name'] = value.strip()   
    return csv_row

with open ('olist_products_dataset.csv', 'r', encoding='utf-8') as f:
    data = csv.DictReader(f)
    for row in data:
        print(read_data(row))
