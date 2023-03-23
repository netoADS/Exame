#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.

print('Escreva uma lista de nomes\n')

lista = []
quant = []
n=0
for i in range(5):
    lista.append(str(input('Digite um nome: ')))

for x in lista:
    quant.append(len(lista[n]))
    n+=1

for u in lista:
    if min(quant) == len(u):
        print('menor nome:', u)
    if max(quant) == len(u):
        print('maior nome:', u)