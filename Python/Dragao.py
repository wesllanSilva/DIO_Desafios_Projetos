''' 
    Leia as as entradas e crie as condições necessárias para verificar se é maior ou
    menor do que 8000 e imprima "Inseto!" ou "Maior que 8000!" para cada caso.
'''

# Lê o número de casos de teste
C = int(input()) 

# Laço para percorrer os casos de teste
for i in range (C): 
  
    # Lê o nível de energia do ser vivo
    N = int(input())
    # Verifica se o nível de energia é maior que 8000
    if N > 8000:
        
        print("Mais de 8000!")
    else:
        
        print("Inseto!")
    
  