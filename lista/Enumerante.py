#Função enumerante -  As vezes e necessario sabe qual o indice do objetvo dentro do laço for, para isso  usa a função enumerate
#Função enumerate() para iterar sobre uma sequência (como uma lista, tupla ou string) ao mesmo tempo em que acessa tanto o índice quanto o valor de cada elemento da sequência.

car_model = ["celta", "fox", "polo","Prisma"]

for indice, car_model in  enumerate(car_model):
    print(f"indice: {indice}, car_model:{car_model}")


lista = ["Calca","Camisa","bone", "Luva"]
for indice, lista in enumerate(lista):
    print(f"\n indice: {indice}, lista:{lista}")