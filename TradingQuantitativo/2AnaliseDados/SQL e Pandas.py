# Data: 28/06/2025
# Trabalhando com SQL e Pandas

import sqlite3
import pandas as pd

# Cria uma base de dados
conn = sqlite3.connect('Dados/web.db')

# Envia comandos para o SQL
c = conn.cursor()

# Importa o .csv
# Vive em memória RAM
df = pd.read_csv('Dados/bd_data.csv', index_col =0)
df.index.name ='index_name'
df = df.iloc[0:10,:]
# Exporta o df para a base de dados SQL
# Vive no HD dentro da base de dados (web.db > dados)
df.to_sql('data',conn,index_label='index_name', if_exists = 'replace')
df

# Importando do banco de dados a tabela data
query = 'SELECT * FROM data'
df_data = pd.read_sql(query,con=conn,index_col='index_name')
df_data


# Update e Delete
c.execute("UPDATE data SET A=99999 WHERE index_name='b'")
conn.commit()

c.execute("UPDATE data SET A=99999, B=56565656 WHERE index_name='b'")
conn.commit()

c.execute("DELETE FROM data WHERE index_name='b'")
conn.commit()