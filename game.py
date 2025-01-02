import pygame
import random
from pygame import mixer
import tkinter as tk


pygame.init()
pygame.mixer.init()

#screen setting

screen=pygame.display.set_mode((1000,600))
bg=pygame.image.load("C:/Users/AAC/Downloads/istockphoto-1613780002-1024x1024-transformed.jpeg")
bg=pygame.transform.scale(bg,(1000,600))

#Game name and icon

pygame.display.set_caption("Fruity Heist")  
icon=pygame.image.load("C:/Users/AAC/Documents/8691038.png")    
pygame.display.set_icon(icon)

# Function for displaying text (FRIUTY HEIST)
def text_screen(text, color, x, y, font):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])

# Fonts (FRUITY HEIST)
font_small = pygame.font.SysFont('comicsansms', 30)
bubbly_font_large = pygame.font.Font("C:/Users/AAC/Downloads/Bubbleboddy-FatTrial.ttf", 70)

# Load images for buttons
start_img = pygame.image.load("C:/Users/AAC/Downloads/start-button.png")
end_img = pygame.image.load("C:/Users/AAC/Downloads/exit.png")

# Resize images
start_img = pygame.transform.scale(start_img, (200, 100)) 
end_img = pygame.transform.scale(end_img, (200, 100))

# Button class
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_hovered(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        return False
    
# Position buttons on screen
start_button = Button(365, 300, start_img)
exit_button = Button(365, start_button.rect.bottom + 20, end_img)
    
# Welcome screen
def welcome():
    exit_game = False
    bg = pygame.image.load("C:/Users/AAC/Downloads/istockphoto-1613780002-1024x1024-transformed.jpeg")
    bg = pygame.transform.scale(bg, (1000, 600))  # Resize the background

    while not exit_game:
        screen.blit(bg, (0, 0))  # Blit background
        text_screen("FRUITY HEIST", (255, 0, 255), 285, 140, bubbly_font_large)  # Title text

        # Draw buttons
        start_button.draw()  
        exit_button.draw()

        if start_button.is_hovered():
            pygame.draw.rect(screen, (255, 255, 0), start_button.rect, 8)

        if exit_button.is_hovered():
            pygame.draw.rect(screen, (255, 255, 0), exit_button.rect,8)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True  
            if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse button click
                if start_button.is_hovered():  # If start button is clicked
                    gameloop()  # Start the game loop when the start button is clicked
                    return  # Exit the welcome function to prevent it from looping again
                if exit_button.is_hovered():  # If exit button is clicked
                    exit_game = True  # Exit the game

        pygame.display.update()
        clock.tick(60)


#clock

clock=pygame.time.Clock()


def gameloop():

    #Background music

    mixer.music.load("C:/Users/AAC/Downloads/mixkit-too-cool-too-crazy-1159.wav")
    mixer.music.play(-1)

    # Loot font
    catch_font = pygame.font.SysFont("lucidasans", 32, "bold")
    catch_fontX = 10
    catch_fontY = 10

    # Basket
    basket = pygame.image.load("C:/Users/AAC/Downloads/picnic_4346757.png")
    basket = pygame.transform.scale(basket, (200, 200))
    basketX = 400
    basketY = 410
    vel = 9

    # Initializing some variables
    score = 0
    fallen_fruits = 0
    missed_fruits = 0
    running = True
    #button_rect = None

    # Game over punch lines
    lines = ["Oops! The heist ends here! 😔", "Mission Squashed! 🍎🍉🍓", "Fruits win this time! 👀"]
    punch_lines = random.choice(lines)

    def Basket():
        screen.blit(basket, (basketX, basketY))

    def Fruits(fruitsX, fruitsY, i):
        screen.blit(fruits_img[i], (fruitsX, fruitsY))

    def show_loot(x, y):
        loot_value = catch_font.render("YOUR LOOTS:" + str(score), True, (204, 102, 0))
        screen.blit(loot_value, (x, y))

    def Game_over_screen(score):
        def quit_game():
            game_over_window.destroy()
            pygame.quit()
            quit()

        game_over_window = tk.Tk()
        game_over_window.title("Game Over")
        game_over_window.iconbitmap("C:/Users/AAC/Documents/8691038.png")
        game_over_window.geometry(f"500x400+{300}+{200}")
        game_over_window.configure(bg="#FFB347")
        tk.Label(
            game_over_window,
            text=punch_lines,
            font=("papyrus", 24, "bold"),
            fg="GREEN",
            bg="#FFB347",
        ).pack(pady=20)
        tk.Label(
            game_over_window,
            text=f"Your Total Loots: {score}",
            font=("papyrus", 16, "bold"),
            fg="brown",
            bg="#FFB347",
        ).pack()
        tk.Button(
            game_over_window,
            text="OKAY",
            font=("papyrus", 14, "bold"),
            command=quit_game,
            bg="green",
            fg="red",
        ).pack(pady=20)
        game_over_window.mainloop()

    # Fruits
    apple = pygame.image.load("C:/Users/AAC/Downloads/wink_9651007.png")
    apple = pygame.transform.scale(apple, (80, 80))

    watermelon = pygame.image.load("C:/Users/AAC/Downloads/wink_9816231.png")
    watermelon = pygame.transform.scale(watermelon, (90, 90))

    orange = pygame.image.load("C:/Users/AAC/Downloads/cool_12637602-removebg-preview.png")
    orange = pygame.transform.scale(orange, (90, 90))

    grapes = pygame.image.load("C:/Users/AAC/Downloads/grapes_9087864.png")
    grapes = pygame.transform.scale(grapes, (100, 100))

    pear = pygame.image.load("C:/Users/AAC/Downloads/smile_12466129-removebg-preview.png")
    pear = pygame.transform.scale(pear, (110, 110))

    strawberry = pygame.image.load("C:/Users/AAC/Downloads/happy_8446031.png")
    strawberry = pygame.transform.scale(strawberry, (70, 70))

    mango = pygame.image.load("C:/Users/AAC/Downloads/star_12794342-removebg-preview.png")
    mango = pygame.transform.scale(mango, (110, 110))

    fruits = [apple, mango, watermelon, orange, grapes, strawberry, pear]
    fruits_img = []
    fruitsX = []
    fruitsY = []
    fruitsX_change = []
    fruitsY_change = []

    no_of_fruits = 6

    for i in range(no_of_fruits):
        fruits_img.append(random.choice(fruits))
        fruitsX.append(random.randint(0, 900))
        fruitsY.append(random.randint(0, 700))
        fruitsX_change.append(random.randint(3, 5))
        fruitsY_change.append(random.randint(3, 5))

    # Bomb
    bomb = pygame.image.load("C:/Users/AAC/Downloads/bomb-removebg-preview.png")
    bomb = pygame.transform.scale(bomb, (150, 150))
    bombX = 0
    bombY = -50
    bomb_active = False
    bomb_vel = 3

    # Diamond
    diamond = pygame.image.load("C:/Users/AAC/Downloads/shopping_14079147.png")
    diamond = pygame.transform.scale(diamond, (70, 70))
    diamondX = 0
    diamondY = -50
    diamond_active = False
    diamond_vel = 6

    # DSE reminder
    reminder_font=pygame.font.SysFont('comicsans',30)
    reminder_interval=60000
    reminder_message="Gaming is fun, but don't forget to blink and rest your eyes!"
    last_reminder_time=0
    show_reminder=False
    reminder_duration=2000
    reminder_start=0

#button font
    button_font = pygame.font.SysFont('comicsansms',18)

# Quit button
    quit_button_rect = pygame.Rect(900, 10, 80, 40)
  
    running = True
    button_rect = None

    while running:
        screen.blit(bg, (0, 0))  # Blit the background image

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button_rect.collidepoint(event.pos):  # Quit button clicked
                    running = False

        pygame.draw.rect(bg, (255, 0, 0), quit_button_rect)
        quit_text = button_font.render("QUIT", True, (255, 255, 255))
        bg.blit(quit_text, (quit_button_rect.x + 10, quit_button_rect.y + 5))

        current_time = pygame.time.get_ticks()
        if not show_reminder and current_time - last_reminder_time >= reminder_interval:
            show_reminder = True
            reminder_start = current_time
            last_reminder_time = current_time

        if show_reminder:
            if current_time - reminder_start <= reminder_duration:
                reminder_text = reminder_font.render(reminder_message, True, "Red")
                reminder_rect = reminder_text.get_rect(center=(500, 100))
                bg.blit(reminder_text, reminder_rect)
            else:
                show_reminder = False

        clock.tick(60)

        # Basket movements
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basketX -= vel
        if keys[pygame.K_RIGHT]:
            basketX += vel

        # Basket boundaries
        if basketX <= -2:
            basketX = -2
        elif basketX >= 807:
            basketX = 807

        # Fruits movement
        for i in range(no_of_fruits):
            if fruitsY[i] > 600:
                fruitsY[i] = random.randint(-700, -50)
                fruitsX[i] = random.randint(0, 900)
                fruits_img[i] = random.choice(fruits)
            fruitsY[i] += fruitsY_change[i]

        for i in range(no_of_fruits):
            Fruits(fruitsX[i], fruitsY[i], i)

        # Loots
        for i in range(no_of_fruits):
            if basketX < fruitsX[i] + 50 < basketX + 200 and basketY < fruitsY[i] + 50 < basketY + 200:
                score += 1
                fruitsX[i] = random.randint(0, 960)
                fruitsY[i] = random.randint(-700, -50)
                fruits_img[i] = random.choice(fruits)

            fruitsY[i] += fruitsY_change[i]
            if fruitsY[i] > 600:
                fruitsX[i] = random.randint(0, 960)
                fruitsY[i] = random.randint(-700, -50)
                fruits_img[i] = random.choice(fruits)

            Fruits(fruitsX[i], fruitsY[i], i)

        # Bomb movement
        for i in range(no_of_fruits):
            fruitsY[i] += fruitsY_change[i]
            if basketX < fruitsX[i] < basketX + 150 and basketY < fruitsY[i] < basketY + 100:
                fruitsX[i] = random.randint(0, 750)
                fruitsY[i] = -random.randint(100, 500)
                fruitsY_change[i] = 2
                score += 1
                fallen_fruits += 1
            elif fruitsY[i] > 600:
                fruitsX[i] = random.randint(0, 750)
                fruitsY[i] = -random.randint(100, 500)
                fruitsY_change[i] = 2
                missed_fruits += 1
                fallen_fruits += 1

            Fruits(fruitsX[i], fruitsY[i], i)

        if fallen_fruits > 0 and fallen_fruits % 10 == 0 and not bomb_active:
            bombX = random.randint(0, 750)
            bombY = -10
            bomb_active = True

        if bomb_active:
            bombY += bomb_vel
            screen.blit(bomb, (bombX, bombY))

            # If bomb caught then game over
            if basketX < bombX < basketX + 150 and basketY < bombY < basketY + 100:
                running = False
                Game_over_screen(score)
            elif bombY > 600:
                bomb_active = False

        # If 30 fruits missed, game over
        if missed_fruits >= 30:
            running = False
            Game_over_screen(score)

        # Diamond movement
        for i in range(no_of_fruits):
            if basketX < fruitsX[i] + 50 < basketX + 200 and basketY < fruitsY[i] + 50 < basketY + 200:
                score += 1
                fruitsX[i] = random.randint(0, 960)
                fruitsY[i] = random.randint(-700, -50)
                fruits_img[i] = random.choice(fruits)

            fruitsY[i] += fruitsY_change[i]
            if fruitsY[i] > 600:
                fruitsX[i] = random.randint(0, 960)
                fruitsY[i] = random.randint(-700, -50)
                fruits_img[i] = random.choice(fruits)

            Fruits(fruitsX[i], fruitsY[i], i)

        if fallen_fruits > 0 and fallen_fruits % 15 == 0 and not diamond_active:
            diamondX = random.randint(0, 750)
            diamondY = -10
            diamond_active = True

        if diamond_active:
            diamondY += diamond_vel
            screen.blit(diamond, (diamondX, diamondY))

            if basketX < diamondX < basketX + 150 and basketY < diamondY < basketY + 100:
                score += 10
                diamond_sound = mixer.Sound("C:/Users/AAC/Downloads/mixkit-bonus-earned-in-video-game-2058.wav")
                diamond_sound.play()
                diamond_active=False
            elif diamondY > 600:
                diamond_active = False

        show_loot(catch_fontX, catch_fontY)
        Basket()
        pygame.display.flip()

    pygame.quit()

welcome()












