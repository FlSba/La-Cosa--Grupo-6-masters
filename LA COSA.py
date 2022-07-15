#Nikolas Garcés, 21.358.930-k
#Sebastián Figueroa, 21.568.341-9
#Victoria Chambe, 21.199.807-5
#Maximiliano Araya, 21.376.338-5
import pygame
import info
import random

def main():
    pygame.init()
    pygame.display.init()
    pygame.font.init()
    screen=pygame.display.set_mode((1240,698))
    pygame.display.set_caption("La cosa")
    icono = pygame.image.load("icono.png")
    pygame.display.set_icon(icono)

    lista=[
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0], 
        [0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],
        [1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],
        [1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0], 
        [0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],
        [0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],
        [0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],
        [0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],
        [0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
        [2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
        [2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],
        [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
        ]
    corriendo=True
    """listaobjetos=info.lista_objetos(lista)
    xy=info.respawn(listaobjetos)
    xyn=[xy,2]
    xy=info.respawn(listaobjetos)
    xyn1=[xy,0,2]
    xy=info.respawn(listaobjetos)
    xyn2=[xy,0,2]
    xy=info.respawn(listaobjetos)
    xyn3=[xy,0,2]
    n=0"""

    reloj=pygame.time.Clock()
    corriendo=True
    Inicio=True
    Intruccion=False
    Juego=False
    Historia=False
    Inicio_Juego=True

    boton1=pygame.image.load("boton1.png")
    boton2=pygame.image.load("boton2.png")
    while corriendo:
        num=0
        reloj.tick(60)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                corriendo=False
            if event.type==pygame.KEYUP:#sacado del video de Jorge Ulloa https://www.youtube.com/watch?v=WQl5SuMfxpw
                tecla_presionada=pygame.key.name(event.key)
                if tecla_presionada=="w":
                    n=1
                if tecla_presionada=="s":
                    n=2
                if tecla_presionada=="a":
                    n=3
                if tecla_presionada=="d":
                    n=4
    
        if Inicio:
            num=inicio(screen,boton1,boton2)
            if num==2:
                Inicio=False
                Intruccion=True
            if num==1:
                Inicio=False
                Historia=True
            if num==3:
                corriendo=False
        num=0
        if Intruccion:
            num=intruccion(screen,boton2)
            if num==1:
                Intruccion=False
                Inicio=True
        num=0
        if Historia:
            num=historia(screen,boton1)
            if num==1:
                Historia=False
                Juego=True
        num=0
        if Juego:
            screen.fill((0,0,0))
            info.mapa(screen,lista)
            if Inicio_Juego:
                listaobjetos=info.lista_objetos(lista)
                xy=info.respawn(listaobjetos)
                xyn=[xy,2]
                xy=info.respawn(listaobjetos)
                xyn1=[xy,0,2]
                xy=info.respawn(listaobjetos)
                xyn2=[xy,0,2]
                xy=info.respawn(listaobjetos)
                xyn3=[xy,0,2]
                n=0
                Inicio_Juego=False
            info.Objetos(screen,listaobjetos)
            xyn1=info.monitos(screen,listaobjetos,xyn1)
            listaobjetos=info.recoge_pocion(xyn1,listaobjetos)
            xyn2=info.monitos(screen,listaobjetos,xyn2)
            listaobjetos=info.recoge_pocion(xyn2,listaobjetos)
            xyn3=info.monitos(screen,listaobjetos,xyn3)
            listaobjetos=info.recoge_pocion(xyn3,listaobjetos)
            xyn=info.monito(screen,listaobjetos,xyn,n)
            listaobjetos=info.recoge_pocion(xyn,listaobjetos)
            n=0
            if info.cuenta_pocion(listaobjetos):
                Juego=False
                Inicio=True
                Inicio_Juego=True
                if victoria:
                    num = victoria(screen, boton2)
                    if num == 1:
                        corriendo = False
                        victoria = True
                    num = 0

            

                
                
    pygame.display.quit()
        
def inicio(screen,boton1,boton2):
    inicio=pygame.image.load("Inicio.png")
    pygame.Surface.blit(screen,inicio,(0,0))

    Font=pygame.font.SysFont("Comic sans",20)
    Font1=pygame.font.SysFont("Comic sans",16)

    if info.boton_en_pantalla_imagen(screen,boton1,inicio,"START",Font,452,480,312,79,(0,0,0)):
        return(1)
    if info.boton_en_pantalla_imagen(screen,boton1,inicio,"INTRUCTION",Font1,480,580,266,75,(0,0,0)):
        return(2)
    if info.boton_en_pantalla_imagen(screen,boton2,inicio,"EXIT",Font1,1050,620,145,45,(0,0,0)):
        return(3)

def intruccion(screen,boton2):
    intruction=pygame.image.load("Instrucciones.png")
    pygame.Surface.blit(screen,intruction,(0,0))
    
    Font=pygame.font.SysFont("Comic sans",16)  
    if info.boton_en_pantalla_imagen(screen,boton2,intruction,"BACK",Font,1050,620,145,45,(0,0,0)):
        return(1)

def historia(screen,boton1):
    history=pygame.image.load("historia.png")
    pygame.Surface.blit(screen,history,(0,0))
    
    Font=pygame.font.SysFont("Comic sans",20)
    if info.boton_en_pantalla_imagen(screen,boton1,history,"NEXT",Font,890,590,312,79,(0,0,0)):
        return(1)

def victoria(screen):
    victory = pygame.image.load("pantalla de victoria.png")
    pygame.Surface.blit(screen, victory, (0,0))

def derrota(screen, boton2):
    perdiste= pygame.image.load("Perdiste.png") 
    pygame.Surface.blit(screen, perdiste, (0,0) )
    Font1=pygame.font.SysFont("Comic sans",16)  
    if info.boton_en_pantalla_imagen(screen,boton2, perdiste,"BACK",Font,1050,620,145,45,(0,0,0)):
        return(1)

#programa principal
main()
