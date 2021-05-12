from lista_possiveis_movimentos import lista_movimentos_possiveis
from cria_baralho import cria_baralho
from empilha_carta import empilha
from extrai_naipe import extrai_naipe
from possui_movimentos_possiveis import possui_movimentos_possiveis
from extrai_valor import extrai_valor
class bcolors:
 purple = '\033[95m'
 blue = '\033[94m'
 green = '\033[92m'
 yellow = '\033[93m'
 red = '\033[91m'
 end = '\033[0m'

def cores(n):
    x = str(extrai_naipe(n))
    if x == "♠":
        return bcolors.blue + n + bcolors.end
    if x == "♥":
        return bcolors.red + n + bcolors.end
    if x == "♣":
        return bcolors.purple + n + bcolors.end
    if x == "♦":
        return bcolors.yellow + n + bcolors.end
print('Paciência Acordeão') 
print('==================')

print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.') 

print('Existem apenas dois movimentos possíveis:') 

print('1. Empilhar uma carta sobre a carta imediatamente anterior;') 
print('2. Empilhar uma carta sobre a terceira carta anterior.') 

print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ')

print('1. As duas cartas possuem o mesmo valor ou')
print('2. As duas cartas possuem o mesmo naipe. ')

print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')
togui= True
while togui:
    baralho = cria_baralho()
    togui=False
play = True
while play:

    print('O estado atual do baralho é: ')

   
    if possui_movimentos_possiveis(baralho):
        for n, item in enumerate(baralho):
            y = n + 1
            print(y, item)
        toyota=True
        while toyota:
            carta_selecionada = int(input('Escolha uma carta (digite um número entre 1 e {0}): '.format(y))) - 1
            if carta_selecionada >= 1 and carta_selecionada < len(baralho):
                verimov=lista_movimentos_possiveis(baralho,carta_selecionada)
                if verimov==[1]:
                    baralho=empilha(baralho,carta_selecionada,carta_selecionada-1)
                    toyota=False
                if verimov==[3]:
                    baralho=empilha(baralho,carta_selecionada,carta_selecionada-3)
                    toyota=False
                if verimov==[1,3] or verimov==[3,1]:
                    gui=True
                    while gui:
                        ggui=int(input('Sobre qual carta você dejesa empilhar ({0} ou {1}): '.format(carta_selecionada,carta_selecionada-2)))-1
                        if ggui==carta_selecionada-1:
                            gui=False
                            toyota=False
                            baralho=empilha(baralho,carta_selecionada,carta_selecionada-1)
                            
                        if ggui==carta_selecionada-3:
                            gui=False
                            toyota=False
                            baralho=empilha(baralho,carta_selecionada,carta_selecionada-3)

                        else:
                            print('essa carta é invalida')
                if verimov==[]:
                    print('Essa carta não pode ser empilhada')
    if possui_movimentos_possiveis(baralho)==False and len(baralho)==1:
        print('você ganhou')
        play=False
        togui=input('você quer jogar de novo?(sim ou não) ')
        if togui=='sim':
            tog=True
            play=True
        else:
            print('até a próxima')
    if possui_movimentos_possiveis(baralho)==False:
        print('você perdeu')
        play=False
        togui=input('você quer jogar de novo?(sim ou não) ')
        if togui=='sim':
            tog=True
            play=True
        else:
            print('até a próxima')