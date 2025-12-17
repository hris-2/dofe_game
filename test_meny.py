import pygame, sys, random

pygame.init()

W, H = 1260, 720
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("TEST")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 30)

characters = ["Character 1", "Character 2", "Character 3", "Character 4"]
maps = ["Map 1", "Map 2", "Map 3", "Map 4"]

state = "title"
character_index_1 = len(characters) // 2
character_index_2 = len(characters) // 2
map_index_1 = len(maps) // 2
map_index_2 = len(maps) // 2

final_decided = False
map_index = 0

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if state == "title":
                state = "character
            elif state == "character":
                if event.key == pygame.K_a:
                    character_index_1 = (character_index_1 - 1) % len(characters)
                elif event.key == pygame.K_d:
                    character_index_1 = (character_index_1 + 1) % len(characters)
                if event.key == pygame.K_LEFT:
                    character_index_2 = (character_index_2 - 1) % len(characters)
                elif event.key == pygame.K_RIGHT:
                    character_index_2 = (character_index_2 + 1) % len(characters)
                if event.key == pygame.K_RETURN:
                    state = "map"
            elif state == "map":
                if event.key == pygame.K_a:
                    map_index_1 = (map_index_1 - 1) % len(maps)
                elif event.key == pygame.K_d:
                    map_index_1 = (map_index_1 + 1) % len(maps)
                if event.key == pygame.K_LEFT:
                    map_index_2 = (map_index_2 - 1) % len(maps)
                elif event.key == pygame.K_RIGHT:
                    map_index_2 = (map_index_2 + 1) % len(maps)
                if event.key == pygame.K_RETURN:
                    if map_index_1 != map_index_2:
                        map_index = random.choice([map_index_1, map_index_2])
                    else:
                        map_index = map_index_1
                    state = "complete"
            elif state == "complete":
                if not final_decided:
                    print(
                        f"PLAYING {characters[character_index_1]} "
                        f"AGAINST {characters[character_index_2]} "
                        f"ON {maps[map_index]}"
                    )
                    final_decided = True
 state == "title":
        title = font.render("TITLE", True, BLACK)
        subtitle = small_font.render("PRESS ANY KEY TO START", True, BLACK)
        screen.blit(title, ((W - title.get_width()) // 2, H // 3))
        screen.blit(subtitle, ((W - subtitle.get_width()) // 2, H // 2))
    elif state == "character":
        info = small_font.render("Select Characters", True, BLACK)
        p1 = font.render(characters[character_index_1], True, BLUE)
        p2 = font.render(characters[character_index_2], True, RED)
        screen.blit(info, ((W - info.get_width()) // 2, H // 6))
        screen.blit(p1, (W // 4 - p1.get_width() // 2, H // 2))
        screen.blit(p2, (3 * W // 4 - p2.get_width() // 2, H // 2))
    elif state == "map":
        info = small_font.render("Select Map", True, BLACK)
        m1 = font.render(maps[map_index_1], True, BLUE)
        m2 = font.render(maps[map_index_2], True, RED)
        screen.blit(info, ((W - info.get_width()) // 2, H // 6))
        screen.blit(m1, (W // 4 - m1.get_width() // 2, H // 2))
        screen.blit(m2, (3 * W // 4 - m2.get_width() // 2, H // 2))
    pygame.display.flip()
    clock.tick(60)