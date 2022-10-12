from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os

from kivy.uix.widget import Widget


class Root(Widget):
    def selected(self,filename):
        try:
            self.ids.image.source=filename[0]
        except:
            pass

class Filechoose(App):
    pass


Filechoose().run()