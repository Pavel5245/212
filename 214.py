import pandas as pd
import psycopg2 as psy
import pprint as pp
import string as s
dict_of_counts = {}
df = pd.read_html('C:/Users/Павел/Documents/Python/Info/Группы_Номенклатуры/Группы_Номенклатуры.htm', index_col=0, skiprows=1, encoding='utf-8')
conn = psy.connect(dbname='WhProd', user='postgres', password='adminPavel', host='localhost', port=5432)
n = 5
request = 0
printer = pp.PrettyPrinter()
cur = conn.cursor()
for row in df:
    row = row.fillna(0) 
    for index in range(len(row)):

        number_1C = str(row[1].iloc[index]).replace("\xa0", ' ')
        name = str(row[2].iloc[index]).replace("\xa0", ' ')
        parent_code = str(row[3].iloc[index]).replace("\xa0", ' ')
        if parent_code == '0' or parent_code == 0:
            
            parent_code = None
            cur.execute(
                """INSERT INTO public.inv_nomeclature_group ("number_1C", name, parent_id) VALUES (%s, %s, %s) RETURNING id""", 
                (number_1C, name, parent_code)
            )
        else:
            cur.execute(
                """INSERT INTO public.inv_nomeclature_group ("number_1C", name, parent_id) VALUES (%s, %s, %s) RETURNING id""", 
                (number_1C, name, dict_of_counts[parent_code])
            )

        insert_id = cur.fetchone()[0]
        dict_of_counts[number_1C] = insert_id

        conn.commit()
cur.close()                         
conn.close()