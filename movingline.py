from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Line, Color, Ellipse
from kivy.metrics import dp
from kivy.uix.widget import Widget


class MyLine(App):
    def build(self):
        pass

class moveline(Widget):
    a = 0
    b = 0
    c = 600
    d = 500
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.ball1 =Line(points=((self.width*0.20),self.height,(self.width*0.20),self.height))
            self.ball2 = Line(points=((self.width * 0.40), 0, (self.width * 0.40), 0))
            self.ball3 = Line(points=((self.width * 0.60), self.height, (self.width * 0.60), self.height))
            self.ball4 = Line(points=((self.width * 0.80), self.height, (self.width * 0.80), self.height))
            Clock.schedule_interval(self.Update,1/500)
    def on_size(self, *args):
        pass

    def Update(self,dt):

        if self.a < self.height :
            self.b = self.b + 1
            self.ball1.points = ((self.width*0.2),(self.a),(self.width*0.2),(self.b))
        else:
            self.a = 0
            self.b = 0
            self.ball1.points = ((self.width*0.2), (self.a), (self.width*0.2), (self.b))

        if self.b > 100:
            self.b = self.b+1
            self.a = self.a+2
            self.ball1.points = ((self.width*0.2),self.a,(self.width*0.2),self.b)

        if self.c > (0) :
            self.c = self.c-1
            self.d = self.d-1
            self.ball2.points = ((self.width*0.4),self.d,(self.width*0.4),self.c)
            print(self.d)

        else:
            self.c = self.height
            self.d= self.height
            self.ball2.points=((self.width*0.4),self.d,(self.width*0.4),self.c)

        '''else:
            self.a = self.heihjt
            self.b = self.height
            self.ball2.points = ((self.width*0.4), (self.height), (self.width*0.4), (self.height))
            '''




        """""
        if self.a <= self.height :
            self.b = self.b + 1
            self.ball3.points = ((self.width*0.6),(self.a),(self.width*0.6),(self.b))
        else:
            self.a = 0
            self.b = 0
            self.ball3.points = ((self.width*0.6), (self.a), (self.width*0.6), (self.b))

        if self.b > 100:
            self.b = self.b+1
            self.a = self.a+2
            self.ball3.points = ((self.width*0.6),self.a,(self.width*0.6),self.b)

        if self.a <= self.height :
            self.b = self.b + 1
            self.ball4.points = ((self.width*0.8),(self.a),(self.width*0.8),(self.b))
        else:
            self.a = 0
            self.b = 0
            self.ball4.points = ((self.width*0.8), (self.a), (self.width*0.8), (self.b))

        if self.b > 100:
            self.b = self.b+1
            self.a = self.a+2
            self.ball4.points = ((self.width*0.8),self.a,(self.width*0.8),self.b)
        """""

MyLine().run()