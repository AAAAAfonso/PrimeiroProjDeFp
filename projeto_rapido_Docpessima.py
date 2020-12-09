#Afonso Freitas | 99173
def eh_tabuleiro(tabuleiro):
    
    #---------------------------------------------------------------------------------------------------#
    #esta funcao verifica se o argumento 'tabuleiro' corresponde a um tabuleiro, com 3 colunas e 3 linhas.
    #o tabuleiro deve ser representada por um tuplo, onde cada linha tambem e um.
    #em cada posicao, do tabuleiro, so podera existir um numero inteiro, sendo ele ou 1 ou -1 ou 0).
    #Se alguma das condicoes nao seja respeitada, retorna 'False', caso contrario retorna 'True'
    #---------------------------------------------------------------------------------------------------#
    
    if isinstance(tabuleiro,tuple) and len(tabuleiro) == 3:    #verifica se o tabuleiro tem 3 linhas, e que o tabuleiro e represento por um tuplo
        for linha in tabuleiro:    
            if isinstance(linha, tuple) and len(linha) == 3:   #verifica se o tabuleiro tem 3 colunas, e que cada linha e representada por um tuplo
                for casa in linha:
                    if casa not in (1,-1,0) or not type(casa) ==int:    #verifica se em cada casa do tabuleiro, existe 1 ou -1 ou 0, e que cada linha e representada por um tuplo
                        return False 
            else:
                return False
    else:
        return False  
    return True 

def eh_posicao(posicao):
    
    #----------------------------------------------------------------------------------------------------#
    #le o argumento 'posicao' e verifica se um dado numero corresponde a uma posicao do tabuleiro
    #caso corresponda retorna 'True', senao retorna 'False'
    #----------------------------------------------------------------------------------------------------#
    
    if type(posicao)==int and 0 < posicao <= 9 : #verifica se um dado numero corresponde a uma posicao da tabuleiro
        return True
    else:
        return False    
def obter_coluna(tabuleiro, numero_coluna):
    
    #----------------------------------------------------------------------------------------------------#
    #obtem qualquer coluna da tabuleiro,a funcao retorna um tuplo correspondente a coluna do tabuleiro
    #a coluna e selecionada com base no argumento 'numero_coluna', e as caracteristicas do 'tabuleiro'
    #----------------------------------------------------------------------------------------------------#
    
    if numero_coluna not in (1,2,3) or type(numero_coluna) !=int or not eh_tabuleiro(tabuleiro):   #verifica atraves dos argumentos 'tabuleiro', e 'numero_coluna' se e possivel extrair uma coluna, 'raise ValueErro' se nao for possivel
        raise ValueError("obter_coluna: algum dos argumentos e invalido")
    coluna=()
    for i in range(3):         
        coluna = coluna + (tabuleiro[i][numero_coluna - 1],)           #adiciona a um tuplo 'coluna', os valores da coluna escolhida de forma ordenada
    return coluna                                         #retorna o tuplo 'coluna'
def obter_linha(tabuleiro, numero_linha):
    
    #----------------------------------------------------------------------------------------------------#
    #obtem qualquer linha do tabuleiro, a funcao retorna um tuplo correspondente a uma linha do tabuleiro
    #a linha e selecionada com base no argumento 'numero_linha', e as caracteristicas do 'tabuleiro'
    #----------------------------------------------------------------------------------------------------#   
    
    if numero_linha not in (1,2,3) or type(numero_linha)!=int or not eh_tabuleiro(tabuleiro):      #verifica atraves dos argumentos 'tabuleiro', e 'numero_linha' se e possivel extrair uma linha, 'raise ValueErro' se nao for possivel
        raise ValueError("obter_linha: algum dos argumentos e invalido")
    else:
        linha = tabuleiro[numero_linha-1]      #adiciona a um tuplo 'linha', a linha escolhida
    return linha  
def obter_diagonal(tabuleiro, valor_diagonal):
    
    #----------------------------------------------------------------------------------------------------#
    #obtem qualquer diagonal do tabuleiro, a funcao retorna um tuplo correspondente a uma diagonal do tabuleiro
    #a diagonal e selecionada com base no argumento 'valor_diagonal', e as caracteristicas do 'tabuleiro'
    #a diagonal e escrita da esquerda para a direita, e obtem a diagonal crescente,da esquerda para a direita, se 'valor_diagonal'== 2, e decrescente,da esquerda para a direita, se 'valor_diagonal' == 1
    #----------------------------------------------------------------------------------------------------#  
    
    if valor_diagonal not in (1,2) or type(valor_diagonal) != int or not eh_tabuleiro(tabuleiro):    #verifica atraves dos argumentos 'tabuleiro', e 'valor_diagonal' se e possivel extrair uma diagonal, 'raise ValueErro' se nao for possivel
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")
    diagonal=()
    if valor_diagonal == 1:
        for i in range(3):
            diagonal = diagonal +(tabuleiro[i][i],)
    else:
        for i in range(3):
            diagonal = diagonal +(tabuleiro[-i+2][i],)       
    return diagonal  #retorna diagonal

def tabuleiro_str(tabuleiro):
    #----------------------------------------------------------------------------------------------------#
    #a funcao retorna uma string correspondente a uma interpretacao grafica do 'tabuleiro'
    #----------------------------------------------------------------------------------------------------#     
    if not eh_tabuleiro(tabuleiro):        #verifica atraves dos argumento 'tabuleiro',se e possivel executar a funcao 'raise ValueErro' senao for possivel
        raise ValueError("tabuleiro_str: o argumento e invalido")    
    fotocopia= ''
    for i in range(3):
        linha = obter_linha(tabuleiro, i+1)
        for j in range(len(linha)):
            if linha[j] == 1:
                fotocopia = fotocopia + " X "  
            elif linha[j] == -1:
                fotocopia = fotocopia + " O "
            else:
                fotocopia = fotocopia + "   "
            if j != 2:
                fotocopia = fotocopia + "|"
            elif i == 2:
                fotocopia = fotocopia + ""
            else: 
                fotocopia = fotocopia + "\n-----------\n"
    return fotocopia
def eh_posicao_livre(tabuleiro,posicao):
    
    #----------------------------------------------------------------------------------------------------#
    #esta funcao verifica se o argumento 'posicao' corresponde a uma posicao livre do 'tabuleiro',
    #----------------------------------------------------------------------------------------------------#  
    
    if not eh_posicao(posicao) or not eh_tabuleiro(tabuleiro):  #verifica atraves dos argumentos 'tabuleiro' e 'posicao',se e possivel executar a funcao 'raise ValueErro' se nao for possivel
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido") 
    if tabuleiro[(posicao-1)//3][(posicao-1)%3] == 0:  #tabela[(posicao-1)//3][(posicao-1)%3] corresponde a posicao no tabuleiro, caso seja 0 entao estamos perante uma posicao livre  
        return True
    else:
        return False
def obter_posicoes_livres(tabuleiro):
    #----------------------------------------------------------------------------------------------------#
    #obtem num unico tuplo com todas as posicoes livres do tabuleiro
    #----------------------------------------------------------------------------------------------------#        
    posicoes_livres=()
    if not eh_tabuleiro(tabuleiro):
        raise ValueError ("obter_posicoes_livres: o argumento e invalido")  #verifica atraves do argumento 'tabuleiro' ,se e possivel executar a funcao,se nao for possivel 'raise ValueErro'
    for i in range(1,10,1):
        if eh_posicao_livre(tabuleiro,i):
            posicoes_livres = posicoes_livres + (i,)    #verifica em loop se uma dada posicao 'eh_posicao_livre' se for adiciona a 'posicoes_livres' 
    return posicoes_livres    
def jogador_ganhador(tabuleiro):
    #----------------------------------------------------------------------------------------------------#
    #determina se houve ou nao um jogador_ganhador do JOGO DO GALO
    #----------------------------------------------------------------------------------------------------#     
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("jogador_ganhador: o argumento e invalido")    #verifica atraves do argumento 'tabuleiro' ,se e possivel executar a funcao,se nao for possivel 'raise ValueErro'           
    for i in range(1,4):
        verificacao = obter_linha(tabuleiro, i)
        if verificacao[0] == verificacao[1] == verificacao[2] and verificacao[2]!= 0:
            return verificacao[0]                   
        verificacao = obter_coluna(tabuleiro, i)
        if verificacao[0] == verificacao[1] == verificacao[2] and verificacao[2]!= 0:
            return verificacao[0]
    for i in range(1,3):
        verificacao = obter_diagonal(tabuleiro, i)
        if verificacao[0] == verificacao[1] == verificacao[2] and verificacao[0] != 0:
            return verificacao[0] 
    return 0

def marcar_posicao(tabuleiro,sinal,posicao):
    #----------------------------------------------------------------------------------------------------#
    #marca numa 'posicao' do 'tabuleiro' um 'sinal', escolhido no argumento
    #----------------------------------------------------------------------------------------------------#     
    if sinal not in [-1,1] or type(sinal) != int or not eh_tabuleiro(tabuleiro) or posicao not in obter_posicoes_livres(tabuleiro ):
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")
    linha = (posicao-1)//3
    coluna = (posicao-1)%3
    tabuleiro_lista = list(tabuleiro)
    linha_lista = list(tabuleiro[linha]) 
    linha_lista[coluna] = sinal                  #transforma o tabuleiro numa lista, troca o valor numa posicao e por fim retorna o tabuleiro
    tabuleiro_lista[linha] = tuple(linha_lista)
    res = tuple(tabuleiro_lista)
    return res        
def centro(tabuleiro):
    #----------------------------------------------------------------------------------------------------#
    #se o centro tiver vazio escolhe-o
    #----------------------------------------------------------------------------------------------------#     
    if eh_posicao_livre(tabuleiro,5):
        return True
    else:
        return False
def  canto_lateral(tabuleiro):
    #----------------------------------------------------------------------------------------------------#
    #se um canto tiver vazio, escolhe, senao, escolhe uma lateral
    #----------------------------------------------------------------------------------------------------#     
    posicoes_livres = obter_posicoes_livres(tabuleiro)
    for pos in posicoes_livres:
        if pos in (1,3,7,9):
                return pos 
    for pos in posicoes_livres:
        if pos in (2,4,6,8):
            return pos 
def vitoria(tabuleiro,sinal):
    #----------------------------------------------------------------------------------------------------#
    #se o jogador estiver perto de ganhar joga na posicao
    #----------------------------------------------------------------------------------------------------#     
    lst = []
    for i in range(1,4):
        linha = obter_linha(tabuleiro,i)
        if linha.count(sinal) == 2 and linha.count(0) == 1:
            lst =  lst + [(i-1)*3 + (linha.index(0)+1)]        
        coluna = obter_coluna(tabuleiro,i)
        if coluna.count(sinal) == 2 and coluna.count(0) == 1:
            lst = lst + [i + (coluna.index(0)*(3))]
    for i in range(1,3):
        diagonal = obter_diagonal(tabuleiro,i)
        if diagonal.count(sinal) == 2 and diagonal.count(0) == 1:
            if i == 1:
                lst = lst + [4*diagonal.index(0) + 1]
            else:
                lst = lst+[-2*diagonal.index(0) + 7]
    if lst != []:
        return  lst 
    else:
        return       
def canto_oposto(tabuleiro,sinal):
    #----------------------------------------------------------------------------------------------------#
    #se o jogador adversario tivesse jogado num canto, jogar no canto oposo
    #----------------------------------------------------------------------------------------------------#        
    lst =[]
    for i in range(1,3):
        diagonal = obter_diagonal(tabuleiro,i)
        if (diagonal[0] == -sinal and diagonal[2] == 0) or (diagonal[2] == -sinal and diagonal[0] == 0):
            if i == 1:
                if diagonal[0] == 0:
                    lst = lst + [1]
                else:
                    lst = lst + [9]
            else:
                if diagonal[2] == -sinal:
                    lst = lst + [7]
                else:
                    lst = lst + [3]
    if lst != []:
        return  min(lst) 
    else:
        return
def Bifurcacao(tabuleiro,sinal,defesa):
    #----------------------------------------------------------------------------------------------------#
    #se duas linhas/colunas/diagonais se intersetarem e for possivel vencer nessas, jogar
    #caso a defesa seja 0, a funcao entra em modo de ataque
    #se a defesa nao for 0, esta entra em modo defensivo
    #----------------------------------------------------------------------------------------------------#     
    if defesa==0:         
        lst= cheio_2livre(tabuleiro,sinal)
        res=[]
        for index in lst:
            if lst.count(index) > 1:
                res =res + [index]
            
        return list(set(res))
    else:
        lst = Bifurcacao(tabuleiro,-sinal,0) 
        if lst == []:
            return
        if len(lst) == 1:
            return min(lst)
        else:
            lstt=cheio_2livre(tabuleiro,sinal)
            lstt.sort()
            for i in lstt:
                tabuleiro_temporaria = marcar_posicao(tabuleiro,sinal,i)
                lst_vitoria= vitoria(tabuleiro_temporaria,sinal)
                lst_Bi=Bifurcacao(tabuleiro_temporaria,-sinal,0)
                if lst_Bi:
                    if len(lst_vitoria) == 1:
                        if min(lst_vitoria) not in lst_Bi:
                            return i 
                    else:
                        return i
                else:
                    return i  
def cheio_2livre(tabuleiro,sinal):
    #--------------------------------------------------------------------------#
    #se econtrar uma linha/coluna/diagonal com um 'sinal' e que seja possivel vencer obter num tuplo, o numero das posicoes
    #--------------------------------------------------------------------------#
    lst_l = []
    for i in range(1,4):
        linha = obter_linha(tabuleiro,i)
        if linha.count(sinal) == 1 and linha.count(0) == 2:
            lst = [0,1,2]
            del lst[linha.index(sinal)]
            for j in lst:
                lst_l = lst_l + [(i-1)*3 + (j+1)] 
                
        coluna = obter_coluna(tabuleiro,i)
        if coluna.count(sinal) == 1 and coluna.count(0) == 2:
            lst = [0,1,2]
            del lst[coluna.index(sinal)]
            for j in lst:
                lst_l = lst_l + [i + (j*(3))] 
                
    for i in range(1,3):
        diagonal = obter_diagonal(tabuleiro,i)
        if diagonal.count(sinal) == 1 and diagonal.count(0) == 2:
                if i == 1:
                    lst = [0,1,2]
                    del lst[diagonal.index(sinal)]
                    for j in lst:
                        lst_l = lst_l + [4*j + 1]      
                else:
                    lst = [0,1,2]
                    del lst[diagonal.index(sinal)]
                    for j in lst:
                        lst_l = lst_l+[-2*j + 7] 
    return lst_l  


def normal(tabuleiro,sinal,modo_de_jogo):
    if vitoria(tabuleiro,sinal):
        lst = vitoria(tabuleiro,sinal) 
        return min(lst)
    elif vitoria(tabuleiro,-sinal):
        lst = vitoria(tabuleiro,-sinal)
        return min(lst)
    elif centro(tabuleiro):
        return 5
    elif canto_oposto(tabuleiro,sinal):
        return canto_oposto(tabuleiro,sinal)        
    return canto_lateral(tabuleiro) 

def perfeito(tabuleiro, sinal, modo_de_jogo):
    if vitoria(tabuleiro,sinal):
        lst = vitoria(tabuleiro,sinal) 
        return min(lst)
    elif vitoria(tabuleiro,-sinal):
        lst = vitoria(tabuleiro,-sinal)
        return min(lst)       
    if Bifurcacao(tabuleiro,sinal,0):
        lst = Bifurcacao(tabuleiro,sinal,0)
        return min(lst)
    if Bifurcacao(tabuleiro,sinal,1):
        return Bifurcacao(tabuleiro,sinal,1)        
    elif centro(tabuleiro):
        return 5
    elif canto_oposto(tabuleiro,sinal):
        return canto_oposto(tabuleiro,sinal)         
    return canto_lateral(tabuleiro)    
    
    
    
    
def escolher_posicao_auto(tabuleiro, sinal, modo_de_jogo):
    if sinal not in [-1,1] or type(sinal) != int or not eh_tabuleiro(tabuleiro) or modo_de_jogo not in ('basico','normal','perfeito') or not obter_posicoes_livres(tabuleiro):
        raise ValueError ('escolher_posicao_auto: algum dos argumentos e invalido')
    if modo_de_jogo=='basico':
        if centro(tabuleiro):
            return 5
        return canto_lateral(tabuleiro) 
    if modo_de_jogo == 'normal':
        return normal(tabuleiro, sinal, modo_de_jogo)
    if modo_de_jogo == 'perfeito':
        return perfeito(tabuleiro, sinal, modo_de_jogo)
    
def escolher_posicao_manual(tabuleiro):
    if not eh_tabuleiro(tabuleiro):
        raise ValueError ('escolher_posicao_manual: o argumento e invalido')       
    posicao_escolhida = eval(input('Turno do jogador. Escolha uma posicao livre: '))
    if posicao_escolhida in obter_posicoes_livres(tabuleiro) and type(posicao_escolhida)== int:
        return  posicao_escolhida
    else:
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida') 

def jogo_do_galo(X_ou_O,modo_de_jogo): 
    if X_ou_O not in ('X','O') or modo_de_jogo not in ('basico','normal','perfeito'):
        raise ValueError ('jogo do galo: algum dos argumentos e invalido')
    print('Bem-vindo ao JOGO DO GALO.')
    print('O jogador joga com \'',X_ou_O,'\'.', sep='')
    tabuleiro = ((0,0,0),(0,0,0),(0,0,0))
    if X_ou_O == 'X':
        sinal = 1
        while True:
            posicao = escolher_posicao_manual(tabuleiro)
            tabuleiro = marcar_posicao(tabuleiro,sinal,posicao)
            print(tabuleiro_str(tabuleiro))
            if jogador_ganhador(tabuleiro) != 0 or not obter_posicoes_livres(tabuleiro):
                break
            print('Turno do computador (', modo_de_jogo,'):',sep='')
            tabuleiro = marcar_posicao(tabuleiro,-sinal,escolher_posicao_auto(tabuleiro, -sinal, modo_de_jogo))
            print(tabuleiro_str(tabuleiro))
            if jogador_ganhador(tabuleiro) != 0 or not obter_posicoes_livres(tabuleiro):
                break            
    else:
        sinal = -1
        while True:
            print('Turno do computador (', modo_de_jogo,'):',sep='')
            tabuleiro = marcar_posicao(tabuleiro,-sinal,escolher_posicao_auto(tabuleiro, -sinal, modo_de_jogo))
            print(tabuleiro_str(tabuleiro))
            if jogador_ganhador(tabuleiro) != 0 or not obter_posicoes_livres(tabuleiro):
                break
            posicao = escolher_posicao_manual(tabuleiro)
            tabuleiro = marcar_posicao(tabuleiro,sinal,posicao)
            print(tabuleiro_str(tabuleiro))
            if jogador_ganhador(tabuleiro) != 0 or not obter_posicoes_livres(tabuleiro):
                break          
    if jogador_ganhador(tabuleiro) == 1:
        return 'X'
    elif jogador_ganhador(tabuleiro) == -1:
        return 'O'
    else:
        return 'EMPATE'
