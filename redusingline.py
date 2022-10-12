from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Line, Color, Ellipse
from kivy.metrics import dp
from kivy.uix.widget import Widget


class ReduceLine(App):
    def build(self):
        pass

class reduceline(Widget):
    points=0
    a=100
    b=100
    c=600
    d=100
    e=350
    f=350
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            line = Line(points=(0, self.b, self.width, self.b))
            self.ball = line
            self.line1 = Line(points=(100,100,self.e,self.f))
            self.line2 = Line(points=(self.e, self.f, 600, 100))
            #self.ball3 = Line(points=((self.width * 0.60), self.height, (self.width * 0.60), self.height))
            #self.ball4 = Line(points=((self.width * 0.80), self.height, (self.width * 0.80), self.height))
            Clock.schedule_interval(self.Update,1/500)
    def on_size(self, *args):
        pass
    def Update(self,dt):
        '''''
        self.a=self.height*0.125
        self.e=self.width*0.5
        self.f=self.height*0.59
        self.line1.points= (0,self.a,self.e,self.f)
        self.line2.points = ( self.e, self.f, self.width, self.a)
        self.ball.points = ((self.points, self.b, self.width, self.a))
        if self.a == self.height*0.125:
            self.a = 100
            self.b = 100
            self.c = 600
            self.d = 100
            self.ball.points = ((self.a, self.b, self.c, self.d))
        '''



ReduceLine().run()