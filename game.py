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
    desenhaQuadrado()    
    regras()


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
    while True:
        cordenadaLinha  = input("Qual a cordenada de linha?  ")        
        if int(cordenadaLinha) in listaVlrCorreto:
            cordenadaColuna = input("Qual a cordenada de coluna?  ")
            if int(cordenadaColuna) in listaVlrCorreto:
                valor = input("Qual o valor que deseja colocar?  ")
                if int(valor) in listaVlrCorreto:
                    cordenadas = True
                else:
                    print("Valor invalido!")
                    cordenadas = False
            else:
                print("Cordenada da Coluna invalida.")
                cordenadas = False
        else:
            print("Cordenada da Linha invalida")
            cordenadas = False

        if cordenadas:                                         
            verificaConflito()
            if not bNaoPodeAlterar:
                verificaQuadrante()            
                matriz[int(cordenadaLinha)-1][int(cordenadaColuna)-1] = valor                                    
            
            aux=0
            bAuxiliar = False

            while aux < len(posicaoConflito):
                if matriz[int(posicaoConflito[aux][0])][int(posicaoConflito[aux][1])] != matriz[int(posicaoConflito[aux+1][0])][int(posicaoConflito[aux+1][1])]:                    
                    del(posicaoConflito[aux])                    
                    del(posicaoConflito[aux])
                    bAuxiliar=True

                if bAuxiliar:
                    aux=0
                    bAuxiliar = False
                else:                    
                    aux=aux+2
            
            if ((not bateNum) and (not conflitoQuad)):
                fimJogo = False
            
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] == ' ':
                        fimJogo = False
                        break
                    else:
                        fimJogo = True
            if len(posicaoConflito) > 0:
                fimJogo = False
        
        desenhaQuadrado()
        conflitoQuad = False
        if fimJogo: 
            break
    print('Parabéns, você ganhou o jogo!')



        
def verificaArray(a):
    
    if a in posicaoConflito:
        return True
    return False



def verificaConflito(acao=None):
    global bConflito
    global fimJogo
    global bateNum
    global matriz
    global posicaoConflito
    global bNaoPodeAlterar
    for i in range(len(listaNaoPodeMudar)):                    
        if listaNaoPodeMudar[i] == str(int(cordenadaLinha)-1) + str(int(cordenadaColuna)-1):
            fimJogo = False
            bateNum = True
            bNaoPodeAlterar = True
            print("Esta posição não pode ser Alterada!")
            break
        else: 
            bateNum = False
            bNaoPodeAlterar = False     
    if not bNaoPodeAlterar:
        for i in range(len(matriz[int(cordenadaLinha)-1])):            
            if matriz[int(cordenadaLinha)-1][i] == valor:
                if not verificaArray(str(int(cordenadaLinha)-1)+str(i)):
                    posicaoConflito.append(str(int(cordenadaLinha)-1)+str(i))
                    posicaoConflito.append(str(int(cordenadaLinha)-1)+str(int(cordenadaColuna)-1))
                else:
                    print('existe')
                fimJogo = False
                bateNum = True
                bConflito = True
                print("Valor em conflito!")
                break
            else: 
                bateNum = False
                bConflito = False        
    if ((not bateNum) and (not bConflito)):        
        for i in range(len(matriz)):            
            if matriz[i][int(cordenadaColuna)-1] == valor:
                if not verificaArray(str(i)+str(int(cordenadaColuna)-1)):                    
                    posicaoConflito.append(str(i)+str(int(cordenadaColuna)-1))
                    posicaoConflito.append(str(int(cordenadaLinha)-1)+str(int(cordenadaColuna)-1))
                else:
                    print('existe')
                fimJogo = False
                bateNum = True
                bConflito = True
                print("Valor em conflito!")
                break
            else: 
                bateNum = False
                bConflito = False 

def verificaQuadrante(acao=None):
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
    if int(cordenadaColuna) in [1,2,3]:
        colunaAux = 0
    elif int(cordenadaColuna) in [4,5,6]:
        colunaAux = 3
    elif int(cordenadaColuna) in [7,8,9]:
        colunaAux = 6

    if int(cordenadaLinha) in [1,2,3]:
        linhaAux = 0
    elif int(cordenadaLinha) in [4,5,6]:
        linhaAux = 3
    elif int(cordenadaLinha) in [7,8,9]:
        linhaAux = 6

    i=linhaAux
    j=colunaAux
    while i < (linhaAux+3):
        j=colunaAux
        while j < (colunaAux+3):            
            if ((matriz[i][j] != ' ') and (matriz[i][j] != '\n')):
                quadrante.append(int(matriz[i][j]))                
            else:
                quadrante.append(matriz[i][j])
            posicaoColorirQuadAux.append(str(i)+str(j))
            j = j + 1        
        i = i + 1
    
    for i in range(0, len(quadrante)):
        if int(valor) == quadrante[i]:
            conflitoQuad = True
            auxiliar = i
            break

    
    
    if conflitoQuad:
        if not verificaArray(posicaoColorirQuadAux[auxiliar]):
            posicaoConflito.append(posicaoColorirQuadAux[auxiliar])
            posicaoConflito.append(str(int(cordenadaLinha)-1)+str(int(cordenadaColuna)-1))
        else:
            print('existe')
        print("Existe conflitos no quadrante!")                        


    
def desenhaQuadrado():
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
                    meio = meio+'\033[31m'+matriz[conta][8]+'\033[0;0m'+' '+chr(9475)
                elif (str(conta)+str(8)) in listaNaoPodeMudar:
                    meio = meio+'\033[32m'+matriz[conta][8]+'\033[0;0m'+' '+chr(9475)
                else:
                    meio = meio+ matriz[conta][8]+' '+chr(9475)
                
            else:
                if passou == 0:
                    if (str(conta)+str(auxColuna)) in posicaoConflito:
                        meio = meio + '\033[31m'+matriz[conta][auxColuna]+'\033[0;0m'
                    elif (str(conta)+str(auxColuna)) in listaNaoPodeMudar:
                        meio = meio + '\033[32m'+matriz[conta][auxColuna]+'\033[0;0m'                                                            
                    else:
                        meio = meio + matriz[conta][auxColuna]
                    
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