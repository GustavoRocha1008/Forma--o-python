#fomos contratados para  por um grande banco para desenvolver o seu novo sistema.
#Esse banco deseja monetizar suas operações e para isso escolheu a liguagem python
#Para a primeira versão do sistema devemos implementar apenas 3 operadores:
#Deposito,saque,extrato
#Pode passar valores positivo - inteiro e positivo
#Deve permite 03 saque diarios de 500 e tem que esta registrado mno extrato de saque
#Extrato deve ser exibido o saldo atual da conta e as transações

#Menu interativo 
menu = """

[s] Sacar
[d] Deposito
[e] Extrato
[Q] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_Saque = 0
Limite_de_saque = 3


while true:
    opção = input (menu)
    if opcao == "s":
        valor = float(input("Digite o valor que deseja sacar:  "))

        excedeu_saldo  = valor > saldo
        excedeu_limite = valor > Limite_de_saque
        excedeu_saque  = numero_de_Saque >=Limite_de_saque

        if excedeu_saldo:
            print("Operação falhou! saldo insuficiente")

        elif excedeu_limite:
            print("limite de saque execedido no dia")

        elif excedeu_saque:
            print("operação falho. Numero maximo de saque no dia")    

        elif valor > 0:
            saldo -=  valor
            extrato += f"SAQUE: R$ {valor:..2f}\n"
            numero_de_Saque += 1

        else:
            print("Operação falhou! o valor informado e invalido")   
        

    elif opcao == "d":
        valor = float(input("Por favor deposite a quantia desejada: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposite: R$  {valor:.2f}\n"
        else:
            print("Operação falhou! o valor informado é invalido")

    elif opcao == "e":
        print ("============Extrato===============")
        print ("Não foram realizados movimentaçõe." if not extrato else extrato)
        print (f"\nSaldo:  R$ {saldo:.2f}")
        Print("===========================")

    elif opcao == "Q":
        break   

    else:
        print("Por favor digite uma opção valida")




