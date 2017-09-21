import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *
from random import *

SCREEN_WIDTH = 680
SCREEN_HEIGHT = 640
ICON_SIZE = 32

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Campo minado" )
    background_image = util.cargar_imagen('imagenes/Fondo-desertico.png');
    pierde_vida = util.cargar_sonido('sonidos/Kbom.mp3')
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    heroe = Heroe()
    villano = [Villano((100,-10),randint(1,3)),
               Villano((150,-50),randint(1,3)),
               Villano((200,-500),randint(1,3)),
               Villano((250,-300),randint(1,3)),
               Villano((300,-35),randint(1,3)),
               Villano((350,-333),randint(1,3)),
               Villano((400,-536),randint(1,3)),
               Villano((450,-133),randint(1,3)),
               Villano((500,-231),randint(1,3)),
               Villano((550,-3),randint(1,3)),
               Villano((600,-325),randint(1,3)),
               Villano((650,-832),randint(1,3)),
               Villano((225,-400),randint(1,3)),
               Villano((650,-148),randint(1,3)),
               Villano((250,-113),randint(1,3)),
               Villano((400,-251),randint(1,3)),
               Villano((500,-152),randint(1,3)),
               Villano((300,-254),randint(1,3)),
               Villano((200,-1),randint(1,3)),
               Villano((450,-235),randint(1,3))]
    
    while True:
        fuente = pygame.font.Font(None,30)
        (""")texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(0,0,0))(""")
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(0,0,0))
        
        heroe.update()
        for n in villano:
            n.update()
        
        for n in villano:
            if heroe.rect.colliderect(n.rect):
                heroe.image = heroe.imagenes[1]
                pierde_vida.play() 	
                if heroe.vida > 0:
                    heroe.vida=heroe.vida-1
                n.velocidad=randint(1,10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(400,620))
        (""")screen.blit(texto_puntos,(100,620))(""")
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)

      
if __name__ == '__main__':
      game()

