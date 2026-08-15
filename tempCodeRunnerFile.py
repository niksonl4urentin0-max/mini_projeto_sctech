print()
print(f'{'-'*100} LISTA DE PEDIDOS CANCELADOS {'-'*100}', sep='\n\n')
print(*list_canceled_orders, sep='\n')
print("-" * 300)

#5. Relatório de Status Manual:
print('SUMÁRIO ESTATÍSTICO')
print(f'Total de linhas processadas: {total_processed_rows}') 
print(f'Valores nulos tratados: {count_null}')
print(f'Total de pedidos cancelados: {canceled_order}')