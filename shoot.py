from random import randint

apple = Actor("apple")
score = 0

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        score += 1
        print("Good shot! Current score: " + str(score))
        place_apple()
    else:
        print("You missed. Game over, Man! FINAL SCORE: " + str(score))
        quit()

place_apple()
