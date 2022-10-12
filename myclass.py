from _testmultiphase import Str
from kivy import clock
from kivy.app import App
from kivy.graphics import Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class Myclass(App):
    def build(self):
        pass
class CanvasExp5(BoxLayout):
    pass
class CanvasExp4(Widget):
    pass
class CanvasExp3(Widget):
    dx = 3
    dy = 4
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bsize= dp(20)
        with self.canvas:
            self.ball = Ellipse(pos=(100,100),size=(self.bsize,self.bsize))
            Clock.schedule_interval(self.Update,1/1000)

    def on_size(self,*args):
        self.ball.pos= (self.center_x-self.bsize/2,self.center_y-self.bsize/2)
    def Update(self,dt):
        x, y = self.ball.pos
        x = x+self.dx
        y = y+self.dy
        if (y+self.bsize >= self.height):
            self.dy = -self.dy

        if (x+self.bsize >= self.width):
            self.dx =-self.dx
        if x <= 0:
            self.dx = -self.dx
        if y <= 0:
            self.dy =-self.dy

        self.ball.pos=x,y




class CanvasExp2(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(pos=(100,100),size=(100,20))
    def press_but(self):
        x, y = self.rect.pos
        w,h = self.rect.size
        if x >= self.width-w:
            pass
        else:
            x += dp(10)
            self.rect.pos = (x, y)
class CanvasExp1(Widget):
    pass

class ImageExp(GridLayout):
    pass
class WidgetExp(GridLayout):
    slider_text=StringProperty('')
    text = StringProperty('0')
    count = 1
    enabled= BooleanProperty(False)
    enable = BooleanProperty(False)
    text_input = StringProperty('')
    def button_click(self,widget):
        if self.enabled == True:
            self.count = self.count+1
            self.text = str(self.count)
    def togglebutton_click(self,Toggle):
        if Toggle.state =='down':
            Toggle.text ='ON'
            self.enabled = True
        else:
            Toggle.text = 'OFF'
            self.enabled = False
    def switch_click(self,widget):
     #   if widget.active == 'True':
      #      self.enable = False
       # if widget.active == 'False':
        #    self.enable = True
        pass
    #def slider_value(self,widget):
        #self.slider_text=str(int(widget.value))
        #pass

    def validate_textinput(self,widget):
        self.text_input = widget.text

class MainWidget(BoxLayout):
    def LayoutExp(self):
        pass
class AnchorLayoutExp(AnchorLayout):
    def anchor(self):
        pass
class StackLayoutExp(StackLayout):
    def __init__(self,**Kwargs):
        super().__init__(**Kwargs)
        for i in range(0,100):
            b = Button(size_hint=(.2,None),height=(100),text=Str(i))
            self.add_widget(b)


Myclass().run()