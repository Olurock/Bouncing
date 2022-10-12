from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


class Ola(App):
    def build(self):
        pass


class OurLayout(Widget):
    enable = BooleanProperty(True)
    labelpos = (200,200)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text='Hello', pos = self.labelpos)
        self.add_widget(self.label)
    def Moveup(self):
        y = self.label.y
        y = y + 10
        self.label.pos = (200, y)

    def open(self, widget):
        print(widget.state)
        if widget.state == 'down':
            self.enable = False
        else:
            self.enable = True

    def On_Switch_active(self,widget):
        if widget.active == False:
            self.enable = False
        else:
            self.enable = True


Ola().run()