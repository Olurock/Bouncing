from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

class PraApp(App):
    def build(self):
        pass
class LayoutExp(BoxLayout):
    chat = StringProperty('0')
    def Chat(self):
        self.chat = 'peter'
    def Calls(self):
        self.chat = 'these are your recent calls'
    def Status(self):
        self.chat = 'new updates'
    def Camera(self):
        self.chat = 'say selfie'
mine = PraApp
mine().run()