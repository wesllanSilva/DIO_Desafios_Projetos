'''
 Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
"encaixa" ou "não encaixa" para cada uma das relações N vezes.
'''

N = int(input())

result = []

for i in range(N):
    numero_1, numero_2 = input().split(" ")

    count = 0
    for i in numero_2:
        count += 1
        
    if len(numero_2) > len(numero_1):
        print("nao") 
    elif(numero_1[-(count):] == numero_2):
        print("encaixa")
    else:
        print("nao")