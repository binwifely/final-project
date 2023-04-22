from pygame import*
from button import Button

window = display.set_mode((500, 500))
clock = time.Clock()

game = True
run = False

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

        if i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                run = not run
    
    if run:
        window.fill((255, 0, 0))
    else:
        window.fill((0, 0, 0))
        