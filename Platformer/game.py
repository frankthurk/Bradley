import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bradley's Platformer")

levels = [
    {
        "platforms": [
            (450, 470, 125, 50),
            (10, 470, 50, 10),
            (10, 410, 40, 10),
            (10, 350, 30, 10),
            (10, 290, 20, 10),
            (10, 230, 10, 10),
            (220, 340, 100, 15),
            (400, 220, 200, 30),
        ],
        "spawn": (485, 390),
        "goal": (50, 180, 30, 40)
    }
    {
        "platforms": [
            (200, 500, 400, 15)
            (0, )
        ]
    }
]
on_ground = False
x, y = levels[current_level]["spawn"]
y_velocity = 0
gravity = 0.5
input_lockout = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if on_ground:
                    y_velocity = -12
                    on_ground = False
    on_ground = False
    platforms = levels[current_level]["platforms"]
    spawn_x, spawn_y = levels[current_level]["spawn"]
    goal_x, goal_y, goal_width, goal_height = levels[current_level]["goal"]
    keys = pygame.key.get_pressed()
    if input_lockout > 0:
        input_lockout -= 1
    else:
        if keys[pygame.K_LEFT]:
            x -= 4
        if keys[pygame.K_RIGHT]:
            x += 4
    if x < 0:
        x = 0
    if x > 750:
        x = 750
    for platform in platforms:
        px, py, pw, ph = platform
        if x + 50 > px and x < px + pw and y < py + ph and y + 50 > py:
            if keys[pygame.K_RIGHT]:
                x = px - 50
            elif keys[pygame.K_LEFT]:
                x = px + pw
    y_velocity += gravity
    y += y_velocity
    if y < 0:
        y = 0
        y_velocity = 0
    for platform in platforms:
        px, py, pw, ph = platform
        if x + 50 > px and x < px + pw and y < py + ph and y + 50 > py:
            if y_velocity > 0:
                y = py - 50
                y_velocity = 0
                on_ground = True
            else:
                y = py + ph
                y_velocity = 0
    if y >= 1000:
        x = spawn_x
        y = spawn_y
        y_velocity = 0
    if x + 50 > goal_x and x < goal_x + goal_width and y < goal_y + goal_height and y + 50 > goal_y:
        x = spawn_x
        y = spawn_y
        y_velocity = 0
        input_lockout = 30
    screen.fill((30, 30, 40))
    for platform in platforms:
        pygame.draw.rect(screen, (50, 200, 50), platform)
    pygame.draw.rect(screen, (255, 223, 0), (goal_x,goal_y,goal_width,goal_height))
    pygame.draw.rect(screen, (200, 50, 50), (x,y,50,50))
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())
pygame.quit()