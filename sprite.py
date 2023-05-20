from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Player(GameSprite):
    def move(self):
        keys_preseed = key.get_pressed()
        if keys_preseed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_preseed[K_d] and self.rect.x < 440:
            self.rect.x += self.speed

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))