from random import *

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget




class RealSnake(App):
    def build(self):
        pass
def collide(Snake,food):
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
    snakes=[]
    x,y = (0,0)
    new_snake=[]
    hor_pos=500
    ver_pos=200
    state=[1]
    enable=BooleanProperty(True)
    foodsize = 20
    snake = 40
    angle = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.init_snake()
            self.update_size()
            self.head = Rectangle(size=(self.snake,10), pos=(self.hor_pos, self.ver_pos))
            self.food = Rectangle(size=(self.foodsize, self.foodsize), pos=(randint(0,600),randint(0,600)))
            self.label = Label(text='',pos=(self.width/2,self.height/2))
            #self.add_widget(self.label)
            #self.init_snake()
            Clock.schedule_interval(self.Update, 1/100)
    def update_movement(self):
        for i in self.snakes:
            x,y = self.snakes[0].pos
            x=x+1
            self.snakes[0].pos=(x,y)
    def update_size(self):
        for i in self.snakes:
            self.snakes[0].size=(40,10)

    def init_snake(self):
        with self.canvas:
            self.snakes.append(Rectangle())

    def Moveup(self,Widget):
        a=(str(Widget.state))
        if a == 'down':
            self.state.remove(self.state[0])
            self.state.append('up')


        #new = Button(size=(self.x,self.y),pos=(self.head.pos))
        #self.x += 2
        #new.size = (self.x, self.y)
        #self.add_widget(new)



    def Movedown(self,Widget):
        b = (str(Widget.state))
        if b == 'down':
            self.state.remove(self.state[0])
            self.state.append('down')

    def Moveleft(self,Widget):
        c = (str(Widget.state))
        if c == 'down':
            self.state.remove(self.state[0])
            self.state.append('left')

    def Moveright(self,Widget):
        d = (str(Widget.state))
        if d == 'down':
            self.state.remove(self.state[0])
            self.state.append('right')

    def Update(self,dt):
        print(self.snakes[0].pos)
        self.update_movement()
        for i in self.state:
            if i == 1:
                x,y = self.head.pos
                x=x+1
                self.head.pos = x, y
            if i == 'up':
                x, y = self.head.pos
                y += 1
                self.head.pos = x, y
            if self.state[0] != 'up':
                self.ids.up.state = 'normal'

            if i == 'down':
                x, y = self.head.pos
                y -= 1
                self.head.pos = x, y
            if self.state[0] != 'down':
                self.ids.down.state = 'normal'

            if i == 'left':
                x, y = self.head.pos
                x -= 1
                self.head.pos = x, y
            if self.state[0] != 'left':
                self.ids.left.state = 'normal'

            if i == 'right':
                x, y = self.head.pos
                x += 1
                self.head.pos = x, y
            if self.state[0] != 'right':
                self.ids.right.state = 'normal'

        if self.head.pos == self.food.pos:
            self.foodsize = 0
            self.food.size=(self.foodsize,self.foodsize)
        
        x,y = self.head.pos
        h,w = self.head.size
        if x == 0 or x == self.width-h or y == 0 or y == self.height-w:
            self.label.text = 'GAME OVER'
        
        if collide((self.head.pos,self.head.size),(self.food.pos,self.food.size)):
            self.food.pos=(randint(0,600),randint(0,600))
            self.snake = self.snake + 20
            self.head.size=(self.snake,10)


class Screen(Widget):
    pass




RealSnake().run()
