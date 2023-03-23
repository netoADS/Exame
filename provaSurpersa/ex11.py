#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista.
print('digite uma lista de números\n')

lista = []

for i in range(5):
    numero = int(input('digite um numero: '))
    if numero%2 == 1:
        lista.append(numero)

print('A soma dos numeros impares da lista é: ', sum(lista))