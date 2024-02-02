# Função para verificar se B encaixa em A
def encaixa(A, B):
    return A.endswith(B)

# Número de casos de teste
N = int(input())

for _ in range(N):
    # Entrada dos valores A e B
    A, B = input().split()
    
    # Verifica se B encaixa em A e imprime o resultado
    if encaixa(A, B):
        print("encaixa")
    else:
        print("nao encaixa")
