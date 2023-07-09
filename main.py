from pygame import *

WIDTH = 1200
HEIGHT = 700

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Доганялки")
background = transform.scale(image.load("images/bg.jpg"), (WIDTH, HEIGHT))

sprite_1 = transform.scale(image.load("images/sprite1.png"), (100, 100))
x_1 = 100
y_1 = 300

sprite_2 = transform.scale(image.load("images/sprite2.png"), (100, 100))
x_2 = 1000
y_2 = 300


clock = time.Clock()

window.blit(background, (0, 0))

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                exit()

    keys_pressed = key.get_pressed()

    if keys_pressed[K_w] and y_1 > 0:
        y_1 -= 10
    if keys_pressed[K_s] and y_1 < HEIGHT - 90:
        y_1 += 10
    if keys_pressed[K_a] and x_1 > -5:
        x_1 -= 10
    if keys_pressed[K_d] and x_1 < WIDTH - 95:
        x_1 += 10

    if keys_pressed[K_UP] and y_2 > 0:
        y_2 -= 10
    if keys_pressed[K_DOWN] and y_2 < HEIGHT - 90:
        y_2 += 10
    if keys_pressed[K_LEFT] and x_2 > -5:
        x_2 -= 10
    if keys_pressed[K_RIGHT] and x_2 < WIDTH - 95:
        x_2 += 10

    window.blit(background, (0, 0))

    window.blit(sprite_1, (x_1, y_1))
    window.blit(sprite_2, (x_2, y_2))

    clock.tick(60)
    display.update()
