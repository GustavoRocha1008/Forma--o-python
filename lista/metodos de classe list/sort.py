#[].sort  -sado para ordenar os elementos de uma lista em ordem crescente ou alfabética. Este método modifica a lista original e não retorna um novo objeto.
#Se você quiser ordenar a lista em ordem decrescente, você pode usar o argumento opcional reverse=True.


lista = [1,2,3,4,5,6,7,8,9,10,11,12]
#lista crescente
lista.sort()
#Lista descrente 
lista.sort(reverse=True)
print(lista)