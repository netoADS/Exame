#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.
print('Escreva uma lista de numeros\n')

lista = []
for i in range(10):
    lista.append(int(input('digite um numero: ')))
 
newList = [x for i, x in enumerate(lista) if i != lista.index(x)]
print('nova lista somente com numeros duplicados: ', newList)