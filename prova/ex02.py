#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a".
print('escreva uma lista de palavras\n')

lista = []
newLista = []

for i in range(10):
    lista.append(str(input('escreva uma palavra: ').capitalize()))

for x in lista:
    if x[0] == 'A':
        newLista.append(x)

print("As palavras com a letra 'A' são:", newLista)