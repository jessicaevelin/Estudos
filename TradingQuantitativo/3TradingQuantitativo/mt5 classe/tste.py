import json

file_path = '3TradingQuantitativo\mt5 classe\pass.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    linhas = [linha.strip() for linha in f.readlines()]

login = linhas[0]
senha = linhas[1]
servidor = linhas[2]

print(login, senha, servidor)
