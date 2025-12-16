import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
#from circleshape import CircleShape
from player import Player
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Make groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable) 

    # Initiate player
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        log_state()
        # Check if user hit the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # initiate black game screen
        screen.fill('black')
        # Draw player
        for p in drawable:
            p.draw(screen)
        # Update player
        for p in updatable:
            p.update(dt)   
        # Flip display
        pygame.display.flip()
        
        delta_time = clock.tick(60)
        dt = delta_time / 1000
        


if __name__ == "__main__":
    main()
