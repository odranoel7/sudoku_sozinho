class GameHumano:
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
        self.matriz = []
        self.quadrante = []
        self.listaNaoPodeMudar = []
        self.listaVlrCorreto = [1,2,3,4,5,6,7,8,9]
        self.conflitoQuad = False
        self.posicaoConflito = []
        self.bNaoPodeAlterar = False
        self.leArquivo()

    def leArquivo(self):
        
        local = input("Escreva o caminho do txt -->  ")
        arq = open(local)
                
        for line in arq.readlines():        
            lista = []
            for i in range(len(line)):
                lista.append(line[i])                
            arq.close
            self.matriz.append(lista)

        self.addImutaveis()
        self.desenhaQuadrado()    
        self.regras()


    def addImutaveis(self):
        
        linha = 0    
        for linha in range(len(self.matriz)):
            coluna = 0
            for coluna in range(len(self.matriz[linha])):            
                if self.matriz[linha][coluna] != " ": 
                    self.listaNaoPodeMudar.append(str(linha)+str(coluna))
        
    def regras(self):
        #bAux = False
        cordenadas = False
        while True:
            self.cordenadaLinha  = input("Qual a cordenada de linha?  ")        
            if int(self.cordenadaLinha) in self.listaVlrCorreto:
                self.cordenadaColuna = input("Qual a cordenada de coluna?  ")
                if int(self.cordenadaColuna) in self.listaVlrCorreto:
                    self.valor = input("Qual o valor que deseja colocar?  ")
                    if int(self.valor) in self.listaVlrCorreto:
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
                self.verificaConflito()
                if not self.bNaoPodeAlterar:
                    self.verificaQuadrante()            
                    self.matriz[int(self.cordenadaLinha)-1][int(self.cordenadaColuna)-1] = self.valor                                    
                
                aux=0
                bAuxiliar = False

                while aux < len(self.posicaoConflito):
                    if self.matriz[int(self.posicaoConflito[aux][0])][int(self.posicaoConflito[aux][1])] != self.matriz[int(self.posicaoConflito[aux+1][0])][int(self.posicaoConflito[aux+1][1])]:
                        del(self.posicaoConflito[aux])                    
                        del(self.posicaoConflito[aux])
                        bAuxiliar=True

                    if bAuxiliar:
                        aux=0
                        bAuxiliar = False
                    else:                    
                        aux=aux+2
                
                if ((not self.bateNum) and (not self.conflitoQuad)):
                    self.fimJogo = False
                
                for i in range(len(self.matriz)):
                    for j in range(len(self.matriz[i])):
                        if self.matriz[i][j] == ' ':
                            self.fimJogo = False
                            break
                        else:
                            self.fimJogo = True
                if len(self.posicaoConflito) > 0:
                    self.fimJogo = False
            
            self.desenhaQuadrado()
            self.conflitoQuad = False
            if self.fimJogo: 
                break
        print('Parabéns, você ganhou o jogo!')



            
    def verificaArray(self, a):
        
        if a in self.posicaoConflito:
            return True
        return False



    def verificaConflito(self, acao=None):
        
        for i in range(len(self.listaNaoPodeMudar)):                    
            if self.listaNaoPodeMudar[i] == str(int(self.cordenadaLinha)-1) + str(int(self.cordenadaColuna)-1):
                self.fimJogo = False
                self.bateNum = True
                self.bNaoPodeAlterar = True
                print("Esta posição não pode ser Alterada!")
                break
            else: 
                self.bateNum = False
                self.bNaoPodeAlterar = False     
        if not self.bNaoPodeAlterar:
            for i in range(len(self.matriz[int(self.cordenadaLinha)-1])):            
                if self.matriz[int(self.cordenadaLinha)-1][i] == self.valor:
                    if not self.verificaArray(str(int(self.cordenadaLinha)-1)+str(i)):
                        self.posicaoConflito.append(str(int(self.cordenadaLinha)-1)+str(i))
                        self.posicaoConflito.append(str(int(self.cordenadaLinha)-1)+str(int(self.cordenadaColuna)-1))
                    else:
                        print('existe')
                    self.fimJogo = False
                    self.bateNum = True
                    
                    self.bConflito = True
                    print("Valor em conflito!")
                    break
                else: 
                    self.bateNum = False
                    self.bConflito = False        
        if ((not self.bateNum) and (not self.bConflito)):        
            for i in range(len(self.matriz)):            
                if self.matriz[i][int(self.cordenadaColuna)-1] == self.valor:
                    if not self.verificaArray(str(i)+str(int(self.cordenadaColuna)-1)):                    
                        self.posicaoConflito.append(str(i)+str(int(self.cordenadaColuna)-1))
                        self.posicaoConflito.append(str(int(self.cordenadaLinha)-1)+str(int(self.cordenadaColuna)-1))
                    else:
                        print('existe')
                    self.fimJogo = False
                    self.bateNum = True
                    self.bConflito = True
                    print("Valor em conflito!")
                    break
                else: 
                    self.bateNum = False
                    self.bConflito = False 

    def verificaQuadrante(self, acao=None):
        
        
        global conflitoQuad    
        global posicaoConflito
        colunaAux=0
        linhaAux=0
        posicaoColorirQuadAux = []
        self.quadrante = []
        i=0
        j=0
        if int(self.cordenadaColuna) in [1,2,3]:
            colunaAux = 0
        elif int(self.cordenadaColuna) in [4,5,6]:
            colunaAux = 3
        elif int(self.cordenadaColuna) in [7,8,9]:
            colunaAux = 6

        if int(self.cordenadaLinha) in [1,2,3]:
            linhaAux = 0
        elif int(self.cordenadaLinha) in [4,5,6]:
            linhaAux = 3
        elif int(self.cordenadaLinha) in [7,8,9]:
            linhaAux = 6

        i=linhaAux
        j=colunaAux
        while i < (linhaAux+3):
            j=colunaAux
            while j < (colunaAux+3):            
                if ((self.matriz[i][j] != ' ') and (self.matriz[i][j] != '\n')):
                    self.quadrante.append(int(self.matriz[i][j]))                
                else:
                    self.quadrante.append(self.matriz[i][j])
                posicaoColorirQuadAux.append(str(i)+str(j))
                j = j + 1        
            i = i + 1
        
        for i in range(0, len(self.quadrante)):
            if int(self.valor) == self.quadrante[i]:
                self.conflitoQuad = True
                auxiliar = i
                break

        
        
        if self.conflitoQuad:
            if not self.verificaArray(posicaoColorirQuadAux[auxiliar]):
                self.posicaoConflito.append(posicaoColorirQuadAux[auxiliar])
                self.posicaoConflito.append(str(int(self.cordenadaLinha)-1)+str(int(self.cordenadaColuna)-1))
            else:
                print('existe')
            print("Existe conflitos no quadrante!")                        


        
    def desenhaQuadrado(self):
        numeracao = ""
        self.cima = ''
        aux = 0    
        numeracao = '  1  2  3  4  5  6   7  8  9'
        for i in range(26):
            if (aux+3)==i:
                self.cima=self.cima+chr(9523)
                aux=aux+3
            elif i == 0:
                self.cima=chr(9487)
            elif i == 25:
                self.cima=self.cima+chr(9473)+chr(9473)
                self.cima=self.cima+chr(9491)
            else:
                self.cima=self.cima+chr(9473)
        
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
                elif (aux+3)==i:
                    self.meio = self.meio+chr(9475)
                    aux = aux+3
                elif i == 25:
                    if (str(conta)+str(8)) in self.posicaoConflito:
                        self.meio = self.meio+'\033[31m'+self.matriz[conta][8]+'\033[0;0m'+' '+chr(9475)
                    elif (str(conta)+str(8)) in self.listaNaoPodeMudar:
                        self.meio = self.meio+'\033[32m'+self.matriz[conta][8]+'\033[0;0m'+' '+chr(9475)
                    else:
                        self.meio = self.meio+ self.matriz[conta][8]+' '+chr(9475)
                    
                else:
                    if passou == 0:
                        if (str(conta)+str(auxColuna)) in self.posicaoConflito:
                            self.meio = self.meio + '\033[31m'+self.matriz[conta][auxColuna]+'\033[0;0m'
                        elif (str(conta)+str(auxColuna)) in self.listaNaoPodeMudar:
                            self.meio = self.meio + '\033[32m'+self.matriz[conta][auxColuna]+'\033[0;0m'                                                            
                        else:
                            self.meio =self. meio + self.matriz[conta][auxColuna]
                        
                        passou = 1
                        auxColuna = auxColuna+1
                    else:
                        self.meio = self.meio +' '
                        passou = 0
                    
            print(str(conta+1)+self.meio)
            aux = 0
            for i in range(28):
                if i == 0: 
                    self.risco = chr(9507)
                elif i == 27:
                    self.risco = self.risco+chr(9507)
                elif (aux+3)==i:            
                    self.risco = self.risco+chr(9507)
                    aux = aux+3            
                else:
                    self.risco = self.risco+chr(9473)
                
                                
            print(' '+self.risco)
        print(numeracao)
        

    #leArquivoHumano()