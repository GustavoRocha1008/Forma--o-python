#Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.
months_dict = {1: 'JANUARY', 2: 'FEBRUARY', 3: 'MARCH', 4: 'APRIL', 5: 'MAY', 6: 'JUNE', 7: 'JULY', 8: 'AUGUST', 9: 'SEPTEMBER', 10: 'OCTOBER', 11: 'NOVEMBER', 12: 'DECEMBER'}

try:
    month = int(input("Digite o mêS desevado do 1 ao 12:  "))
    month = int(month)
    if month in months_dict:
        print(f"Então o mes selecionado e {months_dict[month]}")
    else:
        print("Digite um valor valido!")

except:
    print("Digite um valor numerico valido!")





month_number = int(input())

months_dict = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

if 1 <= month_number <= 12:
    month_name = months_dict[month_number]
    print(month_name)
else:
    print("Digite um valor válido entre 1 e 12.")
