from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget


class Single(App):
    def build(self):
        pass


class OurLayout(Widget):
    labelpos = (200,200)
    downpos = (0,200)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text = 'up',on_press = self.moveup) )
        self.label = Label(text='Hello', pos = self.labelpos)
        self.add_widget(self.label)

    def moveup(self, a):
        y = self.label.y
        if y == (self.height - self.height) :
            y = y + 10
        elif y != (self.height - self.label.y):
            y = y-10
        self.label.pos = (200, y)






Single().run()
