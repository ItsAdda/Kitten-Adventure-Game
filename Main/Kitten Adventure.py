# === IMPORTS & INITIAL SETUP ===
import random
import sys
import pygame
import pygame.mixer
import json
import os
import random
import math

from config import *

global enemy

pygame.init()
pygame.mixer.init()

bg_color_time = 0

# === SCREEN SETUP ===
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_title)


# === SOUNDS ===
backgroundMusic = pygame.mixer.Sound("Sounds/game-music-loop-9-145494 (mp3cut.net).mp3")
backgroundMusic.play(loops=-1)
buttonClick = pygame.mixer.Sound("Sounds/video-game-menu-click-sounds-148373 (1) (mp3cut.net).mp3")
fishCollection = pygame.mixer.Sound("Sounds/retro-coin-3-236679.mp3")
enemyHit = pygame.mixer.Sound("Sounds/stunned_04-99823.mp3")
DashSound = pygame.mixer.Sound("Sounds/retro-jump-3-236683.mp3")
enemyKill = pygame.mixer.Sound("Sounds/explosion-9-340460.mp3")
enemyDamage = pygame.mixer.Sound("Sounds/fist-fight-192117 (mp3cut.net).mp3")
backgroundMusic.set_volume(0.5)
enemyHit.set_volume(0.5)

# === LOAD IMAGES ===
fish_image = pygame.image.load("Sprites/Anchovy.png").convert_alpha()
fish_image = pygame.transform.scale(fish_image, (40, 40))
jellyfishDrop_image = pygame.image.load("Sprites/Goldfish.png").convert_alpha()
jellyfishDrop_image = pygame.transform.scale(jellyfishDrop_image, (40, 40))
heart_img = pygame.image.load("Sprites/heart.png").convert_alpha()
heart_img = pygame.transform.smoothscale(heart_img, (200, 200))
nightFish_image = pygame.image.load("Sprites/Surgeonfish Outline.png").convert_alpha()
nightFish_image = pygame.transform.scale(nightFish_image, (40, 40))



clock = pygame.time.Clock()
day_phase = "day"
day_cycle_time = 0

# === COLORS ===
from config import *

# === UPGRADE SYSTEM VARIABLES ===
upgradeCountSpeed = 0
upgradeCountFishSpawnRate = 0
upgradeCountFishValue = 0
upgradeCountMagnet = 0
upgradeLimitFish = 10
upgradeLimitFishSpawnRate = 5
upgradeLimitFishValue = 5
upgradeLimitMagnet = 2
upgradeUp_speed = [5, 10, 20, 40, 60, 100, 150, 200, 250, 300]
upgradeUp_fasterSpawnRateFish = [5, 20, 50, 100, 200]
upgradeUp_fishvalue = [10, 40, 80, 120, 200]
upgradeUp_magnet = [50, 300]


# === FONT & SPRITE SIZE ===
font = pygame.font.SysFont('comicsans', 30)
title_font = pygame.font.Font("Fonts/coolfont.ttf", 120)
normal_size = (60, 60)
vertical_size = (48, 48)


# === MOVEMENT & ANIMATION CONTROL ===
bouncing = False
bounce_dx = 0
bounce_dy = 0
bounce_timer = 0
bounce_duration = 0.15
bounce_strength = 1200
idle_finished = False
current_direction = "down"
current_frame = 0
idle_animation_speed = 0.05
run_animation_speed = 0.10
frame_timer = 0
moving = False

# === LOAD ANIMATION FRAMES ===
kittenFramesRunning = {
    "up": ["sprite12 (4).png", "sprite12 (5).png", "sprite12 (6).png", "sprite12 (7).png", "sprite12 (8).png"],
    "down": ["black_21.png", "black_22.png", "black_23.png", "black_24.png", "black_25.png"],
    "left": ["sprite6.png", "sprite7.png", "sprite8.png", "sprite9.png", "sprite10.png"],
    "right": ["sprite12 (14).png", "sprite12 (15).png", "sprite12 (16).png", "sprite12 (17).png", "sprite12 (18).png"],
    "up_left": ["sprite11.png", "sprite12.png", "sprite12 (1).png", "sprite12 (2).png", "sprite12 (3).png"],
    "up_right": ["sprite12 (9).png", "sprite12 (10).png", "sprite12 (11).png", "sprite12 (12).png", "sprite12 (13).png"],
    "down_left": ["sprite1.png", "sprite2.png", "sprite3.png", "sprite4.png", "sprite5.png"],
    "down_right": ["sprite12 (19).png", "sprite12 (20).png", "sprite12 (21).png", "sprite12 (22).png", "sprite12 (23).png"]
}
kittenFramesStill = {
    "up": ["sprite (25).png", "sprite (26).png", "sprite (27).png", "sprite (28).png", "sprite (29).png", "sprite (30).png", "sprite (31).png"],
    "down": ["sprite.png", "sprite (1).png", "sprite (2).png", "sprite (3).png", "sprite (4).png", "sprite (5).png", "sprite (6).png"],
    "left": ["sprite (13).png", "sprite (14).png", "sprite (15).png", "sprite (16).png", "sprite (17).png", "sprite (18).png"],
    "right": ["sprite (38).png", "sprite (39).png", "sprite (40).png", "sprite (41).png", "sprite (42).png", "sprite (43).png"],
    "up_left": ["sprite (19).png", "sprite (20).png", "sprite (21).png", "sprite (22).png", "sprite (23).png", "sprite (24).png"],
    "up_right": ["sprite (32).png", "sprite (33).png", "sprite (34).png", "sprite (35).png", "sprite (36).png", "sprite (37).png"],
    "down_left": ["sprite (7).png", "sprite (8).png", "sprite (9).png", "sprite (10).png", "sprite (11).png", "sprite (12).png"],
    "down_right": ["sprite (44).png", "sprite (45).png", "sprite (46).png", "sprite (47).png", "sprite (48).png", "sprite (49).png"]
}
jellyfishFloat = [pygame.transform.scale(pygame.image.load("Sprites/" + f).convert_alpha(), (40, 40)) for f in
                  ["sprite (50).png", "sprite (51).png", "sprite (52).png", "sprite (53).png", "sprite (54).png"]]

jellyfishDeath = [pygame.transform.scale(pygame.image.load("Sprites/" + f).convert_alpha(), (40, 40)) for f in
                  ["sprite (55).png", "sprite (56).png", "sprite (57).png", "sprite (58).png", "sprite (59).png", "sprite (60).png", "sprite (61).png"]]

menuSittingCat = [pygame.transform.scale(pygame.image.load("Sprites/" + f).convert_alpha(), (200, 200)) for f in
                  ["sprite (12).png"]]

menuLookingAroundCat = [pygame.transform.scale(pygame.image.load("Sprites/" + f).convert_alpha(), (200, 200)) for f in
                        ["sprite03.png", "sprite04.png", "sprite05.png", "sprite04.png", "sprite03.png", "sprite02.png", "sprite01.png", "sprite02.png", "sprite03.png", "sprite04.png", "sprite03.png"]]

menuLyingDownCat = [pygame.transform.scale(pygame.image.load("Sprites/" + f).convert_alpha(), (200, 200)) for f in
                    ["sprite001.png", "sprite002.png", "sprite003.png", "sprite004.png", "sprite005.png", "sprite006.png", "sprite007.png", "sprite008.png"]]



# === MENU CAT ANIMATION CONTROL ===
menu_cat_states = {
    "sit": menuSittingCat,
    "look": menuLookingAroundCat,
    "lie": menuLyingDownCat,
    "sit_up": list(reversed(menuLyingDownCat)),

}
menu_cat_state = "sit"
menu_cat_frame = 0
menu_cat_forward = True
menu_cat_timer = 0
menu_cat_speed = 0.15
menu_cat_wait_times = {
    "sit": random.uniform(3.0, 4.0),
    "look": random.uniform(2.0, 0.1),
    "lie": random.uniform(5.0, 7.0),
    "sit_up": random.uniform(5.0, 7.0)
}
menu_cat_wait_timer = 0
menu_cat_waiting = False

menu_cat_order = ["sit", "look", "lie", "sit_up"]
menu_cat_index = 0
menu_cat_x, menu_cat_y = 400, 550

# === SCALE SPRITES BASED ON DIRECTION ===
for direction in kittenFramesStill:
    size = vertical_size if direction in ["up", "down"] else normal_size
    kittenFramesStill[direction] = [
        pygame.transform.scale(pygame.image.load(frame).convert_alpha(), size)
        for frame in kittenFramesStill[direction]
    ]
for direction in kittenFramesRunning:
    size = vertical_size if direction in ["up", "down"] else normal_size
    kittenFramesRunning[direction] = [
        pygame.transform.scale(pygame.image.load(frame).convert_alpha(), size)
        for frame in kittenFramesRunning[direction]
    ]


current_frames = kittenFramesStill[current_direction]







# === DRAWING FUNCTIONS ===
def draw_button(screen, w, h, x, y, text, text_color, color, hover_color, mouse_pos):
    is_hovered = x <= mouse_pos[0] <= x + w and y <= mouse_pos[1] <= y + h
    pygame.draw.rect(screen, hover_color if is_hovered else color, (x, y, w, h), border_radius=8)

    words = text.split()
    button_font = pygame.font.SysFont('comicsans', 30)

    if len(words) <= 2:
        text_surface = button_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
        screen.blit(text_surface, text_rect)
    else:
        mid = len(words) // 2
        line1 = " ".join(words[:mid])
        line2 = " ".join(words[mid:])

        text_surface1 = button_font.render(line1, True, text_color)
        text_rect1 = text_surface1.get_rect(center=(x + w / 2, y + text_surface1.get_height() / 2))
        screen.blit(text_surface1, text_rect1)

        text_surface2 = button_font.render(line2, True, text_color)
        text_rect2 = text_surface2.get_rect(center=(x + w / 2, y + 25 + text_surface2.get_height() / 2))
        screen.blit(text_surface2, text_rect2)

    return is_hovered


def draw_text(text, text_color, x, y):
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def save_game(data, filename="save.json"):
    with open(filename, "w") as f:
        json.dump(data, f)


def load_game(filename="save.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return None
def save_progress():
    data = {
        "score": score,
        "upgradeCountSpeed": upgradeCountSpeed,
        "upgradeCountFishSpawnRate": upgradeCountFishSpawnRate,
        "upgradeCountFishValue": upgradeCountFishValue,
        "upgradeCountMagnet": upgradeCountMagnet,
        "dashUpgradeCount": dashUpgradeCount,
        "kitten_speed": kitten_speed,
        "fishSpawnRate": fishSpawnRate,
        "fishvalue": fishvalue,
        "magnetRadius": magnetRadius,
        "upgradeUp_speed": upgradeUp_speed,
        "upgradeUp_fasterSpawnRateFish": upgradeUp_fasterSpawnRateFish,
        "upgradeUp_fishvalue": upgradeUp_fishvalue,
        "upgradeUp_magnet": upgradeUp_magnet
    }
    save_game(data)

def get_animated_bg_color(dt):
    global bg_color_time, day_phase
    bg_color_time += dt * 0.02

    # Smooth oscillation for time of day (starts at day)
    t = (math.sin(bg_color_time + math.pi / 2) + 1) / 2

    # Light blue (day) → deep navy (night)
    light_blue = (90, 190, 255)
    dark_blue = (2, 10, 40)

    # Blend colors
    r = int(dark_blue[0] + (light_blue[0] - dark_blue[0]) * t)
    g = int(dark_blue[1] + (light_blue[1] - dark_blue[1]) * t)
    b = int(dark_blue[2] + (light_blue[2] - dark_blue[2]) * t)

    # Define day/night phases
    if t > 0.6:
        day_phase = "day"
    elif t < 0.4:
        day_phase = "night"

    return (r, g, b, t)


# === GAME OBJECTS (RECTS, VARIABLES) ===
x = random.randint(0, 1920 - 40)
y = random.randint(0, 1080 - 20)
kitten = pygame.Rect(900, 500, 40, 40)
enemy_jellyfish = pygame.Rect(x, y, 40, 40)
rareFish = pygame.Rect(x, y, 40, 40)

kitten_x = float(kitten.x)
kitten_y = float(kitten.y)
enemy_jellyfish_x = float(enemy_jellyfish.x)
enemy_jellyfish_y = float(enemy_jellyfish.y)
kitten_speed = 3.5
enemy_jellyfishSpeed = 3
enemy_jellyfishhealth = 2
enemy_jellyfishmaxhealth = 2
enemy_jellyfishhealthBar = False

fish_list = []
enemy_jellyfishList = []
maxfish = 5
maxenemy_jellyfish = 1
fishvalue = 1
score = 0
health = 5
fishSpawnRate = 5000
SPAWN_FISH = pygame.USEREVENT + 1
SPAWN_ENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_ENEMY, 1500)
pygame.time.set_timer(SPAWN_FISH, fishSpawnRate)
dash_speed = kitten_speed * 2
dash_duration = 0.3
dash_cooldown = 2.0
dash_timer = 0
dash_time_left = 0
is_dashing = False
trail_list = []
trail_duration = 300
normalSpeed = kitten_speed
dashUpgradeCount = 0
dashUpgradeLimit = 1
magnetRadius = 0
fish = pygame.Rect(x, y, 40, 20)
fish_x = float(fish.x)
fish_y = float(fish.y)
stunned = False
stun_timer = 0
stun_duration = 2000
shake_duration = 0
shake_magnitude = 10

hit_effect_duration = 0
hit_effect_color = red
hit_effect_alpha = 100

paused = False
state = "menu"

loaded = load_game()
if loaded:
    score = loaded.get("score", score)
    upgradeCountSpeed = loaded.get("upgradeCountSpeed", upgradeCountSpeed)
    upgradeCountFishSpawnRate = loaded.get("upgradeCountFishSpawnRate", upgradeCountFishSpawnRate)
    upgradeCountFishValue = loaded.get("upgradeCountFishValue", upgradeCountFishValue)
    upgradeCountMagnet = loaded.get("upgradeCountMagnet", upgradeCountMagnet)
    dashUpgradeCount = loaded.get("dashUpgradeCount", dashUpgradeCount)
    magnetRadius = loaded.get("magnetRadius", magnetRadius)
    fishvalue = loaded.get("fishvalue", fishvalue)
    kitten_speed = loaded.get("kitten_speed", kitten_speed)
    fishSpawnRate = loaded.get("fishSpawnRate", fishSpawnRate)
    upgradeUp_speed = loaded.get("upgradeUp_speed", upgradeUp_speed)
    upgradeUp_fishvalue = loaded.get("upgradeUp_fishvalue", upgradeUp_fishvalue)
    upgradeUp_fasterSpawnRateFish = loaded.get("upgradeUp_fasterSpawnRateFish", upgradeUp_fasterSpawnRateFish)
    upgradeUp_magnet = loaded.get("upgradeUp_magnet", upgradeUp_magnet)


# === MAIN GAME LOOP ===
running = True
while running:
    # --- EVENT HANDLING ---
    clicked = False
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress()
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == "game":
                    save_progress()
                    running = False
                    pygame.quit()
                    sys.exit()
                elif state == "shop":
                    state = "game"
                    paused = False
                elif state == "powers":
                    state = "game"
                    paused = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = True
        if not paused:
            if event.type == SPAWN_FISH:
                if len(fish_list) < maxfish:
                    x = random.randint(0, 1920 - 40)
                    y = random.randint(0, 1080 - 20)
                    if day_phase == "day":
                        fish_list.append(pygame.Rect(x, y, 40, 20))
                    else:
                        fish_list.append({
                            "rect": pygame.Rect(x, y, 40, 20),
                            "type": "night",
                            "spawn_time": pygame.time.get_ticks()
                        })
            if event.type == SPAWN_ENEMY:
                if len(enemy_jellyfishList) < maxenemy_jellyfish:
                    x = random.randint(0, 1920 - 40)
                    y = random.randint(0, 1080 - 20)
                    if day_phase == "night":
                        enemy_health = 5
                    else:
                        enemy_health = 3
                    enemy = {
                        "rect": pygame.Rect(x, y, 40, 40),
                        "health": enemy_health,
                        "max_health": enemy_health,
                        "show_health": False,
                        "state": "float",
                        "frame": 0,
                        "frame_timer": 0,
                        "type": "night" if day_phase == "night" else "day"
                    }
                    enemy_jellyfishList.append(enemy)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dashUpgradeCount > 0 >= dash_timer:
                    pygame.mixer.Sound.play(DashSound)
                    is_dashing = True
                    dash_time_left = dash_duration
                    dash_timer = dash_cooldown
    # --- MAGNET LOGIC (PULL FISH TOWARD PLAYER) ---
    for fish in fish_list[:]:

        if isinstance(fish, dict):
            rect = fish["rect"]
        else:
            rect = fish

        dx = kitten.centerx - rect.centerx
        dy = kitten.centery - rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < magnetRadius and distance != 0:
            dx /= distance
            dy /= distance
            pull_speed = 3
            rect.x += dx * pull_speed
            rect.y += dy * pull_speed

    # --- ENEMY MOVEMENT TOWARD PLAYER ---
    if state == "game":
        for enemy in enemy_jellyfishList[:]:
            rect = enemy["rect"]
            dx = kitten.centerx - rect.centerx
            dy = kitten.centery - rect.centery
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance < 2000 and distance != 0:
                dx /= distance
                dy /= distance
                pull_speed = 1
                rect.x += dx * pull_speed
                rect.y += dy * pull_speed

    dt = clock.tick(60) / 1000
    day_cycle_time += dt


    cycle_length = 60
    phase_progress = (math.sin((day_cycle_time / cycle_length) * math.pi * 2) + 1) / 2

    if phase_progress > 0.5:
        day_phase = "night"
    else:
        day_phase = "day"

    # --- SCREEN SHAKE OFFSET CALCULATION ---
    mouse_pos = pygame.mouse.get_pos()
    shake_offset_x = 0
    shake_offset_y = 0
    if shake_duration > 0:
        shake_offset_x = random.randint(-shake_magnitude, shake_magnitude)
        shake_offset_y = random.randint(-shake_magnitude, shake_magnitude)
        shake_duration -= dt


    # === MENU SCREEN ===
    if state == "menu":
        screen.fill(pink)


        paused = True

        # MENU CAT ANIMATION
        menu_cat_timer += dt

        if menu_cat_waiting:
            menu_cat_wait_timer -= dt
            if menu_cat_wait_timer <= 0:
                menu_cat_waiting = False

        else:
            current_speed = 0.15
            if menu_cat_state == "look":
                current_speed = 0.32

            frames = menu_cat_states[menu_cat_state]

            # === CONTROL SPEED ===
            current_speed = 0.15
            if menu_cat_state == "look":
                current_speed = 0.12

            # === CONTROL MINI-PAUSES BETWEEN LOOK FRAMES ===
            look_pause_frames = {2: 5, 6: 2, 9: 2}
            if menu_cat_state == "look" and menu_cat_frame in look_pause_frames:
                current_speed = look_pause_frames[menu_cat_frame]

            if menu_cat_timer >= current_speed:
                menu_cat_timer = 0
                menu_cat_frame += 1

                # When finished with the animation
                if menu_cat_frame >= len(frames):
                    menu_cat_frame = 0
                    menu_cat_index = (menu_cat_index + 1) % len(menu_cat_order)
                    menu_cat_state = menu_cat_order[menu_cat_index]
                    menu_cat_waiting = True
                    menu_cat_wait_timer = menu_cat_wait_times.get(menu_cat_state, 1.0)

        title_surface = title_font.render("KITTEN ADVENTURE", True, lightRed)
        title_rect = title_surface.get_rect(center=(950, 200))


        menu_cat_image = menu_cat_states[menu_cat_state][menu_cat_frame]

        screen.blit(menu_cat_image, (menu_cat_x, menu_cat_y))

        current_frame = menu_cat_states[menu_cat_state][menu_cat_frame]




        heart_y = title_rect.centery - heart_img.get_height() // 2
        left_heart_x = title_rect.left - heart_img.get_width() - 20  # 20px gap
        right_heart_x = title_rect.right + 20



        screen.blit(heart_img, (left_heart_x, heart_y))
        screen.blit(heart_img, (right_heart_x, heart_y))
        shadow = title_font.render("KITTEN ADVENTURE", True, black)
        screen.blit(shadow, (title_rect.x + 4, title_rect.y + 4))
        screen.blit(title_surface, title_rect)
        if draw_button(screen, 200, 65, 850, 400, "Start", black, red, green, mouse_pos) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            state = "game"
            paused = False
        if draw_button(screen, 200, 65, 850, 550, "Exit", black, red, green, mouse_pos) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            running = False
            pygame.quit()
            sys.exit()
        if draw_button(screen, 200, 65, 850, 700, "Tips", black, red, green, mouse_pos) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            state = "tips"
            paused = True
    # === GAME STATE MOVEMENT & ANIMATION ===
    if not paused:
        base_speed = kitten_speed

        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += 1

        if dx != 0 or dy != 0:
            length = (dx ** 2 + dy ** 2) ** 0.5
            dx /= length
            dy /= length

        if stunned:
            stun_timer -= dt * 1000
            if stun_timer <= 0:
                stunned = False

        if is_dashing:
            trail_list.append({
                "image": current_frames[current_direction][current_frame].copy(),
                "pos": (int(kitten_x), int(kitten_y)),
                "time": pygame.time.get_ticks()
            })
            dash_time_left -= dt
            if dash_time_left <= 0:
                is_dashing = False

        if dash_timer > 0 and not is_dashing:
            dash_timer -= dt
            if dash_timer < 0:
                dash_timer = 0
        old_direction = current_direction
        if dx < 0 and dy == 0:
            current_direction = "left"
        elif dx > 0 and dy == 0:
            current_direction = "right"
        elif dy < 0 and dx == 0:
            current_direction = "up"
        elif dy > 0 and dx == 0:
            current_direction = "down"
        elif dx < 0 and dy < 0:
            current_direction = "up_left"
        elif dx > 0 > dy:
            current_direction = "up_right"
        elif dx < 0 < dy:
            current_direction = "down_left"
        elif dx > 0 and dy > 0:
            current_direction = "down_right"


        moving = dx != 0 or dy != 0
        frames = kittenFramesRunning if moving else kittenFramesStill

        if old_direction != current_direction or frames is not current_frames:
            current_frame = 0
            frame_timer = 0
            current_frames = frames
            idle_finished = False

        current_speed = idle_animation_speed if not moving else run_animation_speed
        frame_timer += dt
        if frame_timer >= current_speed:
            frame_timer = 0
            if moving:
                idle_finished = False
                current_frame = (current_frame + 1) % len(current_frames[current_direction])
            else:
                if not idle_finished:
                    current_frame += 1
                    if current_frame >= len(current_frames[current_direction]) - 1:
                        current_frame = len(current_frames[current_direction]) - 1
                        idle_finished = True

        if stunned:
            current_speed = 0
        elif is_dashing:
            current_speed = base_speed * 3
        else:
            current_speed = base_speed

        # --- MOVEMENT UPDATE ---
        kitten_x += dx * current_speed
        kitten_y += dy * current_speed
        kitten.x = int(kitten_x)
        kitten.y = int(kitten_y)
        if bouncing:
            bounce_timer -= dt
            kitten_x += bounce_dx * bounce_strength * dt
            kitten_y += bounce_dy * bounce_strength * dt

            if bounce_timer <= 0:
                bouncing = False


    # === BORDER COLLISION ===
    if not paused:
        if kitten.left < 0:
            kitten.left = 0
            kitten_x = kitten.left
        if kitten.right > 1920:
            kitten.right = 1920
            kitten_x = kitten.left
        if kitten.top < 0:
            kitten.top = 0
            kitten_y = kitten.top
        if kitten.bottom > 1080:
            kitten.bottom = 1080
            kitten_y = kitten.top

    # === ENEMY ANIMATION HANDLING ===
    for enemy in enemy_jellyfishList[:]:
        enemy["frame_timer"] += dt


        float_animation_speed = 0.15
        death_animation_speed = 0.05

        if enemy["state"] == "float":
            if enemy["frame_timer"] >= float_animation_speed:
                enemy["frame_timer"] = 0
                enemy["frame"] = (enemy["frame"] + 1) % len(jellyfishFloat)

        elif enemy["state"] == "dying":
            if enemy["frame_timer"] >= death_animation_speed:
                enemy["frame_timer"] = 0
                if enemy["frame"] < len(jellyfishDeath) - 1:
                    enemy["frame"] += 1
                else:
                    enemy_jellyfishList.remove(enemy)
                    continue


    # === GAME STATE DRAWING ===

    if state == "game":
        r, g, b, t = get_animated_bg_color(dt)
        screen.fill((r, g, b))

        shake_offset_x = 0
        shake_offset_y = 0
        if shake_duration > 0:
            shake_offset_x = random.randint(-shake_magnitude, shake_magnitude)
            shake_offset_y = random.randint(-shake_magnitude, shake_magnitude)
            shake_duration -= dt
        current_time = pygame.time.get_ticks()
        for trail in trail_list[:]:
            if current_time - trail["time"] > trail_duration:
                trail_list.remove(trail)
                continue

            alpha = 255 - int(255 * ((current_time - trail["time"]) / trail_duration))
            trail_image = trail["image"].copy()
            trail_image.set_alpha(alpha)
            screen.blit(trail_image, trail["pos"])
        screen.blit(current_frames[current_direction][current_frame], (kitten_x, kitten_y))
        if not paused:
            # --- DRAW FISH & ENEMIES ---
            current_time = pygame.time.get_ticks()

            for fish in fish_list[:]:

                if isinstance(fish, dict):
                    rect = fish["rect"]
                    fish_type = fish["type"]
                    spawn_time = fish["spawn_time"]
                else:
                    rect = fish
                    fish_type = "normal"
                    spawn_time = 0


                if fish_type == "rare":
                    screen.blit(jellyfishDrop_image, rect)
                else:
                    if fish_type == "night":
                        screen.blit(nightFish_image, rect)
                    else:
                        screen.blit(fish_image, rect)


                if fish_type == "rare" and current_time - spawn_time < 1000:
                    continue


                if kitten.colliderect(rect):
                    pygame.mixer.Sound.play(fishCollection)
                    fish_list.remove(fish)
                    if fish_type == "rare":
                        score += 15
                    else:
                        score += fishvalue
            for enemy in enemy_jellyfishList[:]:
                rect = enemy["rect"]
                if enemy["state"] == "float":
                    frame = jellyfishFloat[enemy["frame"]]
                else:
                    frame = jellyfishDeath[min(enemy["frame"], len(jellyfishDeath) - 1)]


                screen.blit(frame, rect)

                if enemy["state"] == "float":

                    night_strength = 1 - abs((t - 0.25) * 3.5)
                    night_strength = max(0, min(night_strength, 1))


                    night_strength = night_strength ** 0.9

                    base_alpha = int(150 * night_strength)
                    pulse = int((math.sin(pygame.time.get_ticks() * 0.005) + 1) * 25 * night_strength)
                    glow_color = (0, 120, 255, base_alpha + pulse)

                    if base_alpha > 0:
                        glow_surface = pygame.Surface((rect.width * 3, rect.height * 3), pygame.SRCALPHA)
                        pygame.draw.circle(
                            glow_surface,
                            glow_color,
                            (rect.width * 1.5, rect.height * 1.5),
                            rect.width
                        )
                        screen.blit(glow_surface, (rect.centerx - rect.width * 1.5, rect.centery - rect.height * 1.5))

                # --- COLLISION HANDLING (DAMAGE, BOUNCE, DEATH) ---
                if kitten.colliderect(rect) and not is_dashing and not bouncing and not enemy["state"] == "dying":
                    dx = rect.centerx - kitten.centerx
                    dy = rect.centery - kitten.centery
                    dist = (dx ** 2 + dy ** 2) ** 0.5
                    if dist != 0:
                        dx /= dist
                        dy /= dist

                    bouncing = True
                    bounce_dx = -dx
                    bounce_dy = -dy
                    bounce_timer = bounce_duration
                    is_dashing = False
                    pygame.mixer.Sound.play(enemyHit)
                    shake_duration = 0.3
                    hit_effect_duration = 0.2
                    if score > 0:
                        score = int(score * 0.9)
                    stunned = True
                    stun_timer = stun_duration


                elif kitten.colliderect(rect) and not stunned and is_dashing:
                    pygame.mixer.Sound.play(enemyDamage)
                    enemy["health"] -= 1
                    enemy["show_health"] = True


                    shake_duration = 0.3

                    if enemy["health"] <= 0:
                        pygame.mixer.Sound.play(enemyKill)
                        score += 2
                        enemy["state"] = "dying"
                        enemy["frame"] = 0
                        enemy["frame_timer"] = 0
                        if random.randint(1, 10) == 1:
                            drop_x = rect.x
                            drop_y = rect.y
                            rare_fish_rect = pygame.Rect(drop_x, drop_y, 40, 40)
                            fish_list.append({
                                "rect": rare_fish_rect,
                                "type": "rare",
                                "spawn_time": pygame.time.get_ticks()
                            })


                    dx = rect.centerx - kitten.centerx
                    dy = rect.centery - kitten.centery
                    dist = (dx ** 2 + dy ** 2) ** 0.5
                    if dist != 0:
                        dx /= dist
                        dy /= dist

                    bouncing = True
                    bounce_dx = -dx
                    bounce_dy = -dy
                    bounce_timer = bounce_duration
                    is_dashing = False

            if stunned:
                stun_timer -= dt * 1000
                if stun_timer <= 0:
                    stunned = False

            base_speed = kitten_speed

            if stunned:
                current_speed = 0
            elif is_dashing:
                current_speed = base_speed * 2
            else:
                current_speed = base_speed


    # === UNIVERSAL ELEMENTS / INTERFACE ===
    if state == "game":
        if draw_button(screen, 150, 50, 1750, 80, "SHOP", black, red, green, mouse_pos) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            state = "shop"
            paused = True

    if state == "tips":
        screen.fill(lightblue)
        if draw_button(screen, 200, 65, 70, 50, "BACK", black, red, green, mouse_pos ) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            state = "menu"
            clicked = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            state = "menu"
        draw_text("Unlock Dash to be able", black, 550, 470)
        draw_text("to kill enemies", black, 550, 500)
        draw_text("There is a 10% chance that a jellyfish", black, 550, 600)
        draw_text("would drop a rare fish after death", black, 550, 630)
        draw_text("Use WASD or Arrow Keys to move", black, 1250, 470)
        draw_text("Press Spacebar to dash", black, 1250, 600)
        draw_text("Collect fish to increase your score", black, 1250, 730)
        draw_text("Use your score to buy upgrades in the shop", black, 550, 730)





    if state == "shop":
        screen.fill(bg_color)
        if draw_button(screen, 150, 50, 1750, 180, "RETURN", black, red, green, mouse_pos) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            state = "game"
            clicked = False
            paused = False
        elif draw_button(screen, 150, 50, 1750, 280, "POWERS", black, red, green, mouse_pos) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            state = "powers"
            clicked = False
            paused = True
        if upgradeCountSpeed < upgradeLimitFish:
            draw_text(f"{upgradeUp_speed[0]} POINTS", black, 1392, 470)
        else:
            draw_text("MAX LEVEL", black, 1392, 470)
        if draw_button(screen, 200, 65, 1300, 500, f"SPEED LVL{upgradeCountSpeed}", black, red, green,
                       mouse_pos) and clicked and upgradeCountSpeed < upgradeLimitFish and upgradeUp_speed and score >= \
                upgradeUp_speed[0]:
            pygame.mixer.Sound.play(buttonClick)
            kitten_speed += 0.2
            upgradeCountSpeed += 1
            score -= upgradeUp_speed[0]
            upgradeUp_speed.remove(upgradeUp_speed[0])
        if upgradeCountFishSpawnRate < upgradeLimitFishSpawnRate:
            draw_text(f"{upgradeUp_fasterSpawnRateFish[0]} POINTS", black, 1092, 470)
        else:
            draw_text("MAX LEVEL", black, 1092, 470)
        if draw_button(screen, 200, 65, 1000, 500, f"FISH SPAWN RATE LVL{upgradeCountFishSpawnRate}", black, red, green,
                       mouse_pos) and clicked and upgradeCountFishSpawnRate < upgradeLimitFishSpawnRate and upgradeUp_fasterSpawnRateFish and score >= \
                upgradeUp_fasterSpawnRateFish[0]:
            pygame.mixer.Sound.play(buttonClick)
            fishSpawnRate -= 500
            pygame.time.set_timer(SPAWN_FISH, fishSpawnRate)
            upgradeCountFishSpawnRate += 1
            score -= upgradeUp_fasterSpawnRateFish[0]
            upgradeUp_fasterSpawnRateFish.remove(upgradeUp_fasterSpawnRateFish[0])
        if upgradeCountFishValue < upgradeLimitFishValue:
            draw_text(f"{upgradeUp_fishvalue[0]} POINTS", black, 792, 470)
        else:
            draw_text("MAX LEVEL", black, 792, 470)
        if draw_button(screen, 200, 65, 700, 500, f"FISH VALUE LVL{upgradeCountFishValue}", black, red, green,
                       mouse_pos) and clicked and upgradeCountFishValue < upgradeLimitFishValue and upgradeUp_fishvalue and score >= \
                upgradeUp_fishvalue[0]:
            pygame.mixer.Sound.play(buttonClick)
            fishvalue += 1
            upgradeCountFishValue += 1
            score -= upgradeUp_fishvalue[0]
            upgradeUp_fishvalue.remove(upgradeUp_fishvalue[0])
        if upgradeCountMagnet < upgradeLimitMagnet:
            draw_text(f"{upgradeUp_magnet[0]} POINTS", black, 492, 470)
        else:
            draw_text("MAX LEVEL", black, 492, 470)
        if draw_button(screen, 210, 65, 400, 500, f"MAGNET LVL{upgradeCountMagnet}", black, red, green,
                       mouse_pos) and clicked and upgradeCountMagnet < upgradeLimitMagnet and upgradeUp_magnet and score >= \
                upgradeUp_magnet[0]:
            pygame.mixer.Sound.play(buttonClick)
            magnetRadius += 300
            upgradeCountMagnet += 1
            score -= upgradeUp_magnet[0]
            upgradeUp_magnet.remove(upgradeUp_magnet[0])

    if state == "powers":
        screen.fill(bg_color)
        if draw_button(screen, 150, 50, 1750, 280, "SHOP", black, red, green, mouse_pos) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            state = "shop"
            clicked = False
            paused = True
        if draw_button(screen, 150, 50, 1750, 180, "RETURN", black, red, green, mouse_pos) and clicked:
            pygame.mixer.Sound.play(buttonClick)
            state = "game"
            clicked = False
            paused = False
        if dashUpgradeCount < dashUpgradeLimit:
            draw_text("100 POINTS", black, 1392, 470)
            draw_text("TIP: DASH INTO ENEMIES", black, 1392, 585)
            draw_text("TO DAMAGE THEM", black, 1392, 620)
        else:
            draw_text("BOUGHT", black, 1392, 470)
        if draw_button(screen, 200, 65, 1300, 500, "DASH", black, red, green,
                       mouse_pos) and clicked and dashUpgradeCount < dashUpgradeLimit and score >= 100:
            pygame.mixer.Sound.play(buttonClick)
            Dash = kitten_speed * 2
            dashUpgradeCount += 1
            score -= 100

    if state == "game" or state == "shop" or state == "powers":
        screen.blit(font.render(str(score), True, black), (50, 50))
    if dashUpgradeCount > 0 and state == "game":
        bar_width = 200
        bar_height = 20
        bar_x = 50
        bar_y = 100
        fill_ratio = max(0, min(1, 1 - dash_timer / dash_cooldown))
        pygame.draw.rect(screen, black, (bar_x, bar_y, bar_width, bar_height), 2)
        pygame.draw.rect(screen, green, (bar_x, bar_y, bar_width * fill_ratio, bar_height))
    if hit_effect_duration > 0:
        hit_effect_duration -= dt
        hit_surface = pygame.Surface((1920, 1080))
        hit_surface.set_alpha(hit_effect_alpha)
        hit_surface.fill(hit_effect_color)
        screen.blit(hit_surface, (0, 0))

    # === DRAW ENEMY HEALTH BARS ===
    for enemy in enemy_jellyfishList:
        if enemy["show_health"] and not enemy["state"] == "dying":
            rect = enemy["rect"]
            bar_x = rect.x
            bar_y = rect.y - 10
            bar_width = rect.width
            bar_height = 5
            health_ratio = enemy["health"] / enemy["max_health"]

            pygame.draw.rect(screen, (80, 80, 80), (bar_x, bar_y, bar_width, bar_height))
            pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height))

    pygame.display.flip()
