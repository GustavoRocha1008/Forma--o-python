#lista aninhada - Podemos armazenar todos os tipos de objetos python, portanto podemos ter a lista que armazenam  outras lista, Com isso podemos criar estruturas bidimensionais (tabelas) e acessar informando os indices de linha coluna
#Exemplos
matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"],
]

print(matriz[0]) # [1,"a",2]
print(matriz[0][0]) #1
print(matriz[0][-1]) #2
print(matriz[-1][-1]) # "C"