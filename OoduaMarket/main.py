from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.metrics import sp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget



class SplashScreen(Screen):
    layout = None
    background = None

    def __init__(self, **kw):
        super().__init__(**kw)

    def init_background(self):
        self.layout = Widget()
        self.add_widget(self.layout)
        with self.layout.canvas.before:
            self.background = Rectangle(size=Window.size)

    def title(self):
        with self.canvas.after:
            l = Label(text="Oja Oodua")
            l.color = (1, 0, 0, 1)
            l.font_size = sp(45)
            l.font_name = "fonts/a.ttf"
            self.add_widget(l)

    def on_enter(self, *args):
        Clock.schedule_interval(self.move, 4)
        self.init_background()
        self.title()
        # print("on Enter:" + str(self.width))

    def on_size(self, *args):
        self.init_background()

    def on_parent(self, *args):
        pass  # print("on Enter:" + str(self.width))

    def move(self, dt):
        sm.current = "login"
        # pass

class Login(Screen):
    bg = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.init_background()

    def init_background(self):
        with self.canvas:
            Color(rgb=(0, 0, 1, 1))
            self.bg = Rectangle(size=Window.size)

    def page(self):
        with self.canvas:
            a = Label(text=" SignUp\n  \n   as")
            a.color = (1, 1, 1, 1)
            a.font_size = sp(30)
            a.pos_hint = {"center_x": .5, "center_y": .7}
            a.font_name = "fonts/a.ttf"
            self.add_widget(a)
            b = Button(text="Buyer")
            b.size_hint = (.3, .1)
            b.pos_hint = {"center_x": .5, "center_y": .5}
            b.bind(on_press=self.buyer)
            b.background_color = (0,.7,0,1)
            b.background_down = "red"
            self.add_widget(b)
            s = Button(text="Seller")
            s.size_hint = (.3, .1)
            s.background_color = (1,0,0,1)
            s.background_down = "red"
            s.bind(on_press=self.seller)
            s.pos_hint = {"center_x": .5, "center_y": .3}
            self.add_widget(s)

    def on_enter(self, *args):
        # self.background()
        self.page()

    def on_size(self, *args):
        self.init_background()
        self.page()

    def seller(self, *args):
        sm.current = "home"

    def buyer(self,*args):
        print("buyers")

class Home(Screen):
    bgd = None

    def __init__(self, **kw):
        super().__init__(**kw)

    def init_background(self):
        with self.canvas:
            Color(rgb=(0, 0, 1, 0))
            self.bgd = Rectangle(size=Window.size)

    def on_enter(self, *args):
        self.init_background()

    def page(self):
        with self.canvas:
            c = Label(text="Login")
            c.color = (1, 1, 1, 1)
            c.pos_hint = {"center_x": .4, "center_y": .85}
            self.add_widget(c)
            d = TextInput()
            d.size_hint = (.3, .1)
            d.pos_hint = {"center_x": .5, "center_y": .78}
            self.add_widget(d)
            e = Label(text="Password")
            e.size_hint = (.3, .1)
            e.pos_hint = {"center_x": .4, "center_y": .7}
            self.add_widget(e)
            f = TextInput()
            f.size_hint = (.3, .1)
            f.pos_hint = {"center_x": .5, "center_y": .6}
            self.add_widget(f)
            g = Button(text = "login")
            g.size_hint = (.1,.05)
            g.pos_hint = {"center_x": .5, "center_y": .5}
            self.add_widget(g)
            h = Button(text="signup")
            h.size_hint = (.1, .05)
            h.pos_hint = {"center_x": .73, "center_y": .4}
            self.add_widget(h)
            i = Label(text="For those who don\'t have an account here click on the")
            i.size_hint = (.3, .1)
            i.pos_hint = {"x": .3, "center_y": .4}
            self.add_widget(i)

    def on_enter(self, *args):
        # self.background()
        self.page()


class OoduaMarket(App):

    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="Splash"))
        sm.add_widget(Login(name="login"))
        sm.add_widget(Home(name="home"))

        return sm


if __name__ == '__main__':
    OoduaMarket().run()




