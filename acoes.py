
from dataclasses import dataclass

class AcoesJogador():
    inserir = 'INSERIR'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def inserir(cls, listaAtual):
        from random import randint
        acoes = []
        for i in range(len(listaAtual)):
            for j in range(len(listaAtual[i])):
                if listaAtual[i][j] == ' ':
                    k = randint(1,9)
                    #ADICIONADO MAIS UM APENAS PARA TESTE, POIS ANTES COORDENADAS COMEÇAVA DO 1 AGORA COMEÇA DO 0
                    return (AcoesJogador.inserir, (str(i+1), str(j+1), str(k)))

#print(str(AcaoJogador.inserir([[1,0,1,1], [2,2,0,2,2,2], [0,3,3,3,3,3,5]])))
        

