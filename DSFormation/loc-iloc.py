import pandas as pd

pd.set_option('display.max_rows', 100)    # máximo de linhas exibidas
pd.set_option('display.max_columns', 50)  # máximo de colunas exibidas
pd.set_option('display.width', 1000)      # largura máxima para quebrar linhas

df_bruto = pd.read_csv("dados/train.csv")
df = df_bruto.copy()

# Qual o valor da informação armazenada na linha 30 e na coluna 10?
print(df.iloc[30,10])

# Selecione as linhas 0 a 20 e as colunas 0 a 2
print(df.iloc[0:20,0:2])

# Seleciona as linhas 5 a 30 e a coluna “Delivery_person_Age”
print(df.loc[0:1,'Delivery_person_Age'])
 
# Selecione as linhas 40 a 42 e as seguintes colunas “Restaurant_longitude”, "Delivery_location_latitude”,  “Restaurant_latitude”, “Delivery_location_longitude”.
print(df.loc[40:42, ["Restaurant_longitude", "Delivery_location_latitude",  "Restaurant_latitude", "Delivery_location_longitude"]])
 
# Qual a menor data de entrega da coluna “ Time_Orderd ” entre as linhas 0 a 50?
df['Time_Orderd'] = pd.to_datetime(df['Time_Orderd'], errors='coerce') # Converte str para %h-%m-%s
menor_tempo = df.loc[0:50,'Time_Orderd'].min()
print(menor_tempo)

# Quais os nomes únicos da coluna “City” entre as linhas 50 e 70?
print(df.loc[50:70,'City'].unique())
 
# Quais os nomes únicos da coluna “Weatherconditions” entre as linhas 0 e 10?
print(df.loc[0:10,'Weatherconditions'].unique())

# Quais os tipos de densidade de trânsito presente na coluna “Road_traffic_density ” entre as linhas 0 a 20?
print(df.loc[0:20,'Road_traffic_density'].unique())

# Qual o ID do entregador de comida mais velho entre as linhas 50 e 70?
df['Delivery_person_Age'] = pd.to_numeric(df['Delivery_person_Age'], errors='coerce')
intervalo = df.loc[50:70]
idade_max = intervalo['Delivery_person_Age'].max()
mais_velho = intervalo[intervalo['Delivery_person_Age'] == idade_max]
entregador_id = mais_velho['Delivery_person_ID'].iloc[0]
print(entregador_id)

# Qual o ID do entregador de comida com a melhor avaliação de entrega entre as linhas 50 e 70?
df['Delivery_person_Ratings'] = pd.to_numeric(df['Delivery_person_Ratings'], errors='coerce')
intervalo = df.iloc[50:71] 
rating_max = intervalo['Delivery_person_Ratings'].max()
mais_bem_avaliado = intervalo[intervalo['Delivery_person_Ratings'] == rating_max]
entregador_id = mais_bem_avaliado['Delivery_person_ID'].iloc[0]
print(entregador_id)

# Quais os tipos de veículos utilizados pelos entregadores entre as linhas 0 a 30?
print(df.loc[0:30,'Type_of_vehicle'].unique())
 
# Quais os tipos de pedidos único que foram entregues entre as linhas 100 e 120?
print(df.loc[100:120,'Type_of_order'].unique())