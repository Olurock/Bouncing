from kivy._event import __init__
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from Cloud import Cloud


class skyview(App):
    def build(self):
        pass


class CloudCall(Widget):
    clouds =[]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_cloud()
        Clock.schedule_interval(self.update,1/50)
    def create_cloud(self):
        c = Cloud(pos=(100, 100))
        self.add_widget(c)
        if len(self.clouds)==0:
            self.clouds.append(c)
    def move(self):
        pass
    def update(self,dt):
        pass




skyview().run()