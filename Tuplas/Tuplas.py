#A  tupla são estrutura de dados, a diferença da tuplas para a lista, a tupla e mais restrita e um função inmutavel
#A tupla não conseguimos alterar os dados informados, para criar a tupla podemos utilizar classe  tuple ou colocando valores separados por vingulas 


frutas = ("laranja","maça","banana",)
frutas1 = tuple(frutas)
print(frutas1)
#Como acessar a tupla
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])

numero = tuple ([1,2,3,4,5,6])
print(numero)
#Como acessar a tupla
print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])
print(numero[4])
print(numero[5])
#ordem inversa
print(numero[-1])
print(numero[-2])

pais = ("brasil",)
#Como acessar a tupla
print(pais[0])
print(pais)


#Tuplas aninhada - podemos ter dentro de um tupla outras tuplas, com isso conseguimos criar tabelas
#utilizamos a tupla por conta garantia que não vai ser alterada
TABELA1 = [
    ("Gustav","alves", "rocha",),
    ("Celta", "Palio", "Corsa",),
    ("MT03", "MT07","MT09",),
    (18, 19, 20),
]

print(TABELA1[0])
print(TABELA1[1])
print(TABELA1[2])
print(TABELA1[3])

#Acessando  informações na tabela 0
print(TABELA1[0][0])
print(TABELA1[0][2])
print(TABELA1[0][1])

#utilizando count 
my_tuple = ("GU","RO","GU","MA","GU")
Contagem = my_tuple.count("GU")
print(Contagem)