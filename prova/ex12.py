#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, verifique se um determinado nome está na lista. Se estiver, imprima "O nome está na lista"; caso contrário, imprima "O nome não está na lista".

print('digite uma lista de nomes\n')

lista = []
verifica = 'Maria'
for i in range(5):
    lista.append(str(input('Digite um nome: ')).capitalize())

for x in lista:
    if verifica == x:
        print('O nome está na lista')
    else:
        print('O nome não está na lista')