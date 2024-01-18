import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Balle:
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.x = self.rayon
            self.change_x*=-2

        if self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon

        if self.y < self.rayon:
            self.change_y*=-2

        if self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle:
    def __init__(self, x, y, change_x, change_y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle

    class Balle:
        def __init__(self, x, y, change_x, change_y, rayon, color):
            self.x = x
            self.y = y
            self.change_x = change_x
            self.change_y = change_y
            self.rayon = rayon
            self.color = color

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

        def draw(self):
            arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


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

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle = Balle(x, y, 2, 2, random.randint(10, 30), arcade.color.RED)
            self.balles.append(balle)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y, 2, 2, random.randint(20, 50), random.randint(20, 50), arcade.color.BLUE, 0)
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

