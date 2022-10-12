from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Line, Color, Ellipse, Rectangle
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


def collide(rec1,rec2):
    r1x = rec1[0][0]
    r1y = rec1[0][1]
    r2x = rec2[0][0]
    r2y = rec2[0][1]
    r1w = rec1[1][0]
    r1h =rec1[1][1]
    r2w = rec2[1][0]
    r2h = rec2[1][1]
    if (r1x<r2x+r2w and r1x+r1w>r2x and r1y <r2y+r2h and r1y+r1h>r2y):

        print(rec1[0])
        return True
    else:
        return False

class MyBall(App):
    def build(self):
        pass

class Bounce(Widget):
    dx = 3
    dy = 4
    ball_size=50
    save = [1]
    barrier = ObjectProperty()
    pos = 200
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.ball = Ellipse(pos=(0,60), size=(self.ball_size,self.ball_size))
            self.barrier = Rectangle(pos = (self.pos,50),size = (300,20))
            Clock.schedule_interval(self.Update,1/1000)
            self.label=Label(pos=(self.width/2,self.height/2))
            #Clock.schedule_interval(self.on_touch_down, 1 / 2)

    def on_size(self, *args):
        pass
    def start(self):
        print(11)

    def Update(self,dt):
        (x,y) = self.ball.pos
        x = x + self.dx
        y = y + self.dy

        if (y + self.ball_size) > self.height:
            y = self.height - self.ball_size
            self.dy = -self.dy
        if (x + self.ball_size) > self.width:
            x = self.width - self.ball_size
            self.dx = -self.dx
        if y < 0:
            y = 0
            self.dy = -self.dy
        if x < 0:
            x = 0
            self.dx = -self.dx

        self.ball.pos = x,y
        if collide((self.barrier.pos,self.barrier.size),(self.ball.pos,self.ball.size)):
            self.dy = -self.dy
        if self.ball.pos[1] < self.barrier.pos[1]:
            self.label.text = 'GAME OVER'
            self.ball.pos = 0,0
    def on_touch_down(self, touch):
        if touch.x < self.width/2:
            a,b = self.barrier.pos
            self.pos -= 3
            a=self.pos
            self.barrier.pos=a,b





MyBall().run()