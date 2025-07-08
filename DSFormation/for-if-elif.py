""" 
Some o valor 1000 a todos os elementos abaixo, guarde os resultados em uma lista e mostre-os para o usuário ao final do script.
"""
lista = [10, 11, 423, 2034, 134, 11, 3, 23, 34, 758, 9, 10, 14, 2, 412, 34, 123, 4132, 4, 12, 3412, 34, 12, 34132, 41, 234, 1, 23,4, 12, 3, 41, 2, 4123]

# Versão 1
nova_lista = []
for numeros in lista:
    # print(numeros)
    numero_somado = numeros + 1000
    # print(numero_somado)
    nova_lista.append(numero_somado)

# Versão 2
nova_lista = []
for numero in lista:
    nova_lista.append(numero + 1000)
print(nova_lista)

""" 
[1010, 1011, 1423, 3034, 1134, 1011, 1003, 1023, 1034, 1758, 1009, 1010, 1014, 1002, 1412, 1034, 1123, 5132, 1004, 1012, 4412, 1034, 1012, 35132, 1041, 1234, 1001, 1023, 1004, 1012, 1003, 1041, 1002, 5123]
"""
"""
Percorra todos os elementos da lista e some 10 aos valores entre 0 e 10, multiplique por 20 os valores entre 11 e 50, subtraia 30 dos valores entre 51 e 100 e divida por 2 os valores acima de 100. 
"""
lista = [10, 52, 423, 2034, 134, 11, 3, 23, 34, 758, 9, 10, 14, 2, 412, 34, 123, 4132, 4, 12, 3412, 34, 12, 34132, 41, 234, 1, 23, 4, 12, 3, 41, 2, 4123]

# Versão 1
nova_lista = []
for numero in lista:
    if numero <= 10:
        print(numero+10)
    if (numero >= 11) and (numero <= 50):
        print(numero*20)
    if (numero >= 51) and (numero <= 100):
        print(numero-30)
    elif numero >= 100:
        print(int(numero/2))

# Versão 2
nova_lista = []
for numero in lista:
    if numero <= 10:
        nova_lista.append(numero+10)
    if (numero >= 11) and (numero <= 50):
        nova_lista.append(numero*20)
    if (numero >= 51) and (numero <= 100):
        nova_lista.append(numero-30)
    elif numero >= 100:
        nova_lista.append(int(numero/2))
print(nova_lista)   

""" [20, 22, 211, 1017, 67, 220, 13, 460, 680, 379, 19, 20, 280, 12, 206, 680, 61, 2066, 14, 240, 1706, 680, 240, 17066, 820, 117, 11, 460, 14, 240, 13, 820, 12, 2061] """

""" 
Crie um script em Python que exiba, cinquenta e duas vezes, a seguinte
mensagem “Um valor foi removido da lista”. Além disso, esse script deve
mostrar, junto com a mensagem, o número de vezes em que a mensagem foi
exibida.
 """
for i in range(1,53,1):
    print(f"{i} Um valor foi removido")

""" 
1 Um valor foi removido
2 Um valor foi removido
3 Um valor foi removido
...
51 Um valor foi removido
52 Um valor foi removido
"""