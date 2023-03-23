#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, crie uma nova lista que contenha apenas as palavras que têm um número ímpar de letras.

print('escreva uma lista de palavras\n')
lista = []
newLista = []
n = 0
for i in range(5):
    lista.append(str(input('Digite um nome: ')))

for x in lista:
    num = len(lista[n])
    if num%2 == 1:
        newLista.append(lista[n])
    n+=1

print('lista com palavras com numero impar de letras: ',newLista)