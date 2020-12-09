#Afonso Freitas | 99173
## O utilizador podera jogar o jogo se seguir as instrucoes representadas na ultima funcao, essas instrucoes estao a cinzento
def eh_tabuleiro(tabuleiro):
    #tabuleiro (tuplo) --> True or False
    """
    esta funcao verifica se o argumento 'tabuleiro' corresponde a um tabuleiro de jogo
    
    o tabuleiro com 3 colunas e 3 linhas deve ser representada por um tuplo, onde cada linha tambem e um.
    em cada posicao, do tabuleiro, so podera existir um numero inteiro, sendo ele ou 1 ou -1 ou 0).
    Se alguma das condicoes nao seja respeitada, retorna 'False', caso contrario retorna 'True'
    """
    
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
    #posicao(inteiro) --> booleano
    """
    esta funcao verifica se o argumento 'posicao' corresponde a uma posicao do jogo
    
    le o argumento 'posicao' e verifica se um dado numero corresponde a uma posicao do tabuleiro
    caso corresponda retorna 'True', senao retorna 'False'
    """
    
    if type(posicao)==int and 0 < posicao <= 9 : #verifica se um dado numero corresponde a uma posicao da tabuleiro
        return True
    
    else:
        return False  
      
def obter_coluna(tabuleiro, numero_coluna):
    #tabuleiro (tuplo),numero_coluna(inteiro) --> coluna (tuplo)
    """
    esta funcao obtem qualquer coluna do tabuleiro,
    
    a funcao retorna um tuplo correspondente a uma coluna do tabuleiro
    verifica se e possivel executar a funcao, e se os argumentos sao validos, se nao forem rais 'ValueErro'
    a coluna e selecionada com base no argumento 'numero_coluna', e as caracteristicas do 'tabuleiro'
    """
    
    if numero_coluna not in (1,2,3) or type(numero_coluna) !=int or not eh_tabuleiro(tabuleiro): #verifica se e possivel continuar a funcao, e se os argumentos sao validos   
        raise ValueError("obter_coluna: algum dos argumentos e invalido")
    
    coluna=()
    for i in range(3):         
        coluna = coluna + (tabuleiro[i][numero_coluna - 1],)                                     #retornar um tuplo com a coluna escolhida             
                                                                                
    return coluna  



def obter_linha(tabuleiro, numero_linha):
    #tabuleiro (tuplo),numero_linha(inteiro) --> linha (tuplo)
    """
    esta funcao obtem qualquer linha do tabuleiro
    
    a funcao retorna um tuplo correspondente a uma linha do tabuleiro
    a linha e selecionada com base no argumento 'numero_linha', e as caracteristicas do 'tabuleiro',
    """ 
    if numero_linha not in (1,2,3) or type(numero_linha)!=int or not eh_tabuleiro(tabuleiro):    #verifica se e possivel continuar a funcao, e se os argumentos sao validos  
        raise ValueError("obter_linha: algum dos argumentos e invalido")
    else:
        linha = tabuleiro[numero_linha-1]                                                        #guardar e retornar um tuplo com a coluna escolhida
    return linha


def obter_diagonal(tabuleiro, valor_diagonal):
    #tabuleiro (tuplo),valor_diagonal(inteiro) --> diagonal (tuplo)
    """
    obtem qualquer diagonal do tabuleiro, 
    
    a funcao retorna um tuplo correspondente a uma diagonal do tabuleiro
    a diagonal e selecionada com base no argumento 'valor_diagonal', e as caracteristicas do 'tabuleiro'
    a diagonal e escrita da esquerda para a direita, e obtem a diagonal crescente,da esquerda para a direita, se 'valor_diagonal'== 2, 
    e decrescente,da esquerda para a direita, caso 'valor_diagonal' seja 1 inteiro
    """ 
    
    if valor_diagonal not in (1,2) or type(valor_diagonal) != int or not eh_tabuleiro(tabuleiro):    #verifica atraves dos argumentos 'tabuleiro', e 'valor_diagonal' se e possivel extrair uma diagonal, 'raise ValueErro' se nao for possivel
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")
    diagonal=()
    if valor_diagonal == 1:
        for i in range(3):                                                                         
            diagonal = diagonal +(tabuleiro[i][i],)                                                   #caso 'valor_diagonal' == 1 retorna a diagonal decrescente                         
            
    else:
        for i in range(3):
            diagonal = diagonal +(tabuleiro[-i+2][i],)                                                #caso 'valor_diagonal' == 2 retorna a diagonal decrescente
            
    return diagonal                                                                                   #retorna diagonal

def tabuleiro_str(tabuleiro):
    #tabuleiro (tuplo) --> fotocopia(string)
    """
    esta funcao retorna uma string correspondente a uma interpretacao grafica do 'tabuleiro'
    
    em cada posicao vai substituir o seu valor por 'X' caso seja 1,
    por 'O' caso seja -1
    por '  ' caso seja 0
    as linhas sao separadas por "\n-----------\n" e as colunas por '|'
    """
    
    if not eh_tabuleiro(tabuleiro):           #verifica atraves dos argumento 'tabuleiro',se e possivel executar a funcao 'raise ValueErro' senao for possivel
        raise ValueError("tabuleiro_str: o argumento e invalido")
    
    fotocopia= ''
    
    for i in range(3):
        linha = obter_linha(tabuleiro, i+1)
        
        for j in range(len(linha)):
            
            if linha[j] == 1:                  #se na 'posicao' do 'tabuleiro' existir um '1', guarda na string "fotocopia" ' X '
                fotocopia = fotocopia + " X "  
                
            elif linha[j] == -1:               #se na 'posicao' do 'tabuleiro' existir um '-1', guarda na string "fotocopia" ' O '
                fotocopia = fotocopia + " O "
                
            else:                              #se na 'posicao' do 'tabuleiro' existir um '1', guarda na string  "fotocopia" '   '
                fotocopia = fotocopia + "   "
                
            if j != 2:                         #se a 'posicao' nao estiver na ultima coluna, guarda na string "fotocopia" '|'
                fotocopia = fotocopia + "|"
                
            elif i == 2:                       #se a 'posicao' for a ultima posicao do tabuleiro, guarda na string "fotocopia" ''
                fotocopia = fotocopia + ""
                
            else:                              #se  a 'posicao' for a ultima posicao de uma linha, guarda na string "fotocopia" "\n-----------\n"
                fotocopia = fotocopia + "\n-----------\n"
                
    return fotocopia                           #retorna "fotocopia"

def eh_posicao_livre(tabuleiro,posicao):
    #tabuleiro(tuplo),posicao(inteiro) --> True or False
    """
    verificar se uma dada posicao do tabuleiro e livre
    
    vai verificar se e possivel executar a funcao atraves dos argumentos dados
    transformar a posicao em um conjunto de indexs do tabuleiro e vai verificar se nessa posicao, existe o inteiro '0'
    se existir vai retornar 'True' caso contrario vai retornar 'False'
    """
    
    if not eh_posicao(posicao) or not eh_tabuleiro(tabuleiro):  #verifica atraves dos argumentos 'tabuleiro' e 'posicao',se e possivel executar a funcao 'raise ValueError' se nao for possivel
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido") 
    
    if tabuleiro[(posicao-1)//3][(posicao-1)%3] == 0:           #tabela[(posicao-1)//3][(posicao-1)%3] corresponde a posicao no tabuleiro, caso seja 0 entao estamos perante uma posicao livre e retorna'True'
        return True
    
    else:                                                       #senao retorna 'False'
        return False
    
def obter_posicoes_livres(tabuleiro):
    #tabuleiro(tuplo)--> posicoes_livres(tuplo)
    """
    obtem num unico tuplo todas as posicoes livres do tabuleiro  
    
    vai verificar se e possivel executar a funcao atraves dos argumentos dados
    vai colocar a funcao 'eh_posicao' num loop passando por todas as posicoes possiveis
    quando a funcao 'eh_posicao' apresentar 'True' vais armazenar num tuplo,executa ate terminar o loop 'for'
    """
    posicoes_livres=()
    
    if not eh_tabuleiro(tabuleiro):
        raise ValueError ("obter_posicoes_livres: o argumento e invalido")  #verifica atraves do argumento 'tabuleiro' ,se e possivel executar a funcao,se nao for possivel 'raise ValueErro'
    
    for i in range(1,10,1):
        
        if eh_posicao_livre(tabuleiro,i):
            posicoes_livres = posicoes_livres + (i,)                        #verifica em loop se uma dada posicao 'eh_posicao_livre' se for adiciona a 'posicoes_livres' 
            
    return posicoes_livres                                                  #retorna 'posicoes_livres' 

def jogador_ganhador(tabuleiro):
    #tabuleiro(tuplo) --> verificao((1,-1)(inteiro)) ou 0(int)  
    """
    indica qual jogador ganhou, caso nenhum tenha ganho return '0'
    
    vai verificar se e possivel executar a funcao atraves dos argumentos dados
    vai a todas as linhas/colunas/diagonais e verifica se em alguma os elementos sao todos iguais e diferentes de 0
    caso tenha encontrado um valor onde essa condicao se verifique a funcao vai retornar o sinal correspondente a essa linha/coluna/diagonal
    senao retorna '0'
    """   
    
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("jogador_ganhador: o argumento e invalido")                    #verifica atraves do argumento 'tabuleiro' ,se e possivel executar a funcao,se nao for possivel 'raise ValueError'  
    
    for i in range(1,4):
        verificacao = obter_linha(tabuleiro, i)
        
        if verificacao[0] == verificacao[1] == verificacao[2] and verificacao[2]!= 0:   #verifacao numa linha, se for tudo igual e diferente de 0, retorna o elemento da linha
            return verificacao[0]   
        
        verificacao = obter_coluna(tabuleiro, i)
        
        if verificacao[0] == verificacao[1] == verificacao[2] and verificacao[2]!= 0:   #verifacao numa coluna, se for tudo igual e diferente de 0, retorna o elemento da coluna
            return verificacao[0]
        
    for i in range(1,3):
        verificacao = obter_diagonal(tabuleiro, i)
        
        if verificacao[0] == verificacao[1] == verificacao[2] and verificacao[0] != 0:  #verifacao numa diagonal, se for tudo igual e diferente de 0, retorna o elemento da diagonal
            return verificacao[0] 
        
    return 0                                                                            #caso nada se verifique retorna ' 0 '                                                              

def marcar_posicao(tabuleiro,sinal,posicao):
    #tabuleiro(tuplo),sinal(inteiro),posicao(inteiro) --> tabuleiro(tuplo)
    """
    marca uma posicao livre do tabuleiro, por um 'sinal' representativo de 'X' ou 'O'
    
    vai verificar se e possivel executar a funcao atraves dos argumentos dados
    transformar o tuplo tabuleiro numa lista, assim como a linha onde a 'posicao' se encontra
    trocar o conteudo da 'posicao'(livre) escolhida, pelo 'sinal' escolhido
    volta a transformar em tuplo e retorna o tabuleiro
    """
    
    if sinal not in [-1,1] or type(sinal) != int or not eh_tabuleiro(tabuleiro) or posicao not in obter_posicoes_livres(tabuleiro ):
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")
                                                 #verifica atraves dos argumentos 'tabuleiro','sinal','posicao' ,se e possivel executar a funcao,se nao for possivel 'raise ValueErro'  
    
    linha = (posicao-1)//3                       #determina a coluna e linha da posicao
    coluna = (posicao-1)%3
    
    tabuleiro_lista = list(tabuleiro)            #transforma o 'tabuleiro' e a linha onde se encontra a 'posicao' num tipo list
    linha_lista = list(tabuleiro[linha])
    
    linha_lista[coluna] = sinal                  #vai a posicao e troca o conteudo da 'posicao'(livre)  pelo 'sinal' escolhido(vai a coluna da linha)
    
    tabuleiro_lista[linha] = tuple(linha_lista)
    res = tuple(tabuleiro_lista)                 #volta a transformar a tabela e a linha onde se encontrava a 'posicao' num tuplo
    
    return res        
def centro(tabuleiro):
    
    #tabuleiro(tuplo) --> 'True' ou 'False'
    """
    ve se o centro esta livre
     
    se o centro do tabuleiro estiver livre, retorna 'True' caso contrario 'False'
    """ 
    
    if eh_posicao_livre(tabuleiro,5):           #se o centro do tabuleiro estiver livre, retorna 'True'
        return True
    
    else:                                       #caso contrario retorna 'False'
        return False                            
    
def  canto_lateral(tabuleiro):
    #tabuleiro(tuplo) --> pos(inteiro)
    """
    escolhe uma posicao livre no canto do tabuleiro, ou na lateral, caso nao exista uma posicao livre no canto 
     
    se um ou mais cantos estiverem livres, escolhe o canto com menor posicao
    se nenhum canto estiver livre, escolhe a lateral com menor posicao
    """  
    
    posicoes_livres = obter_posicoes_livres(tabuleiro)
    
    for pos in posicoes_livres:                 
        if pos in (1,3,7,9):                    #se algum dos cantos estiver livre, retorna a sua posicao
            return pos 
            
    for pos in posicoes_livres:
        
        if pos in (2,4,6,8):                    #se alguma das laterais estiver livre, retorna a sua posicao
            return pos 
        
def vitoria(tabuleiro,sinal):
    #tabuleiro(tuplo),sinal(int) --> pos(inteiro)
    """
    retorna numa lista as posicoes que daram a vitoria
     
    vai a todas as linhas/colunas/diagonais e verifica se em alguma delas aparece duas vezes o elemento 'sinal' e uma vez 'posicao livre'
    se respeitar a condicao adiciona a uma lista essas posicoes, que daram a vitoria
    depois de examinar cada uma das linhas/colunas/diagonais, retorna uma lista com as posicoes que daram a vitoria
    """
    
    lst = []                                                   #cria uma lista sem nenhum conteudo
    
    for i in range(1,4):
        linha = obter_linha(tabuleiro,i)                       #obtem todas as linhas possiveis
        
        if linha.count(sinal) == 2 and linha.count(0) == 1:
            lst =  lst + [(i-1)*3 + (linha.index(0)+1)]        #se em uma dessas linhas existerem duas posicoes com 'sinal' e uma posicao livre adiciona a lista, a posicao livre 
            
        coluna = obter_coluna(tabuleiro,i)                     #obtem todas as colunas possiveis
        
        if coluna.count(sinal) == 2 and coluna.count(0) == 1:
            lst = lst + [i + (coluna.index(0)*(3))]            #se em uma dessas colunas existerem duas posicoes com 'sinal' e uma posicao livre adiciona a lista, a posicao livre
            
        if i !=3:
            diagonal = obter_diagonal(tabuleiro,i)             #obtem as duas diagonais possiveis
        
            if diagonal.count(sinal) == 2 and diagonal.count(0) == 1:
                
                if i == 1:
                    lst = lst + [4*diagonal.index(0) + 1]     #se na primeira diagonal existir duas posicoes com 'sinal' e uma posicao livre adiciona a lista, a posicao livre
                
                else:
                    lst = lst + [-2*diagonal.index(0) + 7]    #se na segunda diagonal exister duas posicoes com 'sinal' e uma posicao livre adiciona a lista, a posicao livre
                
    return  lst                                               #retorna uma lista com posicoes livres, e que daram a vitoria
     
    
def canto_oposto(tabuleiro,sinal):
    #tabuleiro(tuplo),sinal(sinal) --> posicao(inteiro)
    """
    retorna a posicao correspondente a oposta de um canto ocupado pelo adversario
     
    vai as duas diagonais, e verifica se nas extermidades dessas existe uma posicao ocupada pelo adversario e outra posicao livre
    se respeitar a condicao, adiciona a uma lista a posicao, correspondente a oposta de um canto ocupado pelo adversario
    depois de examinar cada uma das diagonais, retorna uma lista com as posicoes que respeitem as condicoes impostas
    """    
           
    lst =[]                                          #cria uma lista sem nenhum conteudo
    
    for i in range(1,3):
        diagonal = obter_diagonal(tabuleiro,i)       #obtem as duas diagonais possiveis
        
        if (diagonal[0] == -sinal and diagonal[2] == 0) or (diagonal[2] == -sinal and diagonal[0] == 0): 
                                                     #verifica se numa das extermidades existe uma posicao ocupada pelo adversario e outra livre
            if i == 1:
                
                if diagonal[0] == 0:
                    lst = lst + [1]                  #obtem numa lista as posicoes livres
                    
                else:
                    lst = lst + [9]
                    
            else:
                
                if diagonal[2] == -sinal:
                    lst = lst + [7]
                                                     #obtem numa lista as posicoes livres
                else:
                    lst = lst + [3]
                    
    if lst != []: 
        return  min(lst)                             #retorna o menor inteiro da lista, caso a lista apresente conteudo
    
    else:
        return 0                                     #senao, retorna 0
    
def Bifurcacao(tabuleiro,sinal):
    #tabuleiro(tuplo),sinal(sinal) --> posicao(inteiro)
    """
    retorna a posicao correspondente a posicao livre onde e possivel uma bifurcacao,
    
    isto e se jogar numa posicao onde haja bifuracao, na ronda seguinte fica com duas possibelidades de ganhar
    comeca por retornar uma lista onde existem todas as posicoes livres
    quando em uma posicao se poder ganhar em mais que uma vez, coloca numa outra lista
    """     
    
    lst= obter_posicoes_livres(tabuleiro)                             #obtem uma lista com as posicoes livres, 'lst'
    res=[]
    
    for index in lst:
        tabuleiro_temporario = marcar_posicao(tabuleiro,sinal,index)  #vai a posicao livre e 'marca_posicao', para um 'tabuleiro_temporario' com o 'sinal', em loop
        
        if len(vitoria(tabuleiro_temporario,sinal)) > 1:              #se existir mais que uma vitoria coloca a posicao numa lista, 'res'    
            res =res + [index]            
        
    return list(set(res))                                             #remove os elementos duplicados de 'res' e retorna em formato de lista
    
def def_bifurcacao(tabuleiro,sinal):
    #tabuleiro(tuplo),sinal(sinal) --> posicao(inteiro)
    """
    retorna a posicao, que defende de uma possivel bifurcacao,
    
    isto e se o adversario tiver a possibilidade de jogar numa posicao onde haja uma 'bifuracao', jogar de forma a nao permitir essa jogada
    se nao for possivel essa 'bifurcacao' do adversario, retorna nada
    se existir uma 'bifurcacao' do adversario, escolher essa posicao
    se existir mais que uma 'bifurcacao' do adversario, retorna uma posicao que provoque o adversario a nao criar uma bifurcacao
    """    
    
    lst = Bifurcacao(tabuleiro,-sinal)    #analisa onde podera exisitir uma bifurcao do adversario, e adiciona os possiveis valores numa lista 'lst'
    
    if lst == []:                         
        return                            #se nao for possivel uma bifurcacao, retorna nada
    
    if len(lst) == 1: 
        return min(lst)                   #se for possivel uma unica bifurcacao, retorna essa posicao
    
    else:                                 #se for possivel varias bifurcacoes, executa o codigo em baixo
        lstt=list(obter_posicoes_livres(tabuleiro))
        lstt.sort()                       #obtem as posicoes livres,e ordena, numa lista 
        
        for i in lstt:                                                          #inicializa um loop 'for' que passe por todas as posicoes livres
            tabuleiro_temporaria = marcar_posicao(tabuleiro,sinal,i)            #cria um tabuleiro_temporario, onde trocou-se uma das 'posicoes_livres'(i) pelo 'sinal'
            lst_vitoria= vitoria(tabuleiro_temporaria,sinal)                    #poe numa lista as posicoes que darao a vitoria, nesse novo 'tabuleiro_temporario' 
            lst_Bi=Bifurcacao(tabuleiro_temporaria,-sinal)                      #poe numa lista as posicoes que podem originar uma bifurcacao para o adversario
                                                                       
            if lst_Bi:                                     #se tiver marcado numa posicao que deixe de exisir bifurcacao, retorna essa posicao
                if len(lst_vitoria) != 0:                  #se a posicao marcada nao originar uma vitoria para o jogador, repete o loop funcao, caso contrario
                    
                    if min(lst_vitoria) not in lst_Bi:     #se a posicao marcada originar uma vitoria para o jogador, e nao cria uma situacao de bifurcacao para o adversario retornar essa posicao
                        return i    
            else:
                return i  

def normal(tabuleiro,sinal,modo_de_jogo):
    #tabuleiro(tuplo),sinal(sinal),modo_de_jogo(string) --> posicao(inteiro)
    """
    retorna a posicao conforme as regras do enunciado, no modo de jogo, normal,
    
    ista funcao executa as funcoes por ordem, vitoria, defesa(executar a funcao vitoria como se fosse o adversario), centro , canto_oposto, e canto_lateral
    """    
    
    if vitoria(tabuleiro,sinal):             #se der vitoria retornar a posicao da funcao
        lst = vitoria(tabuleiro,sinal) 
        return min(lst)
    
    elif vitoria(tabuleiro,-sinal):          #se der vitoria para o adversario retornar a posicao da funcao
        lst = vitoria(tabuleiro,-sinal)
        return min(lst)
    
    elif centro(tabuleiro):                  #se der o centro estiver livre retornar a posicao centro
        return 5
    
    elif canto_oposto(tabuleiro,sinal):      #se o canto oposto estiver livre retornar a posicao correspondente ao canto oposto
        return canto_oposto(tabuleiro,sinal) 
    
    return canto_lateral(tabuleiro)          #retornar um dos centros ou uma das laterais

def perfeito(tabuleiro, sinal, modo_de_jogo):
    #tabuleiro(tuplo),sinal(sinal),modo_de_jogo(string) --> posicao(inteiro)
    """
    retorna a posicao conforme as regras do enunciado, no modo de jogo, perfeito,
    
    isto executa as funcoes por ordem, vitoria, defesa(executar a funcao vitoria como se fosse o adversario),bifurcacao,def_bifurcacao, centro , canto_oposto, e canto_lateral
    """       
    if vitoria(tabuleiro,sinal):
        lst = vitoria(tabuleiro,sinal)           #se der vitoria retornar a posicao da funcao
        return min(lst)
     
    elif vitoria(tabuleiro,-sinal):              #se der vitoria para o adversario retornar a posicao da funcao
        lst = vitoria(tabuleiro,-sinal)
        return min(lst)       
    
    if Bifurcacao(tabuleiro,sinal):              #se existir uma bifurcacao, retorna a sua posicao
        lst = Bifurcacao(tabuleiro,sinal)
        return min(lst)
    
    if def_bifurcacao(tabuleiro,sinal):          #se existir uma bifurcacao para o adversario, retorna a posicao que nao deixa o adversario joga-la
        return def_bifurcacao(tabuleiro,sinal) 
    
    elif centro(tabuleiro):                      #se der para jogar no centro, retornar a posicao centro
        return 5
    
    elif canto_oposto(tabuleiro,sinal):          #se o canto oposto estiver livre, a posicao correspondente ao canto oposto
        return canto_oposto(tabuleiro,sinal)
    
    return canto_lateral(tabuleiro)              #retornar um dos centros ou uma das laterais

    
    
    
    
def escolher_posicao_auto(tabuleiro, sinal, modo_de_jogo):
    #tabuleiro(tuplo),sinal(sinal),modo_de_jogo(string) --> posicao(inteiro)
    """
    retorna a posicao conforme as caracteristicas do 'tabuleiro', o 'sinal' e 'modo_de_jogo'
    
    verifica se e possivel executar a funcao
    retorna a posicao conforme as caracteristicas do 'tabuleiro', o sinal e 'modo_de_jogo'
    """  
    
    if sinal not in [-1,1] or type(sinal) != int or not eh_tabuleiro(tabuleiro) or modo_de_jogo not in ('basico','normal','perfeito') or not obter_posicoes_livres(tabuleiro):
        raise ValueError ('escolher_posicao_auto: algum dos argumentos e invalido')
                                                     #verifica atraves dos argumentos 'tabuleiro','sinal','posicao' ,se e possivel executar a funcao,se nao for possivel 'raise ValueErro' 
    if modo_de_jogo=='basico':                       #se o modo_de_jogo basico for escolhido executa por ordem e retorna, centro,canto_lateral
        if centro(tabuleiro):
            return 5
        
        return canto_lateral(tabuleiro) 
    
    if modo_de_jogo == 'normal':                    #se o modo_de_jogo 'normal' for escolhido retorna e executa a funcao 'normal'
        return normal(tabuleiro, sinal, modo_de_jogo)
    
    if modo_de_jogo == 'perfeito':                  #se o modo_de_jogo 'perfeito' for escolhido retorna e executa a funcao 'normal'
        return perfeito(tabuleiro, sinal, modo_de_jogo)
    
def escolher_posicao_manual(tabuleiro):
    #tabuleiro(tuplo) --> posicao(inteiro)
    """
    o jogador escolhe manualmente a posicao que quer jogar
    
    verifica se e possivel executar a funcao com base no argumento'tabuleiro'
    o jogador escolhe uma posicao, se a posicao for invalida ou nao estiver livre, raise 'ValueError'
    """    
    
    if not eh_tabuleiro(tabuleiro):
        raise ValueError ('escolher_posicao_manual: o argumento e invalido') 
    
    posicao_escolhida = eval(input('Turno do jogador. Escolha uma posicao livre: '))            #o jogador escolhe a posicao, apos print de 'Turno do jogador. Escolha uma posicao livre: '
    
    if posicao_escolhida in obter_posicoes_livres(tabuleiro) and type(posicao_escolhida)== int: #verifica a escolha se for valida retorna a posicao escolhida, senao raise 'ValueError'
        return  posicao_escolhida                                   
    
    else:
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida') 
    
    
def Turno_Computador(tabuleiro,sinal,modo_de_jogo):
    #tabuleiro(tuplo),sinal(tuplo),modo_de_jogo(String) --> tabuleiro(tuplo)
    """
    esta funcao retorna o tabuleiro apos uma a escolha do computador
    
    o computador vai escolher automaticamente uma posicao automaticamente
    na funcao altera-se o 'tabuleiro', marcando a posicao escolhida pelo computador, com 'sinal' correspondente ao oposto do jogador 
    esta funcao ainda imprime o tabuleiro de jogo alterado, antes de retorna-lo
    """ 
    
    print('Turno do computador (', modo_de_jogo,'):',sep='') 
    tabuleiro = marcar_posicao(tabuleiro,-sinal,escolher_posicao_auto(tabuleiro, -sinal, modo_de_jogo))#o computador escolhe uma posicao, e marca a posicao escolhida no tabuleiro
    print(tabuleiro_str(tabuleiro)) 
    return tabuleiro
    
def Turno_Jogador(tabuleiro,sinal,modo_de_jogo):
    #tabuleiro(tuplo),sinal(tuplo),modo_de_jogo(String) --> tabuleiro(tuplo)
    """
    esta funcao retorna o tabuleiro apos uma escolha de posicao do jogador
    
    ao jogador e perguntado qual posicao quer jogar, se a posicao for invalida raise 'ValueError'
    na funcao altera-se o 'tabuleiro', marcando na posicao escolhida, o sinal que o jogador escolheu
    esta funcao ainda imprime o tabuleiro de jogo alterado, antes de retorna-lo
    """ 
    
    posicao = escolher_posicao_manual(tabuleiro)        #o jogador escolhe uma posicao
    tabuleiro = marcar_posicao(tabuleiro,sinal,posicao) #marca a posicao escolhida no tabuleiro
    print(tabuleiro_str(tabuleiro)) 
    
    return tabuleiro
    

    
    
    

def jogo_do_galo(X_ou_O,modo_de_jogo):
    #X_ou_O(string), modo_de_jogo(string) --> executa um jogo --> retorna o vencedor ('X','O','EMPATE')
    
    ##funcao principal do programa, o utilizador podera escrever na consola 'jogo_do_galo(X_ou_O,modo_de_jogo)' para jogar o jogo do galo
    ## X_ou_O tera de ser ou 'X' ou 'O'
    ## e o modo de jogo 'basico','normal','perfeito'
    
    """
    o jogador escolhe com que simbolo quer jogar , X_ou_O, e o modo_de_jogo, joga uma partida contra um computador,e depois retorna o vencedor ('X','O','EMPATE')
    
    verifica se e possivel executar a funcao com base no argumento'X_ou_O', e o 'modo_de_jogo' escolhido
    o jogador escolhe com que caracter quer jogar se escolher o caracter 'X' comeca por ser ele a jogar, se escolher 'O' comeca o caracter 'X', o computador 
    """       
    if X_ou_O not in ('X','O') or modo_de_jogo not in ('basico','normal','perfeito'):   #verifica se e possivel continuar o jogo
        raise ValueError ('jogo do galo: algum dos argumentos e invalido')
    
    print('Bem-vindo ao JOGO DO GALO.')
    print('O jogador joga com \'',X_ou_O,'\'.', sep='')
    tabuleiro = ((0,0,0),(0,0,0),(0,0,0))
    if X_ou_O == 'X':
        sinal = 1                                                                        #o sinal 1 corresponde a 'X' e -1 corresponde a 'O'
        while True:                                                                      #loop que so para quando executar o comando 'break'
            tabuleiro = Turno_Jogador(tabuleiro,sinal,modo_de_jogo)                      #turno do Jogador
            if jogador_ganhador(tabuleiro) != 0 or not obter_posicoes_livres(tabuleiro): #verifica se ainda e possivel continuar o jogo
                break
            
            tabuleiro = Turno_Computador(tabuleiro,sinal,modo_de_jogo)                    #turno do computador
            if jogador_ganhador(tabuleiro) != 0 or not obter_posicoes_livres(tabuleiro):  #verifica se ainda e possivel continuar o jogo
                break      
            
    else:
        sinal = -1
        while True:                                                                       #loop que so para quando executar o comando 'break'
            tabuleiro = Turno_Computador(tabuleiro,sinal,modo_de_jogo)                    #turno do computador                                               
            if jogador_ganhador(tabuleiro) != 0 or not obter_posicoes_livres(tabuleiro):  #verifica se ainda e possivel continuar o jogo
                break
            
            tabuleiro = Turno_Jogador(tabuleiro,sinal,modo_de_jogo)                       #turno do Jogador
            if jogador_ganhador(tabuleiro) != 0 or not obter_posicoes_livres(tabuleiro):  #verifica se ainda e possivel continuar o jogo
                break    
             
    if jogador_ganhador(tabuleiro) == 1:            #verifica o jogador_ganhador tiver o sinal 1 for o vencedor retorna 'X'
        return 'X'
    
    elif jogador_ganhador(tabuleiro) == -1:         #verifica o jogador_ganhador tiver o sinal -1 for o vencedor retorna 'O'
        return 'O'
    
    else:                                           #se nenhum jogador venceu retorna 'EMPATE'
        return 'EMPATE'
    
print(jogo_do_galo('X','perfeito'))

    
    
