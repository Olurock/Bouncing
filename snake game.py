import random

from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ListProperty


class SnakegameApp(App):
    def build(self):
        pass
class Snake(Widget):
    def Moveup(self,Widget):
        self.wid = Rectangle()
        self.add_widget(self.wid)


SnakegameApp().run()
