import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 50
TREASURE_COLOR = (255, 215, 0)
OBSTACLE_COLOR = (255, 0, 0)
PLAYER_COLOR = (0, 0, 255)
LOCKED_COLOR = (128, 128, 128)
WALL_COLOR = (100, 100, 100)
DOOR_COLOR = (255, 165, 0)
WIZARD_COLOR = (128, 0, 128)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the player
player_x = 0
player_y = 0
player_health = 100
player_max_health = 100
player_health_regeneration = 0

# Set up the level
level = 1

# Set up the cells, obstacles, keys, walls, and doors
cells = []
obstacles = []
keys = []
walls = []
doors = []
current_key_count = 0
current_cell_index = 0
wizard_x = 0
wizard_y = 0
wizard_speed = 1
wizard_disabled = False
wizard_disabled_time = 0

# Function to generate a new level
def generate_level(level):
    global cells, obstacles, keys, walls, doors, current_key_count, current_cell_index, wizard_x, wizard_y, wizard_speed
    cells = []
    obstacles = []
    keys = []
    walls = []
    doors = []
    current_key_count = 0
    current_cell_index = 0
    wizard_speed = level
    cell_count = level * 5
    for i in range(cell_count):
        x = random.randint(0, WIDTH // CELL_SIZE - 1)
        y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        while (
            (x, y) in [(cell[0], cell[1]) for cell in cells]
            or (x, y) in obstacles
            or (x, y) in keys
            or (x, y) in walls
            or (x, y) in doors
        ):
            x = random.randint(0, WIDTH // CELL_SIZE - 1)
            y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        cells.append((x, y, i + 1))  # Assign a unique number to each cell
    for _ in range(level * 10):
        x = random.randint(0, WIDTH // CELL_SIZE - 1)
        y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        while (
            (x, y) in [(cell[0], cell[1]) for cell in cells]
            or (x, y) in obstacles
            or (x, y) in keys
            or (x, y) in walls
            or (x, y) in doors
        ):
            x = random.randint(0, WIDTH // CELL_SIZE - 1)
            y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        obstacles.append((x, y))
    for _ in range(level * 5):
        x = random.randint(0, WIDTH // CELL_SIZE - 1)
        y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        while (
            (x, y) in [(cell[0], cell[1]) for cell in cells]
            or (x, y) in obstacles
            or (x, y) in keys
            or (x, y) in walls
            or (x, y) in doors
        ):
            x = random.randint(0, WIDTH // CELL_SIZE - 1)
            y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        keys.append((x, y))
    for _ in range(level * 20):
        x = random.randint(0, WIDTH // CELL_SIZE - 1)
        y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        while (
            (x, y) in [(cell[0], cell[1]) for cell in cells]
            or (x, y) in obstacles
            or (x, y) in keys
            or (x, y) in walls
            or (x, y) in doors
        ):
            x = random.randint(0, WIDTH // CELL_SIZE - 1)
            y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        if random.random() < 0.2:  # 20% chance to be a wall
            walls.append((x, y))
        elif random.random() < 0.1:  # 10% chance to be a door
            doors.append((x, y))

    # Make sure wizard spawns on opposite side of the box from player
    if player_x < WIDTH // CELL_SIZE // 2:
        wizard_x = random.randint(WIDTH // CELL_SIZE // 2, WIDTH // CELL_SIZE - 1)
        wizard_y = random.randint(HEIGHT // CELL_SIZE // 2, HEIGHT // CELL_SIZE - 1)
    else:
        wizard_x = random.randint(0, WIDTH // CELL_SIZE // 2 - 1)
        wizard_y = random.randint(0, HEIGHT // CELL_SIZE // 2 - 1)
    while (
        (wizard_x, wizard_y) in [(cell[0], cell[1]) for cell in cells]
        or (wizard_x, wizard_y) in obstacles
        or (wizard_x, wizard_y) in keys
        or (wizard_x, wizard_y) in walls
        or (wizard_x, wizard_y) in doors
    ):
        if player_x < WIDTH // CELL_SIZE // 2:
            wizard_x = random.randint(WIDTH // CELL_SIZE // 2, WIDTH // CELL_SIZE - 1)
            wizard_y = random.randint(HEIGHT // CELL_SIZE // 2, HEIGHT // CELL_SIZE - 1)
        else:
            wizard_x = random.randint(0, WIDTH // CELL_SIZE // 2 - 1)
            wizard_y = random.randint(0, HEIGHT // CELL_SIZE // 2 - 1)


# Generate the first level
generate_level(level)

def game_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Game Menu", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))
    text = font.render("1. Continue Game", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))
    text = font.render("2. Quit Game", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 90))
    text = font.render("3. Restart Game", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 130))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return
                elif event.key == pygame.K_2:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_3:
                    player_x = 0
                    player_y = 0
                    player_health = 100
                    player_max_health = 100
                    player_health_regeneration = 0
                    level = 1
                    cells = []
                    obstacles = []
                    keys = []
                    walls = []
                    doors = []
                    current_key_count = 0
                    current_cell_index = 0
                    wizard_x = 0
                    wizard_y = 0
                    wizard_speed = 1
                    wizard_disabled = False
                    wizard_disabled_time = 0
                    generate_level(level)
                    return

def pause_game():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Game Paused", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))
    text = font.render("Press 'p' to continue", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))
    pygame.display.flip()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            new_x, new_y = player_x, player_y
            if event.key == pygame.K_UP:
                new_y -= 1
            elif event.key == pygame.K_DOWN:
                new_y += 1
            elif event.key == pygame.K_LEFT:
                new_x -= 1
            elif event.key == pygame.K_RIGHT:
                new_x += 1
            elif event.key == pygame.K_p:
                pause_game()
            elif event.key == pygame.K_m:
                game_menu()

            # Wrap around edges
            if new_x < 0:
                new_x = WIDTH // CELL_SIZE - 1
            elif new_x >= WIDTH // CELL_SIZE:
                new_x = 0
            if new_y < 0:
                new_y = HEIGHT // CELL_SIZE - 1
            elif new_y >= HEIGHT // CELL_SIZE:
                new_y = 0

            if (new_x, new_y) not in walls:
                if (new_x, new_y) in doors:
                    if current_key_count > 0:
                        current_key_count -= 1
                        doors.remove((new_x, new_y))
                        player_x, player_y = new_x, new_y
                        wizard_disabled = True
                        wizard_disabled_time = pygame.time.get_ticks()
                    else:
                        print("You don't have a key to unlock this door!")
                else:
                    player_x, player_y = new_x, new_y

    # Move the wizard
    if not wizard_disabled:
        if wizard_x < player_x:
            wizard_x = min(wizard_x + 0.01 + level * 0.005, player_x)
        elif wizard_x > player_x:
            wizard_x = max(wizard_x - 0.01 - level * 0.005, player_x)
        if wizard_y < player_y:
            wizard_y = min(wizard_y + 0.01 + level * 0.005, player_y)
        elif wizard_y > player_y:
            wizard_y = max(wizard_y - 0.01 - level * 0.005, player_y)

        # Wrap around edges for the wizard
        if wizard_x < 0:
            wizard_x = WIDTH // CELL_SIZE - 1
        elif wizard_x >= WIDTH // CELL_SIZE:
            wizard_x = 0
        if wizard_y < 0:
            wizard_y = HEIGHT // CELL_SIZE - 1
        elif wizard_y >= HEIGHT // CELL_SIZE:
            wizard_y = 0
    else:
        if pygame.time.get_ticks() - wizard_disabled_time > 2500:
            wizard_disabled = False

    # Check for cells
    for cell in cells:
        if (player_x, player_y) == (cell[0], cell[1]):
            if (
                cell[2] == current_cell_index + 1
            ):  # Check if the cell is the next one in sequence
                print(f"You collected cell {cell[2]}!")
                cells.remove(cell)
                current_cell_index += 1
                player_health += 20
                if len(cells) == 0:
                    level += 1
                    generate_level(level)
                    player_x = 0
                    player_y = 0
            else:
                print("You must collect the cells in order!")
                player_health -= 20

    # Check for obstacles
    if (player_x, player_y) in obstacles:
        print("You hit an obstacle!")
        obstacles.remove((player_x, player_y))
        player_health -= 20

    # Check for keys
    if (player_x, player_y) in [key[:2] for key in keys]:
        key_index = [key[:2] for key in keys].index((player_x, player_y))
        print("You found a key!")
        keys.pop(key_index)
        current_key_count += 1

    # Check for wizard
    if (player_x, player_y) == (wizard_x, wizard_y):
        print("The wizard caught you! Game over.")
        pygame.quit()
        quit()

    # Regenerate health
    if player_health < player_max_health:
        player_health += player_health_regeneration

    # Check for game over
    if player_health <= 0:
        print("Game over! You died.")
        pygame.quit()
        quit()


    # Draw everything
    screen.fill((0, 0, 0))
    for cell in cells:
        pygame.draw.rect(
            screen,
            TREASURE_COLOR,
            (cell[0] * CELL_SIZE, cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )
        text = font.render(str(cell[2]), True, (255, 255, 255))
        screen.blit(
            text,
            (
                cell[0] * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2,
                cell[1] * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2,
            ),
        )
    for obstacle in obstacles:
        pygame.draw.rect(
            screen,
            OBSTACLE_COLOR,
            (obstacle[0] * CELL_SIZE, obstacle[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )
    for key in keys:
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (key[0] * CELL_SIZE, key[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )
    for wall in walls:
        pygame.draw.rect(
            screen,
            WALL_COLOR,
            (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )
    for door in doors:
        pygame.draw.rect(
            screen,
            DOOR_COLOR,
            (door[0] * CELL_SIZE, door[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )
    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    )
    text = font.render(str(current_cell_index + 1), True, (255, 255, 255))
    screen.blit(
        text,
        (
            player_x * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2,
            player_y * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2,
        ),
    )
    if not wizard_disabled:
        pygame.draw.rect(
            screen,
            WIZARD_COLOR,
            (int(wizard_x) * CELL_SIZE, int(wizard_y) * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )
    text = font.render("Health: " + str(player_health), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    text = font.render("Keys: " + str(current_key_count), True, (255, 255, 255))
    screen.blit(text, (10, 40))
    text = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(text, (10, 70))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

y = np.array([[12,34], [98, 23]])