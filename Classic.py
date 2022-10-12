from kivy.app import App
from kivy.core import window
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from collections import Counter
import mysql.connector

class Classic(App):
    def build(self):
        pass


class Mr_Raph(BoxLayout):
    point_x = NumericProperty(0)
    point_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Mr_Raph,self).__init__(**kwargs)
        with self.canvas.before:
            Color(.1,0,.3,1)
            Rectangle(size=(5000,5000))

            #self.TextInput1= Label(pos = ('400','520'),size= ('150','50'),text='Classic\nCourses and Programs fron the best university in the world')
            #self.add_widget(self.TextInput1)
            #self.HEAD = Label(pos=('400', '480'), size=('150', '50'),text= 'WHAT DO YOU WANT TO LEARN')
            #self.add_widget(self.HEAD)
            #self.TextInput2 = TextInput(pos = (self.point_x,self.point_y),size= ('150','50'), multiline = False)
            #self.add_widget(self.TextInput2)




Classic().run()