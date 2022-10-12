from kivy._event import __init__
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Line, Color, Ellipse, Rectangle
from kivy.metrics import dp
from kivy.uix.widget import Widget


class CanvassExp(App):
    def build(self):
        pass

class wid(Widget):
    size = dp(100)
    pos = (400)
    circle = []
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        self.init_circle()
    def init_circle(self):
        with self.canvas:
            Color(1,0,0)
            for i in range(0,2):
                self.circle.append(Rectangle)

    def update_circle(self):
        self.init_circle()
        for i in self.circle:
            self.circle[i].pos=[200,200]



    def update(self,dt):
        pass


CanvassExp().run()