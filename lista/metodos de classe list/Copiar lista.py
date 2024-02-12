#[].copy  -copiar lista 
#cria uma cópia superficial da lista, o que significa que ele cria uma nova lista contendo os mesmos elementos da lista original. Se a lista original contiver objetos mutáveis (como outras listas), as alterações feitas nos elementos mutáveis da cópia afetarão a lista original e vice-versa. Se você precisar de uma cópia profunda (onde cada objeto na nova lista é uma cópia do objeto correspondente na lista original), você pode usar o módulo copy e sua função deepcopy()
lista = [1, "Python", [40,30,20]]
Nova_lista = lista.copy()
print ( id (Nova_lista), id (lista))