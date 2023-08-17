from src.constantes import *
from src.classes.world import World 

pygame.init()
pygame.display.set_caption('diep.io')

SCREEN.fill(BLACK())

if ON_FULLSCREEN:
    pygame.display.toggle_fullscreen()
    
clock = pygame.time.Clock()

# -----+----- #

world = World()
my_tik = 0

# -----+----- #

while RUN:
    clock.tick(FPS)
    SCREEN.fill(WHITE(10))
    
    pygame.display.set_caption(f'diep.io    fps: {str(int(clock.get_fps()))}')

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            RUN = False

        if event.type == pygame.MOUSEWHEEL:
            world.scale_world(event.y/10)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f :
                SIZE_SCREEN = [1366, 768]
                SCREEN = pygame.display.set_mode(SIZE_SCREEN)
                
                pygame.display.toggle_fullscreen()
            pass
        
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        RUN = False

    if keys[pygame.K_t] :
        world.players[0].shot()

    if keys[pygame.K_w]:
        world.cam_pos[1] += 20

    if keys[pygame.K_s]:
        world.cam_pos[1] -= 20

    if keys[pygame.K_a]:
        world.cam_pos[0] += 20

    if keys[pygame.K_d]:
        world.cam_pos[0] -= 20

    if keys[pygame.K_LEFT]:
        world.players[0].player_move(-9, 0)

    if keys[pygame.K_RIGHT]:
        world.players[0].player_move(9, 0)

    if keys[pygame.K_SPACE]:
        world.players[0].player_move(0, 10)

    if RUN == True: 
        world.draw_screen()
        world.world_update(my_tik)
        pygame.display.update()
        my_tik += 1