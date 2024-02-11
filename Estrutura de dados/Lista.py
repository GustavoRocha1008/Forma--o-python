#A lista ela tem capacitadade de armazena qualquer informação

frutas = ["laranja", "maca","uva"]
print(frutas)

Fruta = []
print(Fruta)

letras = list("Python")
print(letras)

numero = list(range(10))
print(numero)

carro =["Ferrari","F8",450000,2020,2900,"São paulo", True]
print(carro)


#Acesso direto -  lista e uma sequncia , portanto podemos  acessar seus dados utilizando indices. contamos o indice de detrminada sequencia zero
#Exemplos
frutas1 = ["maça","laranja","uva","pera"]
frutas1[0] #maça
Frutas1[1] #laranja
frutas1[2] #uva
frutas1[3] #pera

#indices negativos - sequencia  suportam indexação negativa. A contagem  comeca -1
#Exemplos
frutas2 = ["maça","laranja","uva","pera"]
frutas2 = [-1] #pera
frutas2 = [-3] #laranja

#lista aninhada - Podemos armazenar todos os tipos de objetos python, portanto podemos ter a lista que armazenam  outras lista, Com isso podemos criar estruturas bidimensionais (tabelas) e acessar informando os indices de linha coluna
#Exemplos
matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"],
]
matriz [0] # [1,"a",2]
matriz [0][0] #1
matriz [0][-1] #2
matriz [-1][-1] # "C"

#fatiamento- Alem de acessar elementos diretamente,podemos extrair um conjunto de valoresde uma sequencia. Para isso bastar passar o indice e/ou final para acessar o conjunt, podemosa ainda informa quantas posições o curso deve "pular" no acesso
#Exemplos
lista =  ["P","Y","T","H","O","N"]
lista[2:] #[T,H,O,N]
lista[:2] #[P,Y]
lista[1:3]#[Y,T]
lista[0:3:2]#[P,T]
lista[::] #["P","Y","T","H","O","N"]
lista[::-1]#["N","O","H","T","Y","P"]