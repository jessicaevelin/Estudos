# Data: 27/06/2025
# Instalar a extensão SQLite

import sqlite3
import pandas as pd

# Cria uma base de dados
conn = sqlite3.connect('Dados/web.db')

# Importa o .csv
# Vive em memória RAM
df = pd.read_csv('Dados/bd_data.csv', index_col =0)
df.index.name ='index_name'

# Exporta o df para a base de dados SQL
# Salva no HD
df.to_sql('data',conn,index_label='index_name')

# Envia comandos para o SQL
c = conn.cursor()

# Cria uma tabela
c.execute('CREATE TABLE products (product_id, product_name, price)')
conn.commit()

# Deleta a tabela
c.execute('DROP TABLE products')
c.execute('DROP TABLE data')

# Cria uma tabela
c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')
conn.commit()

# Inserir

c.execute("INSERT INTO products (product_id, product_name, price) VALUES (?, ?, ?)", ('1', 'Computer', '800'))
c.execute("INSERT INTO products (product_id, product_name, price) VALUES (?, ?, ?)", ('2', 'Printer', '200'))
c.execute("INSERT INTO products (product_id, product_name, price) VALUES (?, ?, ?)", ('3', 'Notebook', '600'))
conn.commit()

# Criando um novo data frame que será empilhado
df2 = df.iloc[::-2]
df2['index_name'] = [1000,2000,3000,4000,5000]
df2.set_index('index_name', inplace=True)

# Coloando o df2 embaixo do df
# Append, Fail ou Replace
df2.to_sql('data', conn, if_exists = 'append')

# Envia comandos para o SQL
c = conn.cursor()

# Select
c.execute('SELECT * FROM data')
# Transformando em DF
# O fetch só pode ser chamado uma vez depois do execute
df3 = pd.DataFrame(c.fetchall())
df3

# Condicional 
# Exibe a primeira linha em tupla
c.execute('SELECT * FROM data WHERE A > 210')
c.fetchall()

c.execute('SELECT * FROM data WHERE A > 210 AND B > 225')
c.fetchall()
