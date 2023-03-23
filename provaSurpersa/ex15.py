#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, remova todos os números duplicados da lista e imprima a nova lista.
print('digite uma lista de numeros\n')

lista = []
for i in range(10):
    lista.append(int(input('Digite um numero: ')))
    lista.sort()

newLista = set(lista)
print('nova lista sem numeros duplicados: ', newLista)