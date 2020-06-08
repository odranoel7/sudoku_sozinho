from game import verificaConflito
from game import verificaQuadrante
from random import *
#def registrarProximaAcao(self, acao):
#    self.acao = acao

def acoes(estadoInicial):
    estadoGerado = []
    #while True:
    for linha in range(len(estadoInicial)):
        for coluna in range(len(estadoInicial[i])):
            if estadoInicial[linha][coluna] == ' ':
                estadoGerado.append(str(random.randint(1,9)))

    return estadoGerado



#def resultado(estadoAtual, acao):
    

def funcaoAvalicao(estadoInicial, estadoVerificacao):
    somaVazioInicial = 0
    linha = 0
    coluna = 0
    for linha in range(len(estadoInicial)):
        for coluna in range(len(estadoInicial[i])):
            if estadoInicial[linha][coluna] == 0:
                somaVazioInicial = somaVazioInicial+1

    linha = 0
    coluna = 0
    for linha in range(len(estadoVerificacao)):
        for coluna in range(len(estadoVerificacao[i]))


    
    return retorno