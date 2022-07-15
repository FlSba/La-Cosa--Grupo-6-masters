
from operator import ilshift, truediv
import pygame
import random


def main():  #hace que corra el programa
    
    pygame.init()
    pygame.display.init()
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption("la cosa")

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

    listaobjetos=lista_objetos(lista)
    corriendo=True
    xy=respawn(listaobjetos)
    xyn=[xy,2]
    xy=respawn(listaobjetos)
    xyn1=[xy,0,2]
    xy=respawn(listaobjetos)
    xyn2=[xy,0,2]
    xy=respawn(listaobjetos)
    xyn3=[xy,0,2]
    reloj=pygame.time.Clock()
    Mapa=True
    n=0

    while corriendo:
        reloj.tick(60)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        if Mapa:
            screen.fill((0,0,0))
            mapa(screen,lista)
            Mapa=True
        Objetos(screen,listaobjetos)
        xyn1=monitos(screen,listaobjetos,xyn1)
        listaobjetos=recoge_pocion(xyn1,listaobjetos)
        xyn2=monitos(screen,listaobjetos,xyn2)
        listaobjetos=recoge_pocion(xyn2,listaobjetos)
        xyn3=monitos(screen,listaobjetos,xyn3)
        listaobjetos=recoge_pocion(xyn3,listaobjetos)
        xyn=monito(screen,listaobjetos,xyn,n)
        listaobjetos=recoge_pocion(xyn,listaobjetos)
        n=0
        if cuenta_pocion(listaobjetos):
            pygame.display.quit()

    pygame.display.quit()

def mapa(screen,lista): # imprime el piso y la pared del tablero
    piso=pygame.image.load("Piso.png")
    piso=pygame.transform.scale(piso,(30,30))
    pared=pygame.image.load("Pared.png")
    pared=pygame.transform.scale(pared,(30,30))
    
    x=0
    y=0

    for i in lista:
        for j in i:
            if j==0:
                pygame.Surface.blit(screen,pared,(x,y))
            if j==1:
                pygame.Surface.blit(screen,piso,(x,y))
            if j==2:
                pygame.Surface.blit(screen,piso,(x,y))
            x=x+30
        x=0
        y=y+30
def Objetos(screen,lista): #imprime los objetos en el tablero
    chatarra=pygame.image.load("Pocion.png")
    chatarra=pygame.transform.scale(chatarra,(30,24))
    obstucalo=pygame.image.load("Obstaculo.png")
    obstucalo=pygame.transform.scale(obstucalo,(30,30))
    piso=pygame.image.load("Piso.png")
    piso=pygame.transform.scale(piso,(30,30))
    
    x=0
    y=0

    for i in lista:
        for j in i:
            if j==-2:
                pygame.Surface.blit(screen,piso,(x,y))
                y+=6
                pygame.Surface.blit(screen,chatarra,(x,y))
                y-=6
            if j==-1:
                pygame.Surface.blit(screen,piso,(x,y))
                pygame.Surface.blit(screen,obstucalo,(x,y))
            x+=30
        y+=30
        x=0
    
def lista_objetos(lista):#crea una lista nueva, la cual contiene los objetos, los -1 son obstaculos y los 1 son las pociones (las pociones son chatarras)
    cuenta_obstaculo=0
    cuenta_pociones=0
    n_obstaculo=random.randrange(10,16)
    n_pociones=random.randrange(30,51)
    for i in range (len(lista)):
        for j in range (len(lista)):
            if lista[i][j]==2:
                aux=random.randrange(1,4)
                if aux==1:
                    if cuenta_pociones<n_pociones:
                        if (lista[i][j-1]==-2 or lista[i-1][j]==-2)==False:
                            cuenta_pociones+=1
                            lista[i][j]=-2
            if lista[i][j]==1:
                Obstupoti=random.randrange(-2,2)
                if Obstupoti==-2:
                    if cuenta_pociones<n_pociones:
                        if (lista[i][j-1]==-2 or lista[i-1][j]==-2)==False:
                            lista[i][j]=-2
                            cuenta_pociones+=1
                if Obstupoti==-1:
                    if cuenta_obstaculo<n_obstaculo:
                        if i>0 and j>0 and i<19 and j<19:
                            if (lista[i-1][j-1]==(-1 or 0) or lista[i-1][j]==(-1 or 0) or lista[i][j-1]==(-1 or 0) or lista[i-1][j+1]==(-1 or 0))==False:
                                cuenta_obstaculo+=1
                                lista[i][j]=-1
                
    return (lista)

def colision(lista,x,y,n):#impide el paso de los tripulantes a una pared u obstaculo. Además, no pueden salir de la ventana

   x=int((x-5)/30)
   y=int(y/30)
   if n==1:
        if y-1==-1:
            return(True)
        if lista[y-1][x]==0 or lista[y-1][x]==-1:
            return(True)
   if n==4:
        if x+1==20:
            return(True)
        if lista[y][x+1]==0 or lista[y][x+1]==-1:
            return(True)
   if n==2:
        if y+1==20:
            return(True)
        if lista[y+1][x]==0 or lista[y+1][x]==-1:
            return(True)
   if n==3:
        if x-1==-1:
            return(True)
        if lista[y][x-1]==0 or lista[y][x-1]==-1:
            return(True)
    
def monitos(screen,lista,xyn):#genera los tripulantes random(aparte del personaje principal, el que controlamos)
    monito_w=pygame.image.load("personaje w.png")
    monito_w=pygame.transform.scale(monito_w,(20,30))
    monito_s=pygame.image.load("personaje s.png")
    monito_s=pygame.transform.scale(monito_s,(20,30))
    monito_a=pygame.image.load("personaje a.png")
    monito_a=pygame.transform.scale(monito_a,(20,30))
    monito_d=pygame.image.load("personaje d.png")
    monito_d=pygame.transform.scale(monito_d,(20,30))

    xy=xyn[0]
    cuentamovimiento1=xyn[1]
    n1=xyn[2]

    x=0
    for y in xy:
        x=x+y
    x=x-y
    
    cuentamovimiento=cuentamovimiento1+1
        
    #movimiento
    if cuentamovimiento==50:
        n=random.randrange(1,5)
        if colision(lista,x,y,n):
            n=0
        if n==1:
            y=y-30
            pygame.Surface.blit(screen,monito_w,(x,y))
            return(((x,y),0,n))
        if n==4:
            x=x+30    
            pygame.Surface.blit(screen,monito_d,(x,y))
            return(((x,y),0,n))
        if n==2:
            y=y+30
            pygame.Surface.blit(screen,monito_s,(x,y))
            return(((x,y),0,n))
        if n==3:
            x=x-30
            pygame.Surface.blit(screen,monito_a,(x,y))
            return(((x,y),0,n))
        cuentamovimiento=0
    #estatica
    if n1==1:
        pygame.Surface.blit(screen,monito_w,(x,y))
        return(((x,y),cuentamovimiento,n1))
    if n1==4:    
        pygame.Surface.blit(screen,monito_d,(x,y))
        return(((x,y),cuentamovimiento,n1))
    if n1==2:
        pygame.Surface.blit(screen,monito_s,(x,y))
        return(((x,y),cuentamovimiento,n1))
    if n1==3:
        pygame.Surface.blit(screen,monito_a,(x,y))
        return(((x,y),cuentamovimiento,n1))


def monito(screen,lista,xyn,n):#genera el personaje principal, el que movemos
    monito_w=pygame.image.load("Principal w.png")
    monito_w=pygame.transform.scale(monito_w,(20,30))
    monito_s=pygame.image.load("Principal s.png")
    monito_s=pygame.transform.scale(monito_s,(20,30))
    monito_a=pygame.image.load("Principal a.png")
    monito_a=pygame.transform.scale(monito_a,(20,30))
    monito_d=pygame.image.load("Principal d.png")
    monito_d=pygame.transform.scale(monito_d,(20,30))

    xy=0
    inutil=0
    for n1 in xyn:
        xy=inutil
        inutil=n1
    
    x=0
    for y in xy:
        x=x+y
    x=x-y

    if colision(lista,x,y,n):
        n=0
    #Movimiento personaje con teclas
    if n==1:
        y=y-30
        pygame.Surface.blit(screen,monito_w,(x,y))
        return(((x,y),n))
    if n==4:
        x=x+30    
        pygame.Surface.blit(screen,monito_d,(x,y))
        return(((x,y),n))
    if n==2:
        y=y+30
        pygame.Surface.blit(screen,monito_s,(x,y))
        return(((x,y),n))
    if n==3:
        x=x-30
        pygame.Surface.blit(screen,monito_a,(x,y))
        return(((x,y),n))
    #Estatica de personaje
    if n1==1:
        pygame.Surface.blit(screen,monito_w,(x,y))
        return(((x,y),n1))
    if n1==4:  
        pygame.Surface.blit(screen,monito_d,(x,y))
        return(((x,y),n1))
    if n1==2:
        pygame.Surface.blit(screen,monito_s,(x,y))
        return(((x,y),n1))
    if n1==3:
        pygame.Surface.blit(screen,monito_a,(x,y))
        return(((x,y),n1))
def respawn(Listaobjetos):#hace que los personajes aparezcan en el tablero de manera aleatoria
    while True:
        x=0
        y=0
        x1=random.randrange(0,21)
        y1=random.randrange(0,21)
        for i in Listaobjetos:
            for j in i:
                if j==2 and x==x1 and y==y1:
                    return (((x*30)+5,y*30))
                x+=1
            y+=1
            x=0
def recoge_pocion(xyn,lista):
    xy=xyn[0]
    x=0
    for y in xy:
        x=x+y
    x=x-y
    x=int((x-5)/30)
    y=int(y/30)
    if lista[y][x]==-2:
        lista[y][x]=2
    return (lista)
def cuenta_pocion(lista):
    cuentapoti=0
    for i in lista:
        for j in i:
            if j==-2:
                cuentapoti+=1
    if cuentapoti==0:
        return (True)
    return (False)

def boton_en_pantalla(screen,palabra,letra,x,y,largo,alto,color):#screen=pantalla o ventana, palabra es "palabra", letra es font,x es distancia en eje x que dibujó el rectangulo, y es lo mismo pero en eje y,color es el color a cambiar el boton
#alto es el alto del rectangulo, el largo es el largo del rectangulo
    Palabra_en_pantalla=letra.render(palabra,True,(255,255,255))
    espacio=pygame.draw.rect(screen,(0,0,0),(x,y,largo,alto))
    if pygame.Rect.collidepoint(espacio,pygame.mouse.get_pos()):
        pygame.draw.rect(screen,color,(x,y,largo,alto))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pygame.draw.rect(screen,(0,0,0),(x,y,largo,alto))
            if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                return True
    pygame.Surface.blit(screen,Palabra_en_pantalla,(x+(largo-pygame.Surface.get_width(Palabra_en_pantalla))/2,y+(alto-pygame.Surface.get_height(Palabra_en_pantalla))/2))
    return()

def boton_en_pantalla_imagen(screen,imagen,imagen_de_fondo,palabra,letra,x,y,ancho,alto,color):
#screen es el lugar donde se dibuja, imagen es la imagen,imagen_de_fondo es la imagen del fondo, palabra es la "palabra" que va dentro del boton, letra es el estilo de letra, x es la distancia en x desde donde se dibuja
#y es la distancia en y desde donde se dibuja, ancho es el ancho de la foto, alto es el alto de la foto, color es el color de las letras
    Texto=letra.render(palabra,True,color)
    imagen=pygame.transform.scale(imagen,(ancho,alto))
    imagen_en_pantalla=pygame.Surface.blit(screen,imagen,(x,y))
    pygame.Surface.blit(screen,Texto,(x+(ancho-pygame.Surface.get_width(Texto))/2,y+(alto-pygame.Surface.get_height(Texto))/2))

    if pygame.Rect.collidepoint(imagen_en_pantalla,pygame.mouse.get_pos()):
        pygame.Surface.blit(screen,pygame.transform.scale(imagen,(ancho+28,alto+14)),(x-14,y-7))
        pygame.Surface.blit(screen,pygame.transform.scale(Texto,(pygame.Surface.get_width(Texto)+26,pygame.Surface.get_height(Texto)+12)),(x+(ancho-(pygame.Surface.get_width(Texto)+24))/2,y+(alto-(pygame.Surface.get_height(Texto)+12))/2))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pygame.Surface.blit(screen,imagen_de_fondo,(0,0))
                pygame.Surface.blit(screen,imagen,(x,y))
                pygame.Surface.blit(screen,Texto,(x+(ancho-pygame.Surface.get_width(Texto))/2,y+(alto-pygame.Surface.get_height(Texto))/2))
            if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                return(True)
