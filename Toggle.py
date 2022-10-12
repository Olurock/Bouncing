from _testmultiphase import Str
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton


class Tog(App):
    def build(self):
        pass

class MyTogButton(ToggleButton):
    def Launch(self):
        pass
class Widgetexp(BoxLayout):
    show = StringProperty('0')
    enabled = BooleanProperty(True)
    count = 0
    def click(self):
        self.count += 1
        self.show = str(self.count)
    def launch(self,Widget):
        print(str(Widget.state))
        if Widget.state == 'down':
            self.enabled = False
        else:
            self.enabled = True




Tog().run()