import pygame
import time
pygame.init()
purple = (220,150,220)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

disp_width = 800
disp_height = 600

gamedisp = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption('Slither')

#pygame.display.update() #to give appearance of things moving by keeping the updated picture everytime on surface

clock = pygame.time.Clock()
FPS = 30
block_size = 10

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gamedisp.blit(screen_text, [disp_width/2,disp_height/2])
    
def gameloop():
    gameexit = False
    gameover = False
    lead_x=disp_width/2
    lead_y=disp_height/2
    lead_x_change = 0
    lead_y_change = 0

    while not gameexit:
        while gameover == True:
            gamedisp.fill(white)
            message_to_screen("Game Over, Press C to continue",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
                    if event.key == pygame.K_c:
                        gameloop()
            
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
        if lead_x>=disp_width or lead_x<0 or lead_y >=disp_height or lead_y<0:
            gameover = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gamedisp.fill(purple)
        pygame.draw.rect(gamedisp, black, [lead_x,lead_y,block_size,block_size]) #x,y,w,h
        pygame.display.update()
        clock.tick(FPS) #frame per second
    pygame.quit()
    quit()

gameloop()

