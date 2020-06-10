class GameAgenteRetrocesso:
    def __init__(self):
        self.cima = ''
        self.meio = ''
        self.risco = ''
        self.bConflito = False
        self.valor = ""
        self.cordenadaLinha = ""
        self.cordenadaColuna = ""
        self.fimJogo = False
        self.bateNum = False
        self.quadrante = []
        self.listaNaoPodeMudar = []
        self.listaVlrCorreto = [1,2,3,4,5,6,7,8,9]
        self.conflitoQuad = False
        self.posicaoConflito = []
        self.bNaoPodeAlterar = False
        self.listaValoresIniciais = [[],[],[],[],[],[],[],[],[]]
        self.leArquivo()

    def leArquivo(self):
        matriz =[]
        local = input("Escreva o caminho do txt -->  ")
        arq = open(local)
        listaAux = []
        for line in arq.readlines():
            lista = []
            for i in range(len(line)):
                lista.append(line[i])
            arq.close
            matriz.append(lista)

        self.addImutaveis(matriz)
        self.desenhaQuadrado(matriz)
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] != '\n':
                    listaAux.append(matriz[i][j])
        
        #print(str(listaAux))
        if not self.sudoku(0, listaAux):
            print('Não foi possível encontrar a solução! :(')

        #if self.backtracking(0,0,matriz):
        #    self.desenhaQuadrado(matriz)
        #else:
        #    print('Não foi possível encontrar a solução! :(')


    def sudoku (self, i, V):
        #print('cdefcedcf '+str(i))
        
        if i > 80:
            self.desenhaQuadrado(self.listaMatriz(V))
            #print(str(V))
            return True # solução encontrada
        elif V[i] != ' ': #Preenchida
            return self.sudoku(i+1, V)

        elif V[i] == ' ': # posição a preencher
            for x in range(1,10):
                if self.nao_ha_violacao(str(x),i,V): # registra e avança
                    #print('-----')
                    V[i] = str(x)
                    if self.sudoku(i+1,V):
                        return True
                    V[i] = ' '
                
            return False

    def listaMatriz(self, lista):
        #print('cdfvc '+str(lista) )
        matriz = []
        matrizAux = []
        aux = 0
        for _ in range(9):
            for j in range(9):
                matrizAux.append(lista[aux+j])
            aux=aux+9
            matriz.append(matrizAux)
            matrizAux = []
        return matriz

    def nao_ha_violacao(self, valor, i, lista):
        matriz = []
        #print('lista '+str(lista))
        #print('vlr '+str(valor))
        #print('i '+str(i))
        #print()
        #print('coluna -> '+str(coluna))
        #print('linha -> '+str(linha))
        #print('lista -> '+str(matriz))
        #print()
        
        aux = lista[i]
        lista[i] = valor
        matriz = self.listaMatriz(lista)
        #print('minha matriz '+str(matriz))

        for linha in range(9):
            for coluna in range(9):
                #print('fdc '+str(matriz[linha]))

                if not self.verificaConflitoLinha(matriz[linha]):
                    if not self.verificaConflitoColuna(matriz, coluna):
                        if self.verificaQuadrante(matriz, coluna, linha):
                            matriz = []
                            lista[i] = aux
                            return False
                    else:
                        #print('2')
                        matriz = []
                        lista[i] = aux
                        return False
                else:
                    #print('3')
                    matriz = []
                    lista[i] = aux
                    return False

        #print('yesssss')
        return True


    #FUNCIONA
    #def backtracking(self, i, j,vetor):
    #    import random
    #    
    #    if (i == 81) and (j == 81):
    #        return True
    #    
    #    for linha in range(0,9):
    #        for coluna in range(0,9):
    #            valor = vetor[linha][coluna]
    #            vetor[linha][coluna] = random.randint(1,9)
    #            if not((not self.verificaConflitoLinha(vetor[linha])) 
    #               and (not self.verificaConflitoColuna(vetor, coluna))
    #               and (not self.verificaQuadrante(vetor, coluna, linha))
    #               and (str(linha)+str(coluna) not in self.listaNaoPodeMudar)):
    #                
    #                vetor[linha][coluna] = valor
    #                
    #            else:
    #                if self.backtracking(i+1, j+1, vetor):
    #                    return True
    #    
    #                    
    #    return False


    def verificaArray(self, a):
        if a in self.posicaoConflito:
            return True
        return False


    def addImutaveis(self, matrizInicial):
        linha = 0
        

        linha = 0
        for linha in range(len(matrizInicial)):
            coluna = 0
            for coluna in range(len(matrizInicial[linha])):
                if matrizInicial[linha][coluna] != " ":
                    self.listaNaoPodeMudar.append(str(linha)+str(coluna))

    def verificaConflitoLinha(self, matrizVerifica):
        for i in range(len(matrizVerifica)):
            for j in range(i+1, len(matrizVerifica)):
                if ((matrizVerifica[i] == matrizVerifica[j]) and (matrizVerifica[i] != ' ' and matrizVerifica[j] != ' ')):
                    return True
        return False

    def verificaConflitoColuna(self, matrizVerifica, coluna):
        for i in range(0,9):
            for j in range(i+1, 9):
                if ((matrizVerifica[i][int(coluna)] == matrizVerifica[j][int(coluna)]) and (matrizVerifica[i][int(coluna)] != ' ' and matrizVerifica[j][int(coluna)] != ' ')):
                    #TEM CONFLITO NA COLUNA
                    return True
        return False

    def verificaQuadrante(self, matrizVerifica, coluna, linha):
        
        colunaAux = 0
        linhaAux = 0
        posicaoColorirQuadAux = []
        quadrante = []
        conflitoQuad = False
        i = 0
        j = 0
        if int(coluna) in [1, 2, 3]:
            colunaAux = 0
        elif int(coluna) in [4, 5, 6]:
            colunaAux = 3
        elif int(coluna) in [7, 8, 9]:
            colunaAux = 6

        if int(linha) in [1, 2, 3]:
            linhaAux = 0
        elif int(linha) in [4, 5, 6]:
            linhaAux = 3
        elif int(linha) in [7, 8, 9]:
            linhaAux = 6

        i = linhaAux
        j = colunaAux
        while i < (linhaAux+3):
            j = colunaAux
            while j < (colunaAux+3):
                if ((matrizVerifica[i][j] != ' ') and (matrizVerifica[i][j] != '\n')):
                    quadrante.append(int(matrizVerifica[i][j]))
                else:
                    quadrante.append(matrizVerifica[i][j])
                posicaoColorirQuadAux.append(str(i)+str(j))
                j = j + 1
            i = i + 1

        for i in range(0, len(quadrante)):
            for j in range(i+1, len(quadrante)):
                if ((quadrante[i] == quadrante[j]) and (quadrante[i] != ' ' and quadrante[j] != ' ')):
                    conflitoQuad = True
                    auxiliar = i
                    break

        if conflitoQuad:
            if not self.verificaArray(posicaoColorirQuadAux[auxiliar]):
                self.posicaoConflito.append(posicaoColorirQuadAux[auxiliar])
                self.posicaoConflito.append(str(int(linha)-1)+str(int(coluna)-1))

            
            return True

        else:
            return False


    #PARTE DA BUSCA
    def acoes(self, estadoInicial):
        from random import randint
        estadoGerado = []
        for linha in range(len(estadoInicial)):
            for coluna in range(len(estadoInicial[linha])):
                if estadoInicial[linha][coluna] == ' ':

                    estadoGerado.append(str(randint(1, 9)))

        return estadoGerado

    def desenhaQuadrado(self, matrizDesenho):
        numeracao = ""
        self.cima = ''
        aux = 0
        numeracao = '  1  2  3  4  5  6   7  8  9'
        for i in range(26):
            if (aux+3) == i:
                self.cima = self.cima+chr(9523)
                aux = aux+3
            elif i == 0:
                self.cima = chr(9487)
            elif i == 25:
                self.cima = self.cima+chr(9473)+chr(9473)
                self.cima = self.cima+chr(9491)
            else:
                self.cima = self.cima+chr(9473)

        print(' '+self.cima)
        auxColuna = 0
        passou = 0

        for conta in range(9):
            self.meio = ''
            aux = 0
            i = 0
            for i in range(26):
                if auxColuna == 8:
                    auxColuna = 0

                if i == 0:
                    self.meio = chr(9475)
                elif (aux+3) == i:
                    self.meio = self.meio+chr(9475)
                    aux = aux+3
                elif i == 25:
                    if (str(conta)+str(8)) in self.posicaoConflito:
                        self.meio = self.meio + \
                            matrizDesenho[conta][8] +' '+chr(9475)
                    elif (str(conta)+str(8)) in self.listaNaoPodeMudar:
                        self.meio = self.meio + \
                            matrizDesenho[conta][8]+' '+chr(9475)
                    else:
                        self.meio = self.meio + matrizDesenho[conta][8]+' '+chr(9475)

                else:
                    if passou == 0:
                        if (str(conta)+str(auxColuna)) in self.posicaoConflito:
                            self.meio = self.meio + \
                                matrizDesenho[conta][auxColuna]
                        elif (str(conta)+str(auxColuna)) in self.listaNaoPodeMudar:
                            self.meio = self.meio+matrizDesenho[conta][auxColuna]
                        else:
                            self.meio = self.meio + matrizDesenho[conta][auxColuna]

                        passou = 1
                        auxColuna = auxColuna+1
                    else:
                        self.meio = self.meio + ' '
                        passou = 0

            print(str(conta+1)+self.meio)
            aux = 0
            for i in range(28):
                if i == 0:
                    self.risco = chr(9507)
                elif i == 27:
                    self.risco = self.risco+chr(9507)
                elif (aux+3) == i:
                    self.risco = self.risco+chr(9507)
                    aux = aux+3
                else:
                    self.risco = self.risco+chr(9473)

            print(' '+self.risco)
        print(numeracao)


    #leArquivo()
