import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'draw'  # Initial mode
    color = (0, 0, 255)  # Initial color (blue)
    drawing = False
    start_pos = None
    points = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    color = (255, 0, 0)  # Red
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  # Green
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  # Blue
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_s:
                    mode = 'rectangle'
                elif event.key == pygame.K_c:
                    mode = 'circle'

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    drawing = True
                    start_pos = event.pos
                    if mode == 'erase':
                        pygame.draw.circle(screen, (255, 255, 255), event.pos, radius)  # Erase part

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    if mode == 'rectangle':
                        end_pos = event.pos
                        rect_width = end_pos[0] - start_pos[0]
                        rect_height = end_pos[1] - start_pos[1]
                        pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], rect_width, rect_height), 3)
                    elif mode == 'circle':
                        end_pos = event.pos
                        circle_radius = int(((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2) ** 0.5)
                        pygame.draw.circle(screen, color, start_pos, circle_radius, 3)

            elif event.type == pygame.MOUSEMOTION and drawing:
                if mode == 'draw':
                    pygame.draw.circle(screen, color, event.pos, radius)
                elif mode == 'erase':
                    pygame.draw.circle(screen, (255, 255, 255), event.pos, radius)  # Erase part

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()