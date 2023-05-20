from pygame import*
from button import Button
from sprite import Player
window = display.set_mode((500, 500))
clock = time.Clock()

game = True
run = False
road = image.load('road.png')
play = Button(250, 100, 200, 50, 'play_button.png')   
exit = Button(250, 250, 200, 50, 'exit_button.png')


car = Player('car.png', 250, 10, 50, 100, 5)

road = transform.scale(road, (500, 500))
road_width = road.get_width()
tiles = 2
scroll = 0
speed = 10

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
        for i in range(0, tiles):
            window.blit(road, (0, i * road_width + scroll))
        scroll -= 3

        if abs(scroll) > road_width:
            scroll = 0
        
        car.draw(window)
        car.move()
    else:
        window.fill((0, 0, 0))
        if play.draw(window):
            run = True
        if exit.draw(window):
            run = False
    display.update()
    clock.tick(60)

