from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Line, Color, Ellipse
from kivy.metrics import dp
from kivy.uix.widget import Widget


class PointLine(App):
    def build(self):
        pass

class pointline(Widget):
    a = 100
    b = 100
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.line=Line(points=(0,0,self.b,self.a), width=2)
            Clock.schedule_interval(self.Update, 1 / 50)
    def On_size(self):
        pass
    def Update(self,dt):
        self.a=self.height
        self.b = self.width
        self.line.points = (0,0,self.b,self.a)

PointLine().run()
