import pygame

# general
screen_width = 1920
screen_height = 1080
fps = 60
game_title = "Kitten Adventure"

# colors
bg_color = (200, 240, 255)
kitty_color = (255, 192, 203)
fish_color = (200, 200, 200)
black = (0, 0, 0)
lightRed = (255, 80, 100)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 204, 0)
lightblue = (102, 204, 255)
pink = (255, 204, 255)

# upgrade system
upgrade_limits = {
    "speed": 10,
    "fish_spawn_rate": 5,
    "fish_value": 5,
    "magnet": 2,
}

upgrade_costs = {
    "speed": [5, 10, 20, 40, 60, 100, 150, 200, 250, 300],
    "fish_spawn_rate": [5, 20, 50, 100, 200],
    "fish_value": [10, 40, 80, 120, 200],
    "magnet": [50, 300],
}

# sprite sizes
normal_size = (40, 40)
vertical_size = (35, 35)

# movement / combat
kitten_speed_default = 3.5
enemy_speed = 3
stun_duration = 2000
dash_duration = 0.3
dash_cooldown = 2.0
bounce_duration = 0.15
bounce_strength = 1200

# camera / hit fx
shake_magnitude = 10
hit_effect_alpha = 100

# fonts
pygame.font.init()
font = pygame.font.SysFont("comicsans", 30)