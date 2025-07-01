import pandas as pd
import psycopg2 as psy
import pprint as pp
import string as s

df = pd.read_html('C:/Users/Павел/Documents/Python/Info/Контрагенты/Контрагенты.htm', index_col=0, skiprows=1, encoding='utf-8')
conn = psy.connect(dbname='WhProd', user='postgres', password='adminPavel', host='localhost', port=5432)
n = 0
printer = pp.PrettyPrinter()
cur = conn.cursor()
for row in df:

    for index in range(len(row)):

        name = str(row[3].iloc[index]).replace("\xa0", ' ')
        inn = str(row[4].iloc[index]).replace("\xa0", ' ')
        manager = str(row[6].iloc[index]).replace("\xa0", ' ')

        # printer.pprint(name)
        # n += 1
        # if n == 10:
        #     break
        cur.execute(
            'INSERT INTO inv_partner (name, "INN", manager) VALUES (%s, %s, %s)',
                (name, inn, manager)
        )
conn.commit()
cur.close()
conn.close()