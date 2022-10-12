from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


class Abiola(App):
    def build(self):
        pass


class OurLayout(Widget):
    labelpos = (200,200)
    downpos = (0,200)
    togpos = (700,200)
    enable = BooleanProperty(True)
    togtexta = 'on'
    togtextb = 'off'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text = 'up',on_press = self.moveup, disabled = not self.enable) )
        self.add_widget(Button(text='down',pos = self.downpos, on_press=self.movedown,disabled = not self.enable))
        self.add_widget(ToggleButton(text=self.togtexta, pos=self.togpos, on_press = self.onstate))
        self.label = Label(text='Hello', pos = self.labelpos)
        self.add_widget(self.label)
    def moveup(self, a):
        y = self.label.y

        if y == (self.height - self.label.height) or y == (600):
            pass
        else:
            y = y + 10
        self.label.pos = (200, y)
    def movedown(self, a):
        y = self.label.y

        if y == (self.height - self.height):
            pass
        else:
            y = y - 10
        self.label.pos = (200, y)
    def onstate(self, widget):
        print(widget.state)
        if widget.state == 'down':
            self.enable = False
        else:
            self.enable = True


Abiola().run()
