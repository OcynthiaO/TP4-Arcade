import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.AMARANTH_PINK,arcade.color.AFRICAN_VIOLET, arcade.color.BABY_BLUE_EYES, arcade.color.BLUE_VIOLET, arcade.color.CHERRY]


#classe Balle
class Balle:
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = random.choice(COLORS)

#Placer la balle sur l’écran
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.x = self.rayon
            self.change_x *= -1

        if self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon
            self.change_x *= -1

        if self.y < self.rayon:
            self.y = self.rayon
            self.change_y *= -1

        if self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon
            self.change_y *= -1

#dessiner la balle à l’écran
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

#classe Rectangle
class Rectangle:
    def __init__(self, x, y, change_x, change_y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.angle = angle
        self.color = random.choice(COLORS)

# Placer le rectangle sur l’écran
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.width / 2:
            self.x = self.width / 2
            self.change_x *= -1

        if self.x > SCREEN_WIDTH - self.width / 2:
            self.x = SCREEN_WIDTH - self.width / 2
            self.change_x *= -1

        if self.y < self.height / 2:
            self.y = self.height / 2
            self.change_y *= -1

        if self.y > SCREEN_HEIGHT - self.height / 2:
            self.y = SCREEN_HEIGHT - self.height / 2
            self.change_y *= -1

# dessiner le rectangle à l’écran
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

#classe MyGame
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        arcade.set_background_color(arcade.color.WHITE)

        self.balles = []
        self.rectangles = []

    def on_draw(self):
        arcade.start_render()

        for balle in self.balles:
            balle.draw()

        for rectangle in self.rectangles:
            rectangle.draw()

#clique de la souris
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle = Balle(x, y, 3, 3, random.randint(10, 30), random.choice(COLORS))
            self.balles.append(balle)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y, 3, 3, random.randint(20, 50), random.randint(20, 50),random.choice(COLORS), 0)
            self.rectangles.append(rectangle)

    def on_update(self, delta_time):
        for balle in self.balles:
            balle.update()

        for rectangle in self.rectangles:
            rectangle.update()

def main():
    my_game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()

