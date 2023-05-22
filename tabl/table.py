import pandas as pd

# Загрузка данных из CSV файлов в отдельные датафреймы
schet_df = pd.read_csv('tabl/schet.csv')
coustumers_df = pd.read_csv('tabl/coustumers.csv')
schetcustomer_df = pd.read_csv('tabl/schetcustomer.csv')

# Объединение таблиц с помощью pd.concat()
merged_df1 = pd.merge(schet_df, schetcustomer_df, on="idschet")

final_table = pd.merge(merged_df1, coustumers_df, on='coustumersid')
# Сохранение объединенной таблицы в новый CSV файл
#merged_df.reset_index().to_csv('merged_table.csv', index=False)

print(final_table)