from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Horizon(App):
    def build(self):
        pass



class OurLayout(Widget):
    labelpos = (200,200)
    leftpos = (0,0)
    rightpos= (700,0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text = 'right',pos = self.rightpos,on_press = self.moveright) )
        self.add_widget(Button(text='left',pos = self.leftpos, on_press=self.moveleft))
        self.label = Label(text='Hello', pos = self.labelpos)
        self.add_widget(self.label)

    def moveright(self, a):
        x_axis = self.label.x

        if x_axis == (self.width - self.label.width) :
            pass
        else:
            x = x_axis + 10
        self.label.pos = (x, 200)
        print (self.label.x)

    def moveleft(self, a):
        x_axis = self.label.x

        if x_axis == (self.width - self.width) :
            pass
        else:
            x = x_axis - 10
        self.label.pos = (x, 200)


Horizon().run()