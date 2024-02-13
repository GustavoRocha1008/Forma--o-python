#Set - uma coleção não possui objetos repetidos, e nem sempre ele segue a ordem da lista    
#Quando utilizando SET ? 
#R: PARA CONJUNTOS MATEMATICOS OU ELIMINAR ITENS DUPLICADOS  DE UM INTERAVEL


carros = set(["Polo","Polo", "Corsa","Corsa", "jetta","jetta",])
print(carros) #deve aparecer Polo,corsa,jetta

lista1 = set(["fusca","fusca"])
print(lista1) #Deve aparecer apenas fusca

letras = set("Gustavo") 
print(letras)#deve apresenta #{G,U,S,T,A,V,O}

animal = {"leão","leão"}
print(animal)# deve apresenta o nome do animal


#conjunto em python não suportam indexacão e nem fatiamento, para fazer isso temos que converte o conjunto
#para lista  
number = {1,2,3,4,5,6,7,8,9,10} # set
transforma = list(number)#convertendo conjunto com para  lista
print(transforma[2])# exibindo o que foi solicitado 


#inter conjunto com o for
carros = ("Polo","civic","jetta")

for carro in carros:
    print(carros)

for indice, modelo in enumerate(carros):
    print(f"{indice} e {modelo}")

for carros in carros:
    print(carros)


# {}.union - união de conjunetos 
modelo_a = {1,2,3}
modelo_b = {3,4,5}

união = modelo_a.union(modelo_b)#União do modelo
print(união)#mostrando a união na tela

modelo_c = {"CAR"}#modelo    C
Modelo_d = {"RO"}#Modelo     D 
Modelo_E = {"E",2010}#modelo E

união_2 = modelo_c.union(Modelo_d)#Juntando o modelo D ao C
união_3 = união_2.union(Modelo_E)#Juntando modelo E ao C e D
print(união_3)#Mostrando a união dos conjuntos 

#{}.intersction  -  
nomes = {"GUSTAVO","Augusto","eliane"}#lista1
nomess1 = {"GUSTAVO","mariana","Augusto"}#lista2

juntos = nomes.intersection(nomess1) #jução da lista e o sitema so mostrar os dados iguais nas duas lista 
print(juntos)

#{}.difference - dados diferente do conjunto 
nomes0 = {"GUSTAVO","Augusto","eliane"}#lista1
nomess2 = {"GUSTAVO","mariana","Augusto"}#lista2

juntos1 = nomes0.difference(nomess2)
juntos2 = nomess2.difference(nomes0)
print(juntos1)
print(juntos2)


#symmetric_difference
nomes3 = {"GUSTAVO","Augusto","eliane"}
nomes4 = {"GUSTAVO","mariana","Augusto"}

juntos3 =  nomes3.symmetric_difference (nomes4)
print(juntos3)


#issubset

nomes5 = {"GUSTAVO","Augusto","eliane"}#lista1
nomes6 = {"GUSTAVO","mariana","Augusto"}#lista2

validacao = nomes5.issubset(nomes6)
validacao1 = nomes6.issubset(nomes5)
 
print(validacao)
print(validacao1)

# {}.add - adicionar dados a lista
frutas = {"maça",}
frutas.add("banana")
print(frutas)




