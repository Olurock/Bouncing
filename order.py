from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget


class Order(App):
    pass

class pop(Popup):
    pass

class MainWidget(BoxLayout):
    Show = StringProperty('')

    def validate_textinput(self):
        self.Show=self.ids.myord.text




Order().run()