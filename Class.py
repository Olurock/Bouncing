from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget


class Peter(App):
    def build(self):
        pass


class OurLayout(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Layout = GridLayout(cols = 10)
       # Layout.add_widget(Label(text = 'hi'))
        x = 1
        while x <= 10:
            Layout.add_widget(Button(text =str( x)))
            x = x+1

        self.add_widget(Layout)


    def grid(self):
        pass

Peter().run()