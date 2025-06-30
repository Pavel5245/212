import pandas as pd
import psycopg2 as psy
import pprint as pp
df = pd.read_html('C:/Users/Павел/Documents/Python/Info/Поступления/Склады.htm', index_col=0)
conn = psy.connect(dbname='WhProd', user='postgres', password='adminPavel', host='localhost', port=5432)
n = 0
printer = pp.PrettyPrinter()
cur = conn.cursor()
for row in df:

    for index in range(len(row)):
        # printer.pprint(object=row[1].iloc[index])
        cur.execute(
            'INSERT INTO inv_wirehouse ("number_1C", "name") VALUES (%s, %s)',
                (row[1].iloc[index], row[2].iloc[index])
        )
conn.commit()
cur.close()
conn.close()