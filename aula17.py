lista = [2, 5, 9, 1]
lista[1] = "pistache"
print(lista)
print(lista[1])
lista[1] = "azeitona"
print(lista[1])
print(lista)
lista.append("pizza")
print(lista)
lista[4] = "pepperoni"
print(lista)
lista2 = [1, 4, 3, 8, 0]
lista2.sort(reverse=True)       # coloca a lista em ordem decrescente
print(lista2)
lista2.sort()   # coloca a lista em ordem crescente
print(lista2)
print(f'Esta lista tem {len(lista2)} elementos.')
lista2.insert(3, "pistache")    # adiciona o elemento descrito no campo selecionado
print(lista2)
lista2.pop(1)       # deleta o elemento selecionado
print(lista2)
# lista2.remove(4)    # remove apenas o elemento selecionado
# print(lista2)
if 5 in lista2:
    lista2.remove(5)
else:
    print("Categoria inexistente")
