import pygame
pygame.init()

wn = pygame.display.set_mode((555, 816))

watter = pygame.image.load('re/watter.jpg')
rührfisch = pygame.image.load('re/rührfisch.png')

angle = 0
run = True

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
  	        run = False

    arial = pygame.font.SysFont("arial", 50)
    angel_ = arial.render(str(angle), 1, (255, 0, 0))
            
    angle += 1
    if angle > 360:
        angle = 0   
    
    drehfisch = pygame.transform.rotate(rührfisch, angle)	
	
    keys = pygame.key.get_pressed()

    wn.blit(watter, (0, 0))
    wn.blit(drehfisch, (180, 500))
	
    pygame.display.update()
	
pygame.QUIT