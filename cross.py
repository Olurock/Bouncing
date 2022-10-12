from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Line, Color, Ellipse
from kivy.metrics import dp
from kivy.uix.widget import Widget


class CrossLine(App):
    def build(self):
        pass

class crossline(Widget):
    a = 0
    b = 0
    c = 0
    d = 0
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.line=Line(points = (self.a,self.b,self.c,self.d))
            Clock.schedule_interval(self.Update,1/500)
    def on_size(self, *args):
        pass

    def Update(self,dt):
        self.a = 0
        self.b = self.height*0.5
        self.d = self.height*0.5
        self.c = self.c+1
        self.line.points = (self.a, self.b, self.c, self.d)

CrossLine().run()