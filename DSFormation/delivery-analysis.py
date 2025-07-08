import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 100)    # máximo de linhas exibidas
pd.set_option('display.max_columns', 50)  # máximo de colunas exibidas
pd.set_option('display.width', 1000)      # largura máxima para quebrar linhas

df_bruto = pd.read_csv("dados/train.csv")
df = df_bruto.copy()

print(df.shape)

print(f"{df.iloc[0:2,0:6]}\n")
print(f"{df.iloc[0:2,7:13]}\n")
print(f"{df.iloc[0:2,14:21]}\n")

# Qual o número total de entregadores cadastrados na base de dados?
print(pd.DataFrame(df.loc[:,'ID']).count())

# Qual o número total de entregadores únicos cadastrados na base de dados?
id_unico = pd.DataFrame(df.loc[:, 'ID'].unique())
print(id_unico.count())
 
# Qual a idade do entregador mais velho? E do mais novo?
df['Delivery_person_Age'] = pd.to_numeric(df['Delivery_person_Age'], errors='coerce')
print(df.loc[:,'Delivery_person_Age'].max())
print(df.loc[:,'Delivery_person_Age'].min())

# Qual o ID do entregador com a maior idade? E o ID do entregador com a menor idade?
df['Delivery_person_Age'] = pd.to_numeric(df['Delivery_person_Age'], errors='coerce')
print(df[df['Delivery_person_Age'] == df.loc[:,'Delivery_person_Age'].max()].loc[:,['ID', 'Delivery_person_Age']])

# Quais os nomes das condições climáticas?
df['Weatherconditions'] = df['Weatherconditions'].str.replace('conditions ', '', regex=False)
print(df.loc[:,'Weatherconditions'].unique())

# Quantas entregas foram realizadas sob condições climáticas de tempestade de areia (Sandstorms)?
agrupado = df.groupby('Weatherconditions')['Weatherconditions'].count()
print(agrupado)
print(agrupado.sum())

# Quais eram as condições climáticas da data mais recente de entrega?
df['Order_Date'] = pd.to_datetime(df['Order_Date'],format="%d-%m-%Y", errors='coerce') # Converte str para %d-%m-%Y
df['Time_Orderd'] = pd.to_datetime(df['Time_Orderd'],format="%H:%M:%S", errors='coerce') # Converte str para %h-%m-%s
menor_data = df.loc[:,'Order_Date'].min()
menor_hora = df.loc[:,'Time_Orderd'].min()
print(df[(df['Order_Date'] == menor_data) & (df['Time_Orderd'] == menor_hora)])

# Quantos tipos de densidade de trânsito existem na base de dados? Quais os nomes delas?
print(df.loc[:,'Road_traffic_density'].unique())

# Quantas entregas foram feitas em cada condição climática?
agrupado = df.groupby('Weatherconditions')['Weatherconditions'].count()
print(agrupado)

# Quantos entregadores únicos fizeram entregas em cada condição climática?
agrupado = df.groupby('Weatherconditions')['ID'].count()
print(agrupado)

# Quantas entregas foram feitas em cada tipo de densidade de trânsito?

df['multiple_deliveries'] = df['multiple_deliveries'].astype(str).str.strip()
df['multiple_deliveries'] = df['multiple_deliveries'].replace(['NaN', 'nan', ''], np.nan)
df['multiple_deliveries'] = df['multiple_deliveries'].fillna(1)
df['multiple_deliveries'] = df['multiple_deliveries'].astype(int)
df.loc[df['multiple_deliveries'] == 0, 'multiple_deliveries'] = 1
total_entregas_reais = df.groupby('Road_traffic_density')['multiple_deliveries'].sum()
print(total_entregas_reais)

# Quantos entregadores únicos fizeram entregas em cada tipo de densidade de trânsito?
print(df.groupby('Road_traffic_density')['Road_traffic_density'].count())

# Quantas cidades únicas existem na base? Quais são os seus nomes?
print(df.loc[:,'City'].unique())

# Quantos tipos de veículos únicos existem na base?
print(df.loc[:,'Type_of_vehicle'].unique())
 
# Qual o tipo de veículo que mais fez entregas com a condição de trânsito pesado (High)?
df_high = df[df['Road_traffic_density'] == 'High ']
contagem_high = df_high.groupby('Type_of_vehicle')['Road_traffic_density'].count()
print(contagem_high)

# Qual o tipo de pedido mais feito durante condições climáticas de tempestade de areia?
df_Sandstorms = df[df['Weatherconditions'] == 'conditions Sandstorms']
Sandstorms = df_Sandstorms.groupby('Type_of_order')['Weatherconditions'].count()
print(Sandstorms)

# Qual o nome da cidade com o(s) entregador(es) mais velho(s)? E o nome da cidade com o(s) entregador(es) mais novo(s)?
df['Delivery_person_Age'] = pd.to_numeric(df['Delivery_person_Age'], errors='coerce')
print(df[df.loc[:,'Delivery_person_Age'] == df.loc[:,'Delivery_person_Age'].max()].loc[:,'City'].unique())
print(df[df.loc[:,'Delivery_person_Age'] == df.loc[:,'Delivery_person_Age'].min()].loc[:,'City'].unique())

# Qual a cidade com o maior número de pedidos de Bebidas (Drinks) feitos em Scooter?
# print(df.groupby('Type_of_order').grou)
df_drinks = df[df.loc[:,'Type_of_order'] == 'Drinks ']
print(df_drinks.groupby('Type_of_vehicle')['Type_of_order'].count())

# Quantas entregas foram feitas durante o Festival?
df['multiple_deliveries'] = df['multiple_deliveries'].astype(str).str.strip()
df['multiple_deliveries'] = df['multiple_deliveries'].replace(['NaN', 'nan', ''], np.nan)
df['multiple_deliveries'] = df['multiple_deliveries'].fillna(1)
df['multiple_deliveries'] = df['multiple_deliveries'].astype(int)
df.loc[df['multiple_deliveries'] == 0, 'multiple_deliveries'] = 1
total_entregas_reais = df.groupby('Festival')['multiple_deliveries'].count()
print(total_entregas_reais)

# Quantas cidades únicas tiveram entregas feitas durante o Festival?
df_festival = df[df.loc[:,'Festival'] == "Yes "]
print(df_festival.groupby('multiple_deliveries')['multiple_deliveries'].count())
