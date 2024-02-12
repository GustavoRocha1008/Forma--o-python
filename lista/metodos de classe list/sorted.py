#[].sorted -Em Python, a função sorted() é usada para ordenar iteráveis (como listas, tuplas, dicionários, etc.) e retorna uma nova lista contendo os elementos ordenados. Ao contrário do método sort() que ordena a lista original in-place, a função sorted() não modifica o objeto original e sim retorna uma nova lista ordenada.
lista  = [1,2,3,4,5,6,7,8,9,10]
lista_new = sorted(lista)
print(lista_new)