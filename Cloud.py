from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse
from kivy.metrics import dp
from kivy.uix.widget import Widget


class Cloud(Widget):
    size = dp(50)
    pos = (400)

    def get_rectangle(self):
        with self.canvas:
            self.rec = Rectangle(pos=(self.size, self.pos), size=(self.size, self.size))

    def get_circle(self):
        cirleft = self.rec.pos[0] - self.size * 0.5
        cirright = self.rec.pos[0] + self.size * 0.5
        cirtops = self.size + 30
        cirtop = self.pos + self.size * 0.45
        with self.canvas:
            self.ellipse1 = Ellipse(pos=(cirleft, self.pos), size=(self.size, cirtops))
            self.ellipse2= Ellipse(pos=(cirright, self.pos), size=(self.size, cirtops))
            self.ellipse3= Ellipse(pos=(self.rec.pos[0], cirtop), size=(self.size, cirtops))

