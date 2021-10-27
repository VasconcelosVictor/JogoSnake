import pygame
import pygame.pypm
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.5)

# pygame.draw.circle(tela, (0,0,255), (300,260),40)
# pygame.draw.line(tela,(255,255,0),(390,0),(390,600),5)
largura = 640
altura = 480

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)
velocidade = 10
x_controle = velocidade
y_controle = 0


x_maca = randint(40, 600)
y_maca = randint(50, 430)

fonte = pygame.font.SysFont('arial', 30, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO")
relogio = pygame.time.Clock()
pontos = 0

lista_cobra = []
comprimento_inicial = 5

morreu = False
def AumentaCobra(lista_cobra):
    for xey in lista_cobra:
        # XEY = [X,Y]
        # XEY[0] = X
        # XEY[1] = Y

        pygame.draw.rect(tela,(0,255,0),(xey[0],xey[1],20,20))

def ReiniciarOJogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial =5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca=[]
    x_maca = randint(40,600)
    y_maca = randint(50,430 )
    morreu = False


while True:  # O jOGO RODA NUM LOOP INFINITO

    relogio.tick(30)
    tela.fill((255, 255, 255))  # LIMPA A TELA
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:  # PEGA EVENTO DE FECHAR A TELA
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle =0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra +x_controle
    y_cobra = y_cobra + y_controle
    # PRIMEIRO PARAMETRO TELA ONDE VAI PARECER A IMAGEM
    # SEGUNGO COR (TUPLA), DIMENSON(TUPLA), X E Y DA LOCALIZAÇÃO E TAMANHO
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))

    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):  # MUDA A POSIÇÃO DO RETANGULO AZUL
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        comprimento_inicial= comprimento_inicial +1

        barulho_colisao.play()
    lista_cabeca = [] #ARMAZENDA A POSIÇÃO DA COBRA
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial',20,True,True)
        mensagem = 'Game Over! Pressione a tecla R pra jogar novamente'
        texto_formatado = fonte2.render(mensagem, True,(0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        ReiniciarOJogo()

            ret_texto.center = (largura//2,altura//2)
            tela.blit(texto_formatado,(ret_texto))
            pygame.display.update()
    if x_cobra > largura:
        x_cobra =0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0


    if len(lista_cobra) > comprimento_inicial:
       del lista_cobra[0]
    AumentaCobra(lista_cobra)

    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()

