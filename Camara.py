# sudo pip3 install pygame

import pygame.camera
import pygame.image
import sys
import os

class Camara:

    def exit(self):
        self.close()
        sys.exit()

    def close(self):
        self.webcam.stop()

    def initConstants(self):
        self.ENTER = 13
        self.SPACE = 32
        self.MOUSE_BUTTON_1 = 1



    def __init__(self):
        self.initConstants()
        self.photoPath = "/home/pi/"

        # Centrado
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.camera.init()

        self.cameras = pygame.camera.list_cameras()
        self.webcam = pygame.camera.Camera(self.cameras[0])

        self.pasos = list()

        self.pasos.append("CARNET_FRONT")
        self.pasos.append("CARNET_BACK")
        self.pasos.append("LICENCIA_FRONT")
        self.pasos.append("LICENCIA_BACK")
        self.pasos.append("SELFIE")

        self.i = 0

        self.white = (255, 255, 255)
        self.black = (0,0,0)

        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

    def takePhoto(self):
        paso = self.pasos[self.i]
        self.i += 1

        try:
            pygame.image.save(self.img, self.photoPath+str(self.i)+"_"+paso+".png")
        except Exception:
            pygame.image.save(self.img, str(self.i)+"_"+paso+".png")
        
        if self.i == 5:
            self.exit()

    def open(self):
        self.webcam.start()
        
        # grab first frame
        self.img = self.webcam.get_image()

        self.WIDTH = self.img.get_width()
        self.HEIGHT = self.img.get_height()

        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        
        pygame.display.set_caption("Awto Camera")

        pygame.font.init()

        try:
            while True :
                for e in pygame.event.get() :
                    if e.type == pygame.QUIT :
                        self.exit()
                    
                    if e.type == pygame.KEYDOWN:
                        # si es enter o espacio
                        if e.key == self.ENTER or e.key == self.SPACE:
                            self.takePhoto()

                    if e.type == pygame.MOUSEBUTTONUP and e.button == self.MOUSE_BUTTON_1:
                        self.takePhoto()

                # draw frame
                self.screen.blit(self.img, (0,0))
                # Texto
                texto = self.myfont.render(self.pasos[self.i], False, self.white)

                #screen.blit(rectangle, (0,0))
                self.screen.blit(texto,(0,0))
                
                pygame.display.flip()
                # grab next frame    
                self.img = self.webcam.get_image()
        except SystemExit:
            pygame.quit()