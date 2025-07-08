import pandas as pd
usuarios = {
	"nome" : ["Meigarom", "Claudio", "Fernando", "Diego", "André"],
	"idade" : [34, 30, 36, 25, 36],
	"cidade" : ["Indaiatuba", "Arcos", "Ouro Fino", "Itapira", "Curitiba"],
	"estado": ["SP", "RJ", "SP", "RJ", "RJ"]
	}
df = pd.DataFrame(usuarios)

print(df)
"""        
nome  idade      cidade estado
0  Meigarom     34  Indaiatuba     SP
1   Claudio     30       Arcos     RJ
2  Fernando     36   Ouro Fino     SP
3     Diego     25     Itapira     RJ
4     André     36    Curitiba     RJ 
"""

# Seleciona a primeira linha e primeira coluna 
df_selecionado = df.iloc[0, 0]
print( df_selecionado ) 
""" 
Meigarom 
"""

# Selecionar primeira linha e um intervalo de coluna 
df_selecionado = df.iloc[0, 1:3] 
print( df_selecionado) 
""" 
idade             34
cidade    Indaiatuba
Name: 0, dtype: object
"""

 # Selecionar um intervalo de linha e uma coluna 
df_selecionado = df.iloc[0:9999, 3] 
print( df_selecionado ) 
""" 
0    SP
1    RJ
2    SP
3    RJ
4    RJ
Name: estado, dtype: object 
"""

# Selecionar um intervalo de linha e um intervalo de coluna 
df_selecionado = df.iloc[0:99999, 2:99999] 
print( df_selecionado ) 
""" 
    cidade estado
0  Indaiatuba     SP
1       Arcos     RJ
2   Ouro Fino     SP
3     Itapira     RJ
4    Curitiba     RJ
"""

# Selecionar um intervalo de linha e uma coluna pelo nome 
df_selecionado = df.loc[1:2,"cidade"] 
print( df_selecionado ) 
""" 
1        Arcos
2    Ouro Fino
Name: cidade, dtype: object
"""

# Selecionar um intervalo de linha e várias coluna pelo nome 
colunas = ["idade", "estado", "cidade"] 
df_selecionado = df.loc[3:25, colunas ] 
print( df_selecionado ) 
"""    
    idade estado    cidade
3     25     RJ   Itapira
4     36     RJ  Curitiba
"""
df_bruto = pd.read_csv("./dados/train.csv")
df = df_bruto.copy()

# Sempre fazer um backup
df = df.copy()

## Dimensões: Linhas e colunas
print(df.shape)
""" 
(4467, 20)
 """

## Primeiras e últimas linhas
print(df.head(1))
print(df.tail(2))
""" 
ID Delivery_person_ID Delivery_person_Age  ... Festival    City  Time_taken(min)
0  0x4     INDORES13DEL02                   37  ...      No   Urban          (min) 24 
[1 rows x 20 columns]

           ID Delivery_person_ID Delivery_person_Age  ... Festival    City  Time_taken(min)
4465  0x3     INDORES13DEL03                   34  ...      No   Urban          (min) 22
4466  0xd      KNPRES03DEL03                   33  ...       No     NaN              NaN
[2 rows x 20 columns] 
"""

## Tipo de coluna
print(df.dtypes)
""" 
ID                              object
Delivery_person_ID              object
Delivery_person_Age             object
Delivery_person_Ratings         object
Restaurant_latitude            float64
Restaurant_longitude           float64
Delivery_location_latitude     float64
Delivery_location_longitude    float64
Order_Date                      object
Time_Orderd                     object
Time_Order_picked               object
Weatherconditions               object
Road_traffic_density            object
Vehicle_condition                int64
Type_of_order                   object
Type_of_vehicle                 object
multiple_deliveries             object
Festival                        object
City                            object
Time_taken(min)                 object
dtype: object
"""

## Valores únicos
print(df['Delivery_person_Age'].unique())
""" 
['37' '34' '23' '38' '32' '22' '33' '35' '36' '21' '24' '29' '25' '31'
 '27' '26' '20' 'NaN ' '28' '39' '30' '15' '50'] 
"""

## Ordenar de acordo com uma coluna
df.sort_values("Delivery_person_Age", ascending=True)

## Somar todas as linhas
df['Delivery_person_Age'].sum()

## Média
df['Delivery_person_Age'].mean()

## Converter o tipo
df['Delivery_person_Age'].astype(float)

## Converte para datas
pd.to_datetime(df['Delivery_person_Age'], format="%d-%m-%Y")