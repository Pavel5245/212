import pandas as pd
import psycopg2 as psy
import pprint as pp
df = pd.read_html('C:/Users/Pavel/Documents/Partners.htm', index_col=0)
conn = psy.connect(dbname='WhProd', user='postgres', password='adminPavel', host='localhost', port=5432)
n = 0
cur = conn.cursor()
for row in df:
            
            val = row[3].to_string(header=False, index=False, na_rep='Not')
            # n += 1
            print(val)
            cur.execute(
                'INSERT INTO inv_partner ("Name") VALUES (%s)',
                (val)  
                )

conn.commit()
cur.close()            

conn.close()  