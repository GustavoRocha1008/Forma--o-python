#fatiamento- Alem de acessar elementos diretamente,podemos extrair um conjunto de valoresde uma sequencia. Para isso bastar passar o indice e/ou final para acessar o conjunt, podemosa ainda informa quantas posições o curso deve "pular" no acesso
#Exemplos
lista =  ["P","Y","T","H","O","N"]
#lista[2:] #[T,H,O,N]
#lista[:2] #[P,Y]
#lista[1:3]#[Y,T]
#lista[0:3:2]#[P,T]
#lista[::] #["P","Y","T","H","O","N"]
#lista[::-1]#["N","O","H","T","Y","P"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])
