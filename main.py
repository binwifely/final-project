from pygame import*
from button import Button

window = display.set_mode((500, 500))
clock = time.Clock()

game = True
run = False
play = Button(250, 100, 200, 50, 'play_button.png')   
exit = Button(250, 250, 200, 50, 'exit_button.png')
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif exit.draw(window):
            game = False

        if i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                run = not run
    
    if run:
        window.fill((255, 0, 0))
    else:
        window.fill((0, 0, 0))
        if play.draw(window):
            run = True
        if exit.draw(window):
            run = False
    display.update()
    clock.tick(60)

