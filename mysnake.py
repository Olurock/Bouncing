from random import *

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class MySnake(App):
    def build(self):
        pass


def collide(Snake, food):
    r1x = Snake[0][0]
    r1y = Snake[0][1]
    r2x = food[0][0]
    r2y = food[0][1]
    r1w = Snake[1][0]
    r1h = Snake[1][1]
    r2w = food[1][0]
    r2h = food[1][1]
    if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
        return True
    else:
        return False


class SnakePart(Widget):
    snakes = []
    x, y = (0, 0)
    new_snake = []
    hor_pos = 200
    ver_pos = 200
    state = [1]
    enable = BooleanProperty(True)
    foodsize = 20
    snake = 40
    angle = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_snake()
        Clock.schedule_interval(self.Update, 1 / 100)

    def init_snake(self):
        with self.canvas:
            self.snakes.append(Rectangle())
    def update_snake_up(self):
        for i in self.snakes:
            i.size = 50,10
            x,y=i.pos
            x=x+1
            i.pos=x,y


    def Moveup(self,Widget):
        a = (str(Widget.state))
        print(a)
        if a == 'down':
            self.update_snake_up()
    def Movedown(self,Widget):
        a= (str(Widget.state))
        if a == 'down':
            self.update_snake()

    def Update(self,dt):
        self.Moveup()







class Screen(Widget):
    pass


MySnake().run()
