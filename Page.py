
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen


class Pagelay(App):
    def build(self):
        pass

class HomeScreen(Screen):
    def spinner_clicked(self,value):
        self.ids.label.text = value




Pagelay().run()
