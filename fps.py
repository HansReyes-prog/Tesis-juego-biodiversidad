import pygame

# Inicializar pygame
pygame.init()

# Crear la ventana del juego y fuente
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36)

# Crear el reloj
clock = pygame.time.Clock()

# Función para actualizar y mostrar FPS
def update_fps():
    fps = str(int(clock.get_fps()))
    text = font.render(fps, True, pygame.Color("coral"))
    return text

# Bucle principal
loop = True
while loop:
    screen.fill((0, 0, 0))  # Limpiar la pantalla
    screen.blit(update_fps(), (10, 0))  # Mostrar FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    clock.tick(60)  # Limitar FPS a 60
    pygame.display.update()  # Actualizar pantalla

pygame.quit()  # Salir del juego
