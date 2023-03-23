#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, crie uma nova lista que contenha apenas os nomes que contêm a letra "e".

print('escreva uma lista de palavras\n')

lista = []
newLista = []
for i in range(10):
    lista.append(str(input('escreva uma palavra: ').capitalize()))
for x in lista:
    if x[0] == 'E':
        newLista.append(x)
print("As palavras com a letra 'E' são:", newLista)