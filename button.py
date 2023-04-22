class Button():
    def __init__(self, x, y, width, height, button_image_name):
        self.image = transform.scale(image.load(button_image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False

    def draw(self, window):
        pose = mouse.get_pose()
        action = False
        
        if self.rect.collidepoint(pose):
            if mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True
            
            if mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        return action