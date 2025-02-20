import pygame
import random
import sys

from pygame import mixer

mixer.init()
pygame.init()

# COLORS
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
grey = (127, 127, 127)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

screen_width = 1280
screen_height = 720

# GAME WINDOW
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ADVENTUROUS WORLD")
pygame.display.update()

# BACKGROUND
bg = pygame.image.load("Images/frontpage.jpg")
cr = pygame.image.load("Images/CRDBG.jpg")
cr_2 = pygame.image.load("Images/CRDBG_2.png")
os_2 = pygame.image.load("Images/SR.jpg")
ad_1 = pygame.image.load("Images/ADVENTURE_1.jpg")
ad_2 = pygame.image.load("Images/ADVENTURE_2.jpg")
gameover = pygame.image.load("Images/gameover.jpg")
ad_complete_fire = pygame.image.load("Images/ADVENTURE COMPLETED_Fire.jpg")
ad_complete_water = pygame.image.load("Images/ADVENTURE COMPLETED_Water.jpg")

# ----------- WINDOW ICON -----------------------------
Game_icon = pygame.image.load("Images/AW_ICON.png")
pygame.display.set_icon(Game_icon)

# ---------------------- SOUND EFFECTS ------------------------------

flg_adv1_reached = pygame.mixer.Sound('Sound Effects/Flag_reached.mp3')
mixer.Sound.set_volume(flg_adv1_reached, 0.4)
trophy_coll = pygame.mixer.Sound('Sound Effects/Trophy_collect.mp3')
mixer.Sound.set_volume(trophy_coll, 0.4)
sack_coll = pygame.mixer.Sound('Sound Effects/sack_collection.mp3')
mixer.Sound.set_volume(sack_coll, 0.4)
mtr_clash = pygame.mixer.Sound('Sound Effects/MTR_Clash.mp3')
jump_adv1 = pygame.mixer.Sound('Sound Effects/adv_1_jump.mp3')
mixer.Sound.set_volume(jump_adv1, 0.3)

f = 50   # *** Used for handling main menu menu selection ***

# FONTS
f1 = pygame.font.Font('Fonts/PIXEL.ttf', 70)
f2 = pygame.font.Font('Fonts/PIXEL.ttf', 50)
f3 = pygame.font.Font('Fonts/PIXEL.ttf', f + 10)
f4 = pygame.font.Font('Fonts/StoryElement.ttf', 35)
f5 = pygame.font.Font('Fonts/StoryElement.ttf', 45)
f6 = pygame.font.Font('Fonts/StoryElement.ttf', 46)

f10 = pygame.font.Font('Fonts/Hussar.ttf', 30)
f11 = pygame.font.Font('Fonts/Hussar.ttf', 35)



# --------------- SOME GAME VARIABLES ----------------------------------

score = 0           # Must be Globally Used

# ---------------------- Used for Closing the Window -----------------------------

def quit_1():
    pygame.quit()
    # quit()
    sys.exit()
# ---------------------- Used to output strings in Adventures -----------------------------

# def draw_text(text, font, text_col, x, y):
#     img = font.render(text, True, text_col)
#     screen.blit(img, (x, y))

def display_text(text, color, x, y):
    d_text = f11.render(text, True, color)
    screen.blit(d_text, (x, y))

# ---------------------- Used to Display ADVENTURE COMPLETE SCREEN -----------------------------

def adventure_complete(chk):

    mixer.music.load('Music/ADV COMP.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1, 0, 1000)

    game_exit_5 = False
    while not game_exit_5:


        for event_5 in pygame.event.get():

            if event_5.type == pygame.QUIT:  # FOR QUIT
                game_exit_5 = True

            if event_5.type == pygame.KEYDOWN:

                if event_5.key == pygame.K_ESCAPE:  # FOR RETURNING TO MAIN MENU
                    mixer.fadeout(1000)
                    mixer.music.stop()
                    function2()
                if event_5.key == pygame.K_BACKSPACE:  # FOR RETURNING TO MAIN MENU
                    mixer.fadeout(1000)
                    mixer.music.stop()
                    function2()

        if chk == True:
            screen.blit(ad_complete_fire, (0, 0))
        else:
            screen.blit(ad_complete_water, (0, 0))


        pygame.display.update()

    quit_1()

# ---------------------- Used to Display Game Over Screen -----------------------------

def game_over(chk):

    mixer.music.load('Music/GAMEOVER.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1, 0, 1000)
    game_exit_5 = False

    while not game_exit_5:

        for event_5 in pygame.event.get():

            if event_5.type == pygame.QUIT:  # FOR QUIT
                game_exit_5 = True

            if event_5.type == pygame.KEYDOWN:

                if event_5.key == pygame.K_ESCAPE:  # FOR RETURNING TO MAIN MENU
                    mixer.fadeout(1000)
                    mixer.music.stop()
                    function2()
                if event_5.key == pygame.K_BACKSPACE:  # FOR RETURNING TO MAIN MENU
                    mixer.fadeout(1000)
                    mixer.music.stop()
                    function2()

        screen.blit(gameover, (0, 0))

        pygame.display.update()

    quit_1()

# -------------------------------- Restarts the Adventure ----------------------------------------------

def adv_restart():

    trophy_group_fire.empty()
    trophy_group_water.empty()

    firemeteor_group.empty()
    firemeteor_group.add(Meteor_Fire(1279, random.choice(location_meteor_fire)))

    watermeteor_group.empty()
    watermeteor_group.add(Meteor_Water(1279, random.choice(location_meteor_water)))

    gold_sack_group.add(Gold_Sack(120, 255))
    gold_sack_group.add(Gold_Sack(570, 255))
    gold_sack_group.add(Gold_Sack(860, 255))
    gold_sack_group.add(Gold_Sack(370, 135))

    trophy_group_fire.add(Trophy_Fire(1050, 108))
    trophy_group_water.add(Trophy_Water(1040, 98))

# ------------------------- (MAIN) PLAYER CLASS FOR ADVENTURE 1 ----------------------------------------

class Player(pygame.sprite.Sprite):

    def __init__(self, ppp):
        super().__init__()

        self.move_right = False
        self.move_left = False
        self.vel_y = 0
        self.cor_y = 480  # USED FOR SPAWNING
        self.jump = False
        self.collected = False
        self.alive = True

        self.clock = pygame.time.Clock()

        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        if ppp == True:
            for num in range(1, 4):
                img_right = pygame.image.load(f"Images/EXP/EXP{num}.png")
                img_right = pygame.transform.scale(img_right, (60, 90))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
        else:
            for num in range(1, 4):
                img_right = pygame.image.load(f"Images/ADR/ADR{num}.png")
                img_right = pygame.transform.scale(img_right, (60, 90))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)

        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect_width = self.image.get_width()
        self.rect_height = self.image.get_height()

        self.rect.topleft = (30, 480)  # USED FOR SPAWNING

        self.direction = 0

    def update(self, ppp, level_id):

        global score

        for event_4 in pygame.event.get():

            if event_4.type == pygame.QUIT:  # FOR QUIT
                quit_1()

            if event_4.type == pygame.KEYDOWN:

                if event_4.key == pygame.K_ESCAPE:  # FOR RETURNING TO MAIN MENU
                    score = 0
                    adv_restart()  # Reset Level
                    mixer.music.stop()
                    function2()

                if event_4.key == pygame.K_LEFT:
                    self.move_left = True

                if event_4.key == pygame.K_RIGHT:
                    self.move_right = True

            elif event_4.type == pygame.KEYUP:

                if event_4.key == pygame.K_LEFT:
                    self.move_left = False

                if event_4.key == pygame.K_RIGHT:
                    self.move_right = False

        dx = 0          # Used for Updating player's position
        dy = 0          # Used for Updating player's position
        walk_speed = 5
#------------------------------------------------------------------------------------------
        h_pos = [200, 430, 784]
        hurdle = [0, 1, 2]
        length_hl = len(hurdle)

        hurdle[0] = (Hurdles(h_pos[0], level_id))
        hurdle[1] = (Hurdles(h_pos[1], level_id))
        hurdle[2] = (Hurdles(h_pos[2], level_id))
#------------------------------------------------------------------------------------------
        il_pos = [110, 300, 560, 300, 850, 300]
        island = [0, 1, 2]
        length_fil = len(island)

        island[0] = (Floating_Islands(il_pos[0], il_pos[1], level_id))
        island[1] = (Floating_Islands(il_pos[2], il_pos[3], level_id))
        island[2] = (Floating_Islands(il_pos[4], il_pos[5], level_id))
#------------------------------------------------------------------------------------------
        il_pos_2 = [360, 180, 1050, 180]
        island_2 = [0, 1]
        length_fil_2 = len(island_2)

        island_2[0] = (Floating_Islands(il_pos_2[0], il_pos_2[1], level_id))
        island_2[1] = (Floating_Islands(il_pos_2[2], il_pos_2[3], level_id))
#------------------------------------------------------------------------------------------

        bh_pos = [248, 720, 896]
        big_hurdle = [0, 1, 2]
        length_bhl = len(big_hurdle)

        big_hurdle[0] = (Big_Hurdles(bh_pos[0], level_id))
        big_hurdle[1] = (Big_Hurdles(bh_pos[1], level_id))
        big_hurdle[2] = (Big_Hurdles(bh_pos[2], level_id))

# ------------------------------------------ JUMP LOGIC --------------------------------------------------------------
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.jump is False:

            if self.rect.y == self.cor_y or self.rect.bottom == hurdle[0].hurdle.top or self.rect.bottom == island[0].flt_island.top or \
                    self.rect.bottom == island_2[0].flt_island.top or self.rect.bottom == big_hurdle[0].bg_hurdle.top:
                jump_adv1.play()
                self.vel_y = -17.5          # Jump distance covered
                self.jump = True

        if key[pygame.K_SPACE] == False:

            if self.rect.y == self.cor_y or self.rect.bottom == hurdle[0].hurdle.top or self.rect.bottom == island[0].flt_island.top or \
                    self.rect.bottom == island_2[0].flt_island.top or self.rect.bottom == big_hurdle[0].bg_hurdle.top:
                self.jump = False

# -------------------------------------------------------------------------------------------------------------------

        if (self.move_left):            # Moves Player in Left direction
            if self.rect.x > 15:
                dx -= 4
                self.counter += 1
                self.direction = -1

        if (self.move_right):           # Moves Player in Right direction
            if self.rect.x < 1170:
                dx += 4
                self.counter += 1
                self.direction = 1

        if (self.move_left) == False and (self.move_right) == False:
            self.counter = 0
            self.index = 0

            if self.direction == 1:
                self.image = self.images_right[self.index]

            if self.direction == -1:
                self.image = self.images_left[self.index]

            if self.direction == 2:
                self.image = self.images_right[4]

            if self.direction == -2:
                self.image = self.images_right[4]


# ------------------------ PLAYER ANIMATION -------------------------------------------------------------------------

        if self.counter > walk_speed:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0

            if self.direction == 1:
                self.image = self.images_right[self.index]

            if self.direction == -1:
                self.image = self.images_left[self.index]


# --------- JUMP VELOCITY LOGIC --------------------

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

# ------------------------------------------ COLLISION DETECTION LOGIC FOR JUMP --------------------------------------------------------------

# ------- For fat hurdle ------------

        i = 0
        while i < length_hl:

            if hurdle[i].hurdle.colliderect(self.rect.x + dx, self.rect.y, self.rect_width, self.rect_height):
                dx = 0

            if hurdle[i].hurdle.colliderect(self.rect.x, self.rect.y + dy, self.rect_width, self.rect_height):

                if self.vel_y >= 0:
                    dy = hurdle[i].hurdle.top - self.rect.bottom
                    self.vel_y = 0

            i += 1

# ------- For Floating Island (Below Ones) ------------

        j = 0
        while j < length_fil:

            if island[j].flt_island.colliderect(self.rect.x + dx, self.rect.y, self.rect_width, self.rect_height):
                dx = 0

            if island[j].flt_island.colliderect(self.rect.x, self.rect.y + dy, self.rect_width, self.rect_height):

                if self.vel_y < 0:
                    dy = island[j].flt_island.bottom - self.rect.top

                if self.vel_y >= 0:
                    dy = island[j].flt_island.top - self.rect.bottom
                    self.vel_y = 0
            j += 1

# ------- For Floating Island (Top ones) ------------

        l = 0
        while l < length_fil_2:
            if island_2[l].flt_island.colliderect(self.rect.x + dx, self.rect.y, self.rect_width, self.rect_height):
                dx = 0

            if island_2[l].flt_island.colliderect(self.rect.x, self.rect.y + dy, self.rect_width, self.rect_height):

                if self.vel_y < 0:
                    dy = island_2[l].flt_island.bottom - self.rect.top

                if self.vel_y >= 0:
                    dy = island_2[l].flt_island.top - self.rect.bottom
                    self.vel_y = 0

            l += 1


# ----------- For Long Hurdle ------------------

        k = 0
        while k < length_bhl:

            if big_hurdle[k].bg_hurdle.colliderect(self.rect.x + dx, self.rect.y, self.rect_width, self.rect_height):
                dx = 0

            if big_hurdle[k].bg_hurdle.colliderect(self.rect.x, self.rect.y + dy, self.rect_width, self.rect_height):

                if self.vel_y >= 0:
                    dy = big_hurdle[k].bg_hurdle.top - self.rect.bottom
                    self.vel_y = 0

            k += 1
# ---------------------------------------------------------------------------------------------------------------------------------

# -------------------- SOME OTHER COLLISIONS WITH SPRITES --------------------------

        if ppp == True:
            if pygame.sprite.spritecollide(self, firemeteor_group, False):
                mtr_clash.play()
                score = 0
                self.alive = False
        else:
            if pygame.sprite.spritecollide(self, watermeteor_group, False):
                mtr_clash.play()
                score = 0
                self.alive = False

        if pygame.sprite.spritecollide(self, gold_sack_group, True):
            sack_coll.play()
            score += 50

        display_text(str(score), green, 1135, 10)
        if score > 0 and score < 100:
            display_text('K', green, 1190, 10)
        if score > 50 and score < 150:
            display_text('K', green, 1210, 10)
        if score > 100 and score < 200:
            display_text('K', green, 1205, 10)
        if score > 150:
            display_text('K', green, 1216, 10)


        if ppp == True:
            if pygame.sprite.spritecollide(self, trophy_group_fire, True):
                trophy_coll.play()
                self.collected = True
        else:
            if pygame.sprite.spritecollide(self, trophy_group_water, True):
                trophy_coll.play()
                self.collected = True

        if pygame.sprite.spritecollide(self, flag_group, False):
            if self.collected is True:
                flg_adv1_reached.play()
                score = 0
                adv_restart()
                mixer.music.stop()
                mixer.fadeout(600)
                adventure_complete(ppp)       # CALLING ADVENTURE COMPLETE SCREEN
# -------------------------------------------------------------------------------------------------------------------------------------

        self.rect.x += dx           # Updating Player x axis value
        self.rect.y += dy           # Updating Players y axis Value

        if self.rect.y <= 70:       # Limit for Jump
            self.vel_y = 0

        if self.rect.y >= self.cor_y:       # Limit to stay remain on the ground After Jump
            self.rect.y = self.cor_y
            dy = 0

        self.clock.tick(70)


# ----------------------- DISPLAY PLAYER ON THE SCREEN --------------------------

    def render(self, screen):

        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, white, self.rect, 2)

# ---------------------------- ALL CLASSES USED IN Adventure --------------------------------------------

class Hurdles(pygame.sprite.Sprite):

    def __init__(self, x, level):
        super().__init__()

        if level == True:
            self.hrd_image = pygame.image.load("Images/h1_fire.png")
        else:
            self.hrd_image = pygame.image.load("Images/h1.png")

        self.hurdle = self.hrd_image.get_rect()
        self.hurdle.topleft = (x, 480)

    def render(self, screen):
        screen.blit(self.hrd_image, self.hurdle)


class Big_Hurdles(pygame.sprite.Sprite):

    def __init__(self, bg_x, level):
        super().__init__()

        if level == True:
            self.bg_hrd_image = pygame.image.load("Images/h2a_fire.png")
        else:
            self.bg_hrd_image = pygame.image.load("Images/h2a.png")

        self.bg_hurdle = self.bg_hrd_image.get_rect()
        self.bg_hurdle.topleft = (bg_x, 435)

    def render(self, screen):
        screen.blit(self.bg_hrd_image, self.bg_hurdle)


class Floating_Islands(pygame.sprite.Sprite):

    def __init__(self, j_x, j_y, level):
        super().__init__()

        if level == True:
            self.isl_image = pygame.image.load("Images/fli_fire.png")
        else:
            self.isl_image = pygame.image.load("Images/fli.png")

        self.flt_island = self.isl_image.get_rect()
        self.flt_island.topleft = (j_x, j_y)

    def render(self, screen):
        screen.blit(self.isl_image, self.flt_island)

#----------------------------------------------------------------------------------------------
class Meteor_Water(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("Images/water meteor.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):

        self.rect.x -= 5
        self.clock.tick(70)
        # pygame.draw.rect(screen, white, self.rect, 2)


class Meteor_Fire(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("Images/fire meteor.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):

        self.rect.x -= 5
        self.clock.tick(70)
        # pygame.draw.rect(screen, white, self.rect, 2)

#----------------------------------------------------------------------------------------------

class Gold_Sack(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("Images/gold.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):

        pass

#----------------------------------------------------------------------------------------------
class Trophy_Fire(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("Images/cup 1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass

class Trophy_Water(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("Images/cup 2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass

#----------------------------------------------------------------------------------------------

class Flag(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("Images/flag.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):

        pass


# ---------------------------------------------------------------
global check
# ------ FLAG GROUP ------------
flag_group = pygame.sprite.Group()
flag_group.add(Flag(1200, 500))

# ------ TROPHY GROUP ------------
trophy_group_fire = pygame.sprite.Group()
trophy_group_fire.add(Trophy_Fire(1050, 108))

trophy_group_water = pygame.sprite.Group()
trophy_group_water.add(Trophy_Water(1040, 98))

# ------ GOLD SACK GROUP ------------
gold_sack_group = pygame.sprite.Group()
gold_sack_group.add(Gold_Sack(120, 255))
gold_sack_group.add(Gold_Sack(570, 255))
gold_sack_group.add(Gold_Sack(860, 255))
gold_sack_group.add(Gold_Sack(370, 135))

# ------ METEOR GROUP ------------
firemeteor_group = pygame.sprite.Group()
location_meteor_fire = [100, 150, 230, 260, 370, 400]
firemeteor_group.add(Meteor_Fire(1279, random.choice(location_meteor_fire)))

watermeteor_group = pygame.sprite.Group()
location_meteor_water = [100, 150, 230, 260, 370, 400]
watermeteor_group.add(Meteor_Water(1279, random.choice(location_meteor_water)))


# ------------------------- FUNCTION DISPLAYS Adventure 1 ------------------------------------------

def adventure(player):

    mixer.music.load('Music/ADV 1.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1, 0, 1000)

    ch = player

    ply = Player(player)
    meteor_freq = 1000
    start_time = pygame.time.get_ticks()
    game_exit_4 = False

# BIG HURDLES LIST

    bh_pos = [248, 720, 896]
    big_hurdle = [0, 1, 2]
    length_bhl = len(big_hurdle)
    big_hurdle[0] = (Big_Hurdles(bh_pos[0], ch))
    big_hurdle[1] = (Big_Hurdles(bh_pos[1], ch))
    big_hurdle[2] = (Big_Hurdles(bh_pos[2], ch))

# HURDLES LIST

    h_pos = [200, 430, 784]
    hurdle = [0, 1, 2]
    length_hl = len(hurdle)
    hurdle[0] = (Hurdles(h_pos[0], ch))
    hurdle[1] = (Hurdles(h_pos[1], ch))
    hurdle[2] = (Hurdles(h_pos[2], ch))

# FLOATING ISLAND LIST (Below)

    il_pos = [110, 300, 560, 300, 850, 300]
    island = [0, 1, 2]
    length_fil = len(island)
    island[0] = (Floating_Islands(il_pos[0], il_pos[1], ch))
    island[1] = (Floating_Islands(il_pos[2], il_pos[3], ch))
    island[2] = (Floating_Islands(il_pos[4], il_pos[5], ch))

# FLOATING ISLAND LIST (Above)

    il_pos_2 = [360, 180, 1050, 180]
    island_2 = [0, 1]
    length_fil_2 = len(island_2)
    island_2[0] = (Floating_Islands(il_pos_2[0], il_pos_2[1], ch))
    island_2[1] = (Floating_Islands(il_pos_2[2], il_pos_2[3], ch))
    # location_meteor = [100, 150, 230, 260, 370, 400]

# ------------------- GAME LOOP FOR ADVENTURE -------------------------

    while not game_exit_4:

        current_time = pygame.time.get_ticks()
        delta_time = current_time - start_time

        if delta_time >= meteor_freq:
            if player == True:
                y = random.choice(location_meteor_fire)
                m = Meteor_Fire(1279, y)
                firemeteor_group.add(m)
                start_time = current_time
            else:
                y = random.choice(location_meteor_water)
                m = Meteor_Water(1279, y)
                watermeteor_group.add(m)
                start_time = current_time

# ---------------- DISPLAYS IF PLAYER IS ALIVE ------------------

        if ply.alive:

            if player == True:
                screen.blit(ad_2, (0, 0))
            else:
                screen.blit(ad_1, (0, 0))

            ply.render(screen)
            ply.update(ch, ch)

            k = 0
            while k < length_bhl:
                big_hurdle[k].render(screen)
                k += 1

            i = 0
            while i < length_hl:
                hurdle[i].render(screen)
                i += 1

            j = 0
            while j < length_fil:
                island[j].render(screen)
                j += 1

            l = 0
            while l < length_fil_2:
                island_2[l].render(screen)
                l += 1

            gold_sack_group.draw(screen)
            flag_group.draw(screen)

            if player == True:
                trophy_group_fire.draw(screen)

                firemeteor_group.update()
                firemeteor_group.draw(screen)
            else:
                trophy_group_water.draw(screen)

                watermeteor_group.update()
                watermeteor_group.draw(screen)


            pygame.display.update()

# ---------------- DISPLAYS IF PLAYER IS DEAD ------------------

        else:
            adv_restart()     # Reset Level
            mixer.music.stop()
            mixer.fadeout(1000)
            game_over(ch)         # Game Over Screen

# --------------------- FUNCTION DISPLAYS ADVENTURE SELECTION MENU -------------------------------------------------

def function2():

    mixer.music.load('Music/ADV SEL.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1, 0, 1000)

    clock = pygame.time.Clock()
    # x_a1 = 280
    game_exit2 = False

    advnt_1 = pygame.image.load("Images/Fire.png")
    advnt_2 = pygame.image.load("Images/Water.png")
    adventure_hl = pygame.image.load("Images/select_hlt_1.png")
    adventure_h2 = pygame.image.load("Images/select_hlt_2.png")

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False
            m_pos = pygame.mouse.get_pos()

            # MOUSE COLLISION DETECTION
            if self.rect.collidepoint(m_pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action

    advn1_button = Button(160, 150, advnt_1)
    advn2_button = Button(160, 420, advnt_2)

    while not game_exit2:

        for event_2 in pygame.event.get():

            if event_2.type == pygame.QUIT:  # FOR QUIT
                game_exit2 = True

            if event_2.type == pygame.KEYDOWN:

                if event_2.key == pygame.K_ESCAPE:  # FOR RETURNING TO MAIN MENU
                    mixer.music.stop()
                    mixer.fadeout(600)
                    function1()

                if event_2.key == pygame.K_BACKSPACE:  # FOR RETURNING TO MAIN MENU
                    mixer.music.stop()
                    mixer.fadeout(600)
                    function1()

        if advn1_button.draw():

            mixer.music.stop()
            mixer.fadeout(600)
            adventure(True)  # Fire Level
            clock.tick(60)

        if advn2_button.draw():

            mixer.music.stop()
            mixer.fadeout(600)
            adventure(False)  # Water Level
            clock.tick(60)

        ms_pos = pygame.mouse.get_pos()
        screen.blit(os_2, (0, 0))

        # FOR MOUSE HIGHLIGHTING REFERENCE

        # pygame.draw.rect(screen, red, (155, 145, 175, 220))       # REFERENCE Coordinates
        # pygame.draw.rect(screen, blue, (155, 415, 175, 220))      # REFERENCE Coordinates

        if 155+175 > ms_pos[0] > 155 and 145+220 > ms_pos[1] > 145:    # For SELECTING ADVENTURE 1 (FIRE)
            screen.blit(adventure_hl, (100, 115))

        if 155+175 > ms_pos[0] > 155 and 415+220 > ms_pos[1] > 415:   # For SELECTING ADVENTURE 2 (WATER)
            screen.blit(adventure_h2, (100, 385))

        advn1_button.draw()
        advn2_button.draw()

        pygame.display.update()

    quit_1()

# --------------------------------------- CLASS WHICH DISPLAYS CREDITS NAMES -------------------------------------------------------

class nm(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.nm_image = pygame.image.load("Images/Numbering_matter.png")
        self.nm_rect = self.nm_image.get_rect()
        self.nm_rect.topleft = (300, 100)

    def render(self, screen):
        screen.blit(self.nm_image, self.nm_rect)

    def update(self):

        pass

nm_names = nm()

# --------------------------------------- FUNCTION FOR CONTROLLING PREVIOUS CREDITS CLASS -----------------------------------------------------

def function3():

    mixer.music.load('Music/CDT.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1, 0, 1000)

    game_exit3 = False

    while not game_exit3:

        for event_3 in pygame.event.get():

            if event_3.type == pygame.QUIT:  # FOR QUIT
                game_exit3 = True

            if event_3.type == pygame.KEYDOWN:

                if event_3.key == pygame.K_BACKSPACE:  # FOR RETURNING TO MAIN MENU
                    mixer.music.stop()
                    mixer.fadeout(600)
                    nm_names.nm_rect.y = 370
                    function1()

                if event_3.key == pygame.K_ESCAPE:  # FOR RETURNING TO MAIN MENU
                    mixer.music.stop()
                    mixer.fadeout(600)
                    nm_names.nm_rect.y = 370
                    function1()

        screen.blit(cr, (0, 0))
        nm_names.render(screen)
        nm_names.update()
        screen.blit(cr_2, (0, 0))

        pygame.display.update()

    quit_1()

# --------------------------------- FUNCTION DISPLAYS MAIN MENU SCREEN -----------------------------------------------------------

def function1():

    mixer.music.load('Music/MM.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1, 0, 1000)

    clock = pygame.time.Clock()
    game_exit = False

    # MENU BUTTONS

    start_img = pygame.image.load("Images/start.png")
    hl_start = pygame.image.load("Images/start_hlt.png")

    cred_img = pygame.image.load("Images/cred.png")
    hl_cred = pygame.image.load("Images/cred_hlt.png")

    exit_img = pygame.image.load("Images/exit.png")
    hl_exit = pygame.image.load("Images/exit_hlt.png")

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False
            m_pos = pygame.mouse.get_pos()

            # MOUSE COLLISION DETECTION
            if self.rect.collidepoint(m_pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action

    start_button = Button(380, 402, start_img)
    cred_button = Button(760, 310, cred_img)
    exit_button = Button(740, 550, exit_img)

    while not game_exit:

        for event_1 in pygame.event.get():

            if event_1.type == pygame.QUIT:  # FOR QUIT
                game_exit = True

        if cred_button.draw():

            pygame.time.delay(350)
            mixer.music.stop()
            mixer.fadeout(600)
            function3()    # CREDIT SCREEN
            clock.tick(60)

        if start_button.draw():

            pygame.time.delay(350)
            mixer.music.stop()
            mixer.fadeout(600)
            function2()   # ADVENTURE SELECTION SCREEN
            clock.tick(60)

        if exit_button.draw():

            pygame.time.delay(350)
            clock.tick(60)
            mixer.music.stop()
            mixer.fadeout(600)
            quit_1()

        ms_pos = pygame.mouse.get_pos()
        screen.blit(bg, (0, 0))


        # FOR MOUSE HIGHLIGHTING

        if 380+240 > ms_pos[0] > 380 and 402+90 > ms_pos[1] > 402:
            screen.blit(hl_start, (278, 287))

        if 760+200 > ms_pos[0] > 760 and 310+100 > ms_pos[1] > 310:
            screen.blit(hl_cred, (658, 230))

        if 740+180 > ms_pos[0] > 740 and 550+100 > ms_pos[1] > 550:
            screen.blit(hl_exit, (635, 466))

        start_button.draw()
        cred_button.draw()
        exit_button.draw()

        pygame.display.update()

    quit_1()

# --------------------------------------------------------------------------------------------------------------------------

function1()        # Calls the Function which Displays MAIN MENU

