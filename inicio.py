from gameAgente import GameAgente
from gameHumano import GameHumano
from gameAgente_Retrocesso import GameAgenteRetrocesso

while True:
    escolhido = input('Com qual agente deseja jogar? \n'+
                      '1 -> Humano. \n'+
                      '2 -> Automático. \n'
                      '3 -> backtracking. \n '
                     )
    if int(escolhido) in [1,2,3]:
        break
        
if int(escolhido) == 1:
    GameHumano()
elif int(escolhido) == 2:
    while True:
        qtde = input('Qual a quantidade de reinícios que você deseja?')
        if ((int(qtde)) and (int(qtde) > 0)):
            break

    GameAgente(qtde)
elif int(escolhido) == 3:
    GameAgenteRetrocesso()