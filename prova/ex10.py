#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista com os números duplicados removidos.
print('Escreva uma lista de numeros\n')
lista = []
for i in range(10):
    lista.append(int(input('digite um numero: ')))

dup = [x for i, x in lista if i != lista.index(x)]
print('os numeros duplicados são: ',dup)