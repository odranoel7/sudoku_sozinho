class GameAgente:
    def __init__(self, qtdReinicio):
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
        self.qtdeReinicio = int(qtdReinicio)
        self.leArquivo()



    def leArquivo(self):
        matriz =[]
        local = input("Escreva o caminho do txt -->  ")
        arq = open(local)
        #matriz = []
        for line in arq.readlines():
            lista = []
            for i in range(len(line)):
                lista.append(line[i])
            arq.close
            matriz.append(lista)
            #self.listaValoresIniciais.append(lista)

        self.addImutaveis(matriz)
        self.desenhaQuadrado(matriz)
        self.regras(tuple(matriz))


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


    def regras(self, matrizInicial):
        auxCont = 0
        verificacaoMelhorEstado = -1
        bAux = False
        #print('tamanho '+str(len(matrizInicial)))
        #print('tamanho '+str(len(matrizResultado)))
        while auxCont <= self.qtdeReinicio:
            
            melhorEstado = []
            acoesRetornadas = []
            matrizResultado = []
            
            auxFuncaoAvaliacao = 0
            auxAcoesRetornadas = 0
            #print('loco '+str(matrizResultado))
            for i in range(len(matrizInicial)):
                aux = []
                for j in range(len(matrizInicial[i])):
                    aux.append(matrizInicial[i][j])
                    #print('aux '+str(aux))
                matrizResultado.append(aux)
            
            
            #print('massa '+str(matrizResultado))

            acoesRetornadas = self.acoes(matrizInicial)
            
            for linha in range(len(matrizResultado)):
                for coluna in range(len(matrizResultado[linha])):
                    if matrizResultado[linha][coluna] == ' ':
                        #print('antes -> '+str(matrizResultado[linha][coluna]))
                        matrizResultado[linha][coluna] = acoesRetornadas[auxAcoesRetornadas]
                        #print('depois -> '+str(matrizResultado[linha][coluna]))
                        auxAcoesRetornadas = auxAcoesRetornadas+1
            auxFuncaoAvaliacao = self.subidaEncosta(tuple(matrizResultado))
            #print('matriz resultado '+str(matrizResultado))
            #print('valor legal '+str(auxFuncaoAvaliacao))
            #print('auzFunção '+str(auxFuncaoAvaliacao)+'   melhor estado '+str(verificacaoMelhorEstado))
            if ((verificacaoMelhorEstado == -1) or (auxFuncaoAvaliacao < verificacaoMelhorEstado)):
                verificacaoMelhorEstado = auxFuncaoAvaliacao
                melhorEstado = matrizResultado
                print('melhor '+str(verificacaoMelhorEstado))
                
            
                if verificacaoMelhorEstado == 0:
                    self.desenhaQuadrado(melhorEstado)
                    print('Fim do jogo.')
                    bAux = True
                    break
            
                    #return melhorEstado
            #matrizResultado.remove
            auxCont = auxCont + 1
        if not bAux:
            print('Não foi encontrada a solução!')



    def verificaConflitoLinha(self, matrizVerifica):
        retorno = 0
        for i in range(len(matrizVerifica)):
            for j in range(i+1, len(matrizVerifica)):
                #print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz '+str(j))
                if matrizVerifica[i] == matrizVerifica[j]:
                    retorno=retorno+1

        return retorno

            
            
            


    def verificaConflitoColuna(self, matrizVerifica, coluna):
        resultado = 0
        for i in range(0,9):
            for j in range(i+1, 9):
                if matrizVerifica[i][int(coluna)] == matrizVerifica[j][int(coluna)]:
                    #TEM CONFLITO NA COLUNA
                    resultado=resultado+1
        return resultado
                    
                    


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
            for j in range(0, len(quadrante)):
                if quadrante[i] == quadrante[j]:
                    conflitoQuad = True
                    auxiliar = i
                    break

        if conflitoQuad:
            if not self.verificaArray(posicaoColorirQuadAux[auxiliar]):
                self.posicaoConflito.append(posicaoColorirQuadAux[auxiliar])
                self.posicaoConflito.append(str(int(linha)-1)+str(int(coluna)-1))

            #print("Existe conflitos no quadrante!")
            return True

        else:
            return False


    #PARTE DA BUSCA
    def acoes(self, estadoInicial):
        from random import randint
        
        #print('matriz que o ações ta recebendo -> '+str(matriz))
        estadoGerado = []
        #while True:

        for linha in range(len(estadoInicial)):
            for coluna in range(len(estadoInicial[linha])):
                if estadoInicial[linha][coluna] == ' ':

                    estadoGerado.append(str(randint(1, 9)))

        return estadoGerado


    def subidaEncosta(self, estadoVerificacao):
        soma = 0
        linha = 0
        coluna = 0
        #print('MATRIX '+str(estadoVerificacao))
        for linha in range(len(estadoVerificacao)):
            soma=soma+self.verificaConflitoLinha(estadoVerificacao[linha])
            #print('LINHA = '+str(linha)+' , VALOR '+str(soma))

        for coluna in range(0,9):
            soma = soma+self.verificaConflitoColuna(estadoVerificacao, coluna)
                

        for i in range(0,9):
            if i in [2,5,8]:
                if self.verificaQuadrante(estadoVerificacao, i, i):
                    soma = soma+1
        
        #print('soma massa '+str(soma))
        return soma


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
                            '\033[31m'+matrizDesenho[conta][8] + \
                            '\033[0;0m'+' '+chr(9475)
                    elif (str(conta)+str(8)) in self.listaNaoPodeMudar:
                        self.meio = self.meio + \
                            '\033[32m'+matrizDesenho[conta][8] + \
                            '\033[0;0m'+' '+chr(9475)
                    else:
                        self.meio = self.meio + matrizDesenho[conta][8]+' '+chr(9475)

                else:
                    if passou == 0:
                        if (str(conta)+str(auxColuna)) in self.posicaoConflito:
                            self.meio = self.meio + \
                                '\033[31m'+matrizDesenho[conta][auxColuna] + \
                                '\033[0;0m'
                        elif (str(conta)+str(auxColuna)) in self.listaNaoPodeMudar:
                            self.meio = self.meio + \
                                '\033[32m'+matrizDesenho[conta][auxColuna] + \
                                '\033[0;0m'
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
