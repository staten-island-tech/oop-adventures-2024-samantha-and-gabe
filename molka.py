import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (player_x, player_y)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += player_speed
        if keys[pygame.K_UP]:
            self.rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += player_speed

# Create player instance
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()

    # Update all sprites
    all_sprites.update(keys)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
class Room:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class Dungeon:
    def __init__(self):
        self.rooms = []

    def generate_rooms(self):
        for _ in range(5):  # Generate 5 rooms
            width = random.randint(100, 200)
            height = random.randint(100, 200)
            x = random.randint(0, SCREEN_WIDTH - width)
            y = random.randint(0, SCREEN_HEIGHT - height)
            room = Room(x, y, width, height)
            self.rooms.append(room)

    def draw(self, screen):
        for room in self.rooms:
            room.draw(screen)

# Create a dungeon and generate rooms
dungeon = Dungeon()
dungeon.generate_rooms()

# Main game loop (updated to show rooms)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    screen.fill(BLACK)

    # Draw dungeon rooms
    dungeon.draw(screen)

    # Draw player
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 100

    def update(self):
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center

    def update(self, player):
        self.rect.center = player.rect.center
        # Here, add logic for the weapon to deal damage if colliding with enemies.

# Create enemy and weapon instance
enemy = Enemy(random.randint(100, 700), random.randint(100, 500))
weapon = Weapon(player)

all_sprites.add(enemy)
all_sprites.add(weapon)

# Example of combat logic (simplified)
def combat_logic():
    if player.rect.colliderect(enemy.rect):  # If the player collides with the enemy
        enemy.take_damage(10)  # Attack the enemy (deal 10 damage)

# Main game loop (updated to include combat)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    combat_logic()

    screen.fill(BLACK)

    dungeon.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
def draw_ui():
    font = pygame.font.SysFont('Arial', 24)
    health_text = font.render(f"Health: {player.health}", True, (255, 255, 255))
    screen.blit(health_text, (10, 10))

# Main game loop (with UI)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    combat_logic()

    screen.fill(BLACK)

    dungeon.draw(screen)
    all_sprites.draw(screen)
    draw_ui()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
