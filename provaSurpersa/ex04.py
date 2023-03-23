#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule a média dos números na lista.

print('digite uma lista de números\n')

lista = []
for i in range(5):
    lista.append(int(input('Digite um numero: ')))

print('A média dos números na lista é: ',sum(lista)/len(lista))