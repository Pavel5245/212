import pandas as pd
import psycopg2 as psy
import pprint as pp


df = pd.read_html('C:/Users/Pavel/Documents/Data/Nomeclature.htm', index_col=0, skiprows=1, encoding='utf-8')
conn = psy.connect(dbname='WhProd', user='postgres', password='adminPavel', host='localhost', port=5432)
printer = pp.PrettyPrinter()
cur = conn.cursor()

cur.execute(
            """SELECT "number_1C", id FROM public.inv_nomeclature_group;""", 
        )
import_rows = dict(cur.fetchall())

for row in df:
    row = row.fillna(0) 
    for index in range(len(row)):

        number_1C = str(row[1].iloc[index]).replace("\xa0", ' ')
        sku = str(row[2].iloc[index]).replace("\xa0", ' ')
        name = str(row[3].iloc[index]).replace("\xa0", ' ')
        parent_code = str(row[4].iloc[index]).replace("\xa0", ' ')
        is_group = str(row[5].iloc[index]).replace("\xa0", ' ')
        if is_group == 'Да':
            pass
        else:

            cur.execute(
                """INSERT INTO public.inv_nomeclature ("number_1C", name, parent_id) VALUES (%s, %s, %s)""", 
                (number_1C, name, import_rows[parent_code])
            )
conn.commit()
cur.close()                         
conn.close()