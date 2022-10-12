from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition


class ScreenApp(App):
    def build(self):
        sm=ScreenManager(transition=FadeTransition())
        sm.add_widget(MainScreen(name='MENU'))
        sm.add_widget(DashboardScreen(name='MYDASH'))
        return sm
class MainScreen(Screen):
    pass
class DashboardScreen(Screen):
    pass



ScreenApp().run()

