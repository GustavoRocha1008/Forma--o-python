#criando dicionario 
#e um conjunto  não-ordenado de pares chaves:valor

#programa 1
print("---boa tarde---")
info = input("digita seu nome:")
info1 = input("digite sua idade:")
pessoas = {f" seu nome e": info , "idade": info1}
print(pessoas)


#programa 2
# Criação do dicionário 'pessoas'
pessoas = {"nome": "Gustavo", "idade": 20}
# Adição de um novo par chave-valor ao dicionário 'pessoas'
pessoas["telefone"] = "40028922"
# Impressão do dicionário 'pessoas' para verificar o resultado
print(pessoas)



#programa 3
#dicionarios aninhandos - pode adicionar qualquer infor desde que a chave seja imutavel 
Contatos = {
    "hadassa_aragao@greenbikeshop.com.br": {"nome":"Hadassa Esther Aragão", "idade":"19","telefone":"(61) 3505-7672" "\n" },
    "luciana-caldeira79@paginacom.com.br": {"nome":"Luciana Sueli Maria Caldeira", "idade":"20","telefone":"(92)2786-7921"}
}
#Alteração informmação
Contatos["hadassa_aragao@greenbikeshop.com.br"]["telefone"]="11949225187"
Contatos["hadassa_aragao@greenbikeshop.com.br"]["nome"] = "DEU CERTO"
print(Contatos)

#consulta informação 
acesso = Contatos ["hadassa_aragao@greenbikeshop.com.br"]["telefone"]
print(acesso)

#interar dicionario  - a forma mais comum e utilizar o comando for 
for email, info_Contatos in Contatos.items():
    print(email, info_Contatos["nome"])


for chave in Contatos:
    print(chave, Contatos[chave])