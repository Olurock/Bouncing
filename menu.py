import os

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

class Menu(App):
    show = 'p'
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='noteapp',size= (200,300)))
        sm.add_widget(Saved(name='saved'))
        #sm.add_widget(CreateNote(name='new'))
        return sm

class Page(PageLayout):
    pass

class MainScreen(Screen):

    def Exit(self):
        exit(0)
        #App.get_running_app().stop()

class Saved(Screen):
    def Exit(self):
        exit(0)
class WinManager(ScreenManager):
    pass


Menu().run()




