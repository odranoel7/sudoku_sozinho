#FOI IMPLEMENTADA SEGUINDO OS MÉTODOS CITADOS NO ENUNCIADO


def backtracking(i, vetor):
    
    if (i == 81):
        return True
    elif (vetor[i] != 0):
        return backtracking(i+1, vetor)
    for j in range(0,9):
        if nao_ha_violacao(j, i, vetor):
            vetor[i] = j
            if backtracking(i+1, vetor):
                return True
            vetor[i] = 0
    return False

def nao_ha_violacao(x, i, vetor):
    pass

def imprime(V):
    pass



# DEMONSTRAÇÃO 

y = []
import random
for z in range(0,81):
    y.append(random.randint(1,9))
if backtracking(0,y):
    imprime(y)
else:
    print('Não foi possível encontrar a solução!')