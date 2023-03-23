#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.
print('Digita uma lista de números\n')

lista = []

for i in range(5):
    lista.append(int(input('Digite um numero: ')))
    
print('numero minimo:', min(lista))
print('numero maximo:', max(lista))