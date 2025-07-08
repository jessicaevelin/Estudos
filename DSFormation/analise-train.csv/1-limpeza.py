import pandas as pd
pd.set_option('display.max_rows', 100)    # máximo de linhas exibidas
pd.set_option('display.max_columns', 50)  # máximo de colunas exibidas
pd.set_option('display.width', 1000)      # largura máxima para quebrar linhas

df_bruto = pd.read_csv("./dados/train.csv")
df = df_bruto.copy()

print("Data Frame bruto")
print(df.dtypes)
print(f"{df.iloc[0:2,0:6]}\n")
print(f"{df.iloc[0:2,7:13]}\n")
print(f"{df.iloc[0:2,14:21]}\n")

# Remove as observações com idade faltando
linhas = (df['Delivery_person_Age'] != 'NaN ')
df = df.loc[linhas, :].copy()

# Converte texto para número
df['Delivery_person_Age'] = df['Delivery_person_Age'].astype(int)
df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].astype(float)

# Converte texto para data
df['Order_Date'] = pd.to_datetime(df['Order_Date'],format = "%d-%m-%Y")

# Converte texto para número
linhas = (df['Delivery_person_Age'] != 'NaN ')
df = df.loc[linhas, :].copy()

# Converte texto para número
linhas = (df['multiple_deliveries'] != 'NaN ')
df = df.loc[linhas, :].copy()

df['multiple_deliveries'] = df['multiple_deliveries'].astype(int)

# Remove os espaços no final das strings
# Strip() remove espaços antes e depois da string
df.loc[:,'ID'] = df.loc[:,'ID'].str.strip()
df.loc[:,'Road_traffic_density'] = df.loc[:,'Road_traffic_density'].str.strip()
df.loc[:,'Type_of_order'] = df.loc[:,'Type_of_order'].str.strip()
df.loc[:,'Type_of_vehicle'] = df.loc[:,'Type_of_vehicle'].str.strip()
df.loc[:,'City'] = df.loc[:,'City'].str.strip()
df.loc[:,"Time_taken(min)"] = df.loc[:,"Time_taken(min)"].str.replace("(min) ", "")

print("Data Frame limpo")
print(df.dtypes)
print(f"{df.iloc[0:2,0:6]}\n")
print(f"{df.iloc[0:2,7:13]}\n")
print(f"{df.iloc[0:2,14:21]}\n")

# Salvando o df em um arquivo pickle
df.to_pickle("./dados/train-limpo.pkl")
