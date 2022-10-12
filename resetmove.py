from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.lang.builder import Builder
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


class Resetmove(App):
    def build(self):
        pass


class OurLayout(Widget):
    labelpos = (200,250)
    uppos = (0,500)
    resetpos= (0,250)
    downpos= (0,0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text = 'up',pos = self.uppos,on_press = self.moveup) )
        self.add_widget(Button(text='down',pos = self.downpos, on_press=self.movedown))
        self.add_widget(Button(text='reset', pos=self.resetpos, on_press=self.reset))
        self.label = Label(text='Hello', pos = self.labelpos)
        self.add_widget(self.label)
    def moveup(self, a):
        y = self.label.y

        if y == (self.height - self.label.height) or y == (600):
            pass
        else:
            y = y + 10
        self.label.pos=(200,y)
        #print(self.width)
        #print(self.label.pos)
        #print(self.label.height)
    def movedown(self, a):
        y = self.label.y

        if y == (self.height - self.height):
            pass
        else:
            y = y - 10
        self.label.pos=(200,y)
        #print(self.width)
        #print(self.label.pos)
        #print(self.height)
    def reset(self, a):
        self.label.pos=(200,250)

Resetmove().run()
