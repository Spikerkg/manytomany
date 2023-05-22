import pandas as pd

# Загрузка данных из CSV файлов в отдельные датафреймы
schet_df = pd.read_csv('tabl/schet.csv')
coustumers_df = pd.read_csv('tabl/coustumers.csv')
schetcustomer_df = pd.read_csv('tabl/schetcustomer.csv')
#print (coustumers_df) 
# Объединение таблиц с помощью pd.concat()
merged_df = pd.concat([schet_df.set_index('summa'), coustumers_df.set_index('Name'), schetcustomer_df.set_index('idschet')],  axis=1)
#print (merged_df)
# Сохранение объединенной таблицы в новый CSV файл
merged_df.reset_index().to_csv('merged_table.csv', index=False)

print(merged_df)