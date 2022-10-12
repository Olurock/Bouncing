from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget


class ImageApp(App):
    def build(self):
        pass

class ImageExp(BoxLayout):
    pass

ImageApp().run()

'''

BoxLayout:
            size_hint: 1,.4
            pos_hint:{'x':1,'center_y': .5}
            BoxLayout:
                background_color: 1,0,0
                RelativeLayout:
                    canvas:
                        Color:
                            rgb: 1, 1, 1
                        Ellipse:
                            source: 'ass1.png'
                            angle_start: 0
                            angle_end: 360
                            size:self.size
        BoxLayout:
            size_hint: 1,.4
            pos_hint:{'x':1,'center_y': .5}
            RelativeLayout:
                canvas:
                    Color:
                        rgb: 1, 1, 1
                    Ellipse:
                        source: 'bg1.jpg'
                        angle_start: 0
                        angle_end: 360
                        size:self.size
        BoxLayout:
            size_hint: 1,.4
            pos_hint:{'x':1,'center_y': .5}
            RelativeLayout:
                canvas:
                    Color:
                        rgb: 1, 1, 1
                    Ellipse:
                        source: 'ass1.png'
                        angle_start: 0
                        angle_end: 360
                        size:self.size
'''