#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por 3.
print('Escreva uma lista de numeros\n')

lista = []
for i in range(10):
    numero = int(input('Insira um numero: '))
    if numero%3 == 0:
        lista.append(numero)

print('os numeros divisiveis por 3 são: ', lista)