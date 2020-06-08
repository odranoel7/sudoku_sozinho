cima = ''
meio = ''
risco = ''
bConflito = False
valor = ""
cordenadaLinha = ""
cordenadaColuna = ""
fimJogo = False
bateNum = False
matriz = []
quadrante = []
listaNaoPodeMudar = []
listaVlrCorreto = [1,2,3,4,5,6,7,8,9]
conflitoQuad = False
posicaoConflito = []
bNaoPodeAlterar = False

def leArquivo():
    global matriz
    local = input("Escreva o caminho do txt -->  ")
    arq = open(local)
            
    for line in arq.readlines():        
        lista = []
        for i in range(len(line)):
            lista.append(line[i])                
        arq.close
        matriz.append(lista)

    addImutaveis()
    desenhaQuadrado(matriz)    
    regras()

def verificaArray(a):
    if a in posicaoConflito:
        return True
    return False


def addImutaveis():
    global listaNaoPodeMudar
    linha = 0    
    for linha in range(len(matriz)):
        coluna = 0
        for coluna in range(len(matriz[linha])):            
            if matriz[linha][coluna] != " ": 
                listaNaoPodeMudar.append(str(linha)+str(coluna))

def regras():
    global bateNum
    global fimJogo
    global valor
    global matriz
    global cordenadaLinha
    global cordenadaColuna
    global listaVlrCorreto
    global conflitoQuad
    global posicaoConflito
    bAux = False
    cordenadas = False
    verificacaoMelhorEstado = -1
    melhorEstado = []
    
    matrizResultado = tuple(matriz)
    acoesRetornadas = []
    auxAcoesRetornadas = 0
    acoesRetornadas = acoes(tuple(matriz))
    auxFuncaoAvaliacao = 0

    while True:
        
        for linha in range(len(matrizResultado)):
            for coluna in range(len(matrizResultado[linha])):
                if matrizResultado[linha][coluna] == ' ':
                    matrizResultado[linha][coluna] = acoesRetornadas[auxAcoesRetornadas]
                    auxAcoesRetornadas = auxAcoesRetornadas+1

        auxFuncaoAvaliacao = funcaoAvalicao(tuple(matrizResultado))
        if ((verificacaoMelhorEstado == -1) or (auxFuncaoAvaliacao < verificacaoMelhorEstado)):
            verificacaoMelhorEstado = auxFuncaoAvaliacao
            melhorEstado = matrizResultado
            print('Esse é o melhor resultado -> '+str(melhorEstado))
            if verificacaoMelhorEstado == 0:
                desenhaQuadrado(melhorEstado)
                break
                #return melhorEstado

def verificaConflitoLinha(matrizVerifica):
    global bConflito
    global fimJogo
    global bateNum
    global matriz
    global posicaoConflito
    global bNaoPodeAlterar
    #for i in range(len(listaNaoPodeMudar)):                    
    #    if listaNaoPodeMudar[i] == str(int(cordenadaLinha)-1) + str(int(cordenadaColuna)-1):
    #        fimJogo = False
    #        bateNum = True
    #        bNaoPodeAlterar = True
    #        print("Esta posição não pode ser Alterada!")
    #        break
    #    else: 
    #        bateNum = False
    #        bNaoPodeAlterar = False     
    #if not bNaoPodeAlterar:
    for i in range(len(matrizVerifica)):        
        if matrizVerifica[i] in matrizVerifica:
            #TEM CONFLITO NA LINHA
            #if not verificaArray(str(int(cordenadaLinha)-1)+str(i)):
                #posicaoConflito.append(str(int(cordenadaLinha)-1)+str(i))
                #posicaoConflito.append(str(int(cordenadaLinha)-1)+str(int(cordenadaColuna)-1))                    
            return True    
    return False
                

def verificaConflitoColuna(matrizVerifica, coluna):
    global bConflito
    global fimJogo
    global bateNum
    global matriz
    global posicaoConflito
    global bNaoPodeAlterar
    #for i in range(len(listaNaoPodeMudar)):                    
        #if listaNaoPodeMudar[i] == str(int(cordenadaLinha)-1) + str(int(cordenadaColuna)-1):
        #    fimJogo = False
        #    bateNum = True
        #    bNaoPodeAlterar = True
        #    print("Esta posição não pode ser Alterada!")
        #    break
        #else: 
        #    bateNum = False
        #    bNaoPodeAlterar = False     
    #if not bNaoPodeAlterar:
    for i in range(len(matrizVerifica)):
        for j in range(len(matrizVerifica)):
            if matrizVerifica[j][int(coluna)] == matrizVerifica[i][int(coluna)]:
            #TEM CONFLITO NA COLUNA
                #if not verificaArray(str(i)+str(int(coluna)-1)):                    
                #    posicaoConflito.append(str(i)+str(int(coluna)-1))
                #    posicaoConflito.append(str(int(cordenadaLinha)-1)+str(int(cordenadaColuna)-1))
                return True
    return False

def verificaQuadrante(matrizVerifica, coluna, linha):
    global quadrante
    global matriz
    global conflitoQuad    
    global posicaoConflito
    colunaAux=0
    linhaAux=0
    posicaoColorirQuadAux = []
    quadrante = []
    i=0
    j=0
    if int(coluna) in [1,2,3]:
        colunaAux = 0
    elif int(coluna) in [4,5,6]:
        colunaAux = 3
    elif int(coluna) in [7,8,9]:
        colunaAux = 6

    if int(linha) in [1,2,3]:
        linhaAux = 0
    elif int(linha) in [4,5,6]:
        linhaAux = 3
    elif int(linha) in [7,8,9]:
        linhaAux = 6

    i=linhaAux
    j=colunaAux
    while i < (linhaAux+3):
        j=colunaAux
        while j < (colunaAux+3):
            if ((matrizVerifica[i][j] != ' ') and (matrizVerifica[i][j] != '\n')):
                quadrante.append(int(matrizVerifica[i][j]))                
            else:
                quadrante.append(matrizVerifica[i][j])
            posicaoColorirQuadAux.append(str(i)+str(j))
            j = j + 1        
        i = i + 1
    
    for i in range(0, len(quadrante)):
        for j in range(0, len(quadrante)):
            if quadrante[i] == quadrante[j]:
                conflitoQuad = True
                auxiliar = i
                break

    
    
    if conflitoQuad:
        if not verificaArray(posicaoColorirQuadAux[auxiliar]):
            posicaoConflito.append(posicaoColorirQuadAux[auxiliar])
            posicaoConflito.append(str(int(linha)-1)+str(int(coluna)-1))
        
        #print("Existe conflitos no quadrante!")                        
        return True
        
    else:
        return False







#PARTE DA BUSCA
def acoes(estadoInicial):
    from random import randint
    estadoGerado = []
    #while True:
    for linha in range(len(estadoInicial)):
        for coluna in range(len(estadoInicial[linha])):
            if estadoInicial[linha][coluna] == ' ':
                estadoGerado.append(str(randint(1,9)))

    return estadoGerado


def funcaoAvalicao(estadoVerificacao):
    soma = 0
    soma
    linha = 0
    coluna = 0
    #for linha in range(len(estadoInicial)):
    #    for coluna in range(len(estadoInicial[i])):
    #        if estadoInicial[linha][coluna] == 0:
    #            somaVazioInicial = somaVazioInicial+1

    linha = 0
    coluna = 0
    for linha in range(len(estadoVerificacao)):
        for coluna in range(len(estadoVerificacao[linha])):
            if estadoVerificacao[linha][coluna] == ' ':
                soma = soma+1
            else:
                if verificaConflitoLinha(estadoVerificacao[linha]):
                    soma=soma+1
                if verificaConflitoColuna(estadoVerificacao, coluna):
                    soma=soma+1
                if verificaQuadrante(estadoVerificacao, linha, coluna):
                    soma=soma+1
    return soma

def desenhaQuadrado(matrizDesenho):
    numeracao = ""
    global cima
    global meio
    global risco
    cima = ''
    aux = 0    
    numeracao = '  1  2  3  4  5  6   7  8  9'
    for i in range(26):
        if (aux+3)==i:
            cima=cima+chr(9523)
            aux=aux+3
        elif i == 0:
            cima=chr(9487)
        elif i == 25:
            cima=cima+chr(9473)+chr(9473)
            cima=cima+chr(9491)
        else:
            cima=cima+chr(9473)
    
    print(' '+cima)
    auxColuna = 0
    passou = 0
    
    for conta in range(9):
        meio = ''
        aux = 0        
        i = 0
        for i in range(26):
            if auxColuna == 8:
                auxColuna = 0

            if i == 0:
                meio = chr(9475)
            elif (aux+3)==i:
                meio = meio+chr(9475)
                aux = aux+3
            elif i == 25:
                if (str(conta)+str(8)) in posicaoConflito:
                    meio = meio+'\033[31m'+matrizDesenho[conta][8]+'\033[0;0m'+' '+chr(9475)
                elif (str(conta)+str(8)) in listaNaoPodeMudar:
                    meio = meio+'\033[32m'+matrizDesenho[conta][8]+'\033[0;0m'+' '+chr(9475)
                else:
                    meio = meio+ matrizDesenho[conta][8]+' '+chr(9475)
                
            else:
                if passou == 0:
                    if (str(conta)+str(auxColuna)) in posicaoConflito:
                        meio = meio + '\033[31m'+matrizDesenho[conta][auxColuna]+'\033[0;0m'
                    elif (str(conta)+str(auxColuna)) in listaNaoPodeMudar:
                        meio = meio + '\033[32m'+matrizDesenho[conta][auxColuna]+'\033[0;0m'                                                            
                    else:
                        meio = meio + matrizDesenho[conta][auxColuna]
                    
                    passou = 1
                    auxColuna = auxColuna+1
                else:
                    meio = meio +' '
                    passou = 0
                
        print(str(conta+1)+meio)
        aux = 0
        for i in range(28):
            if i == 0: 
                risco = chr(9507)
            elif i == 27:
                risco = risco+chr(9507)
            elif (aux+3)==i:            
                risco = risco+chr(9507)
                aux = aux+3            
            else:
                risco = risco+chr(9473)
            
                            
        print(' '+risco)
    print(numeracao)
    

leArquivo()