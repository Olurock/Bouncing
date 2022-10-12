from random import random, Random

from kivy.app import App
from kivy.core import window
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color, Ellipse, RoundedRectangle
from kivy.metrics import sp, dp
from kivy.properties import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class log(App):
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(FirstPage(name = 'mypage'))
        sm.add_widget(LoginPage(name = 'logpage'))
        sm.add_widget(Signup_page(name='signub'))
        sm.add_widget(Buyer_page(name='Buyerpg'))
        sm.add_widget(Seller_page(name='sellerpg'))
        sm.add_widget(DashBoard(name='dashboard'))
        sm.add_widget(SellProfile(name='sellprofile'))
        sm.add_widget(BuyProfile(name='buyprofile'))
        return sm
class FirstPage(Screen):
    background = None
    layout = None
    def __init__(self,**Kwargs):
        super().__init__(**Kwargs)

        Clock.schedule_interval(self.transistion,1)

    def init_bacground(self):
        self.layout=Widget()
        self.add_widget(self.layout)
        with self.layout.canvas.before:
            Color(.6,.3,.6,1)
            self.background= Rectangle(source = 'oja1.jpg',size=Window.size)

    def title(self):
        with self.canvas:
            text = Label()
            text.text ='OLU MART'
            text.font_name = 'font2.ttf'
            text.color = 1,1,0,1
            text.font_size = 100
            text.pos_hint = {'center_x': .5, 'center_y': .7}
            self.add_widget(text)

    def on_size(self, *args):
        self.init_bacground()
        self.title()
    def on_enter(self, *args):
        self.init_bacground()
        self.title()

    def transistion(self,dt):
        if sm.current == 'mypage':
            sm.current = 'logpage'
        else:
            pass
class LoginPage(Screen):
    bg = None
    layou =None
    def __init__(self,**kw):
        super().__init__(**kw)
    def init_bacground(self,Image):
        with self.canvas:
            Color(.6,.3,.6,1)
            self.bg= Rectangle(source= 'oja1.jpg',size=Window.size)
    def page(self):
        with self.canvas:
            label = Label()
            label.text = 'Gmail'
            label.pos_hint= {'center_x': .43,'center_y': .92}
            self.add_widget(label)
            Gtext = Myinput()
            Gtext.repos(320,470)
            self.add_widget(Gtext)
            label = Label()
            label.text = 'Password'
            label.pos_hint = {'center_x': .45, 'center_y': .7}
            self.add_widget(label)
            Ptext = Myinput()
            Ptext.repos(320,350)
            self.add_widget(Ptext)
            login = Login_Button()
            login.text = 'Login'
            login.pos_hint = {'center_x': .43, 'center_y': .55}
            login.size_hint = .1, .05
            self.add_widget(login)
            Signup_note = Label()
            Signup_note.text = "You don't have an account:"
            Signup_note.pos_hint = {'center_x': .51, 'center_y': .5}
            Signup_note.size_hint = .1, .05
            self.add_widget(Signup_note)
            Signup = Signup_Button()
            Signup.text = 'SignUp'
            Signup.color = (1,0,0,1)
            Signup.pos_hint = {'center_x': .55, 'center_y': .45}
            Signup.size_hint = .1, .05
            self.add_widget(Signup)


    def on_size(self, *args):
        self.init_bacground(Image)
        self.page()
    def on_enter(self, *args):
        self.page()
class DashBoard(Screen):
    images = ['ass1.png','ass2.png','backk.png','bg1.jpg','oja1.jpg','oja2.png','oja3.jpg']
    def background(self):
        with self.canvas:
            Color(.65456531,.28745632445,.73457865725,1)
            back = Rectangle(size = Window.size)
    def page(self):
        filename = None
        a =(Window.size[0]*0.2)
        b = (Window.size[1]*0.2)
        choose_pic = FileChooserIconView()
        choose_pic.on_selection = print(choose_pic.selection)
        self.add_widget(choose_pic)
        pic = picture_Button()
        pic.source = choose_pic.on_selection
        pic.size_hint = (.3,.3)
        pic.pos_hint= {'center_x': .45, 'center_y': .9}
        pic.size = (a,b)
        #self.add_widget(pic)
        layout = GridLayout(rows = 1,spacing = 10,size_hint_x=None)
        layout.pos_hint =  {'center_x': .45, 'center_y': .7}
        layout.bind(minimum_height = layout.setter('width'))
        '''for i in range(50):
            button = Image(source = 'oja3.jpg',size_hint_x = None, size_hint_y = None)
            layout.add_widget(button)

        root = ScrollView(size_hint = (1,None),size = (Window.width,Window.height))
        root.add_widget(layout)
'''
        carousel = Carousel(direction='right')
        carousel.size_hint_y = 0.5
        for i in self.images:
            src = i
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        self.add_widget(carousel)

        back = Back_Button()
        back.background_color = (1, 1, 1, 1)
        back.source = 'baK.png'
        back.pos_hint = {"center_x": .1, "center_y": .9}
        back.size_hint = .06, .06
        self.add_widget(back)





    def on_enter(self, *args):
        self.background()
        self.page()

    def on_size(self, *args):
        self.background()
        self.page()


class Signup_page(Screen):
    bg = None


    def init_background(self):
        with self.canvas:
            Color(rgb=(.4, .3, .5, 1))
            self.bg = Rectangle(source="oja1.jpg",size=Window.size)

    def page(self):
        with self.canvas:
            a = Label(text=" SignUp\n  \n   as")
            a.color = (1, 1, 1, 1)
            a.font_size = sp(30)
            a.pos_hint = {"center_x": .5, "center_y": .7}
            a.font_name = "font1.ttf"
            self.add_widget(a)
            b = Button(text="Buyer")
            b.border =(10,10,10,10)
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
            back = Back_Button()
            back.background_color = (1, 1, 1, 1)
            back.source = 'baK.png'
            back.pos_hint = {"center_x": .1, "center_y": .9}
            back.size_hint = .06, .06
            self.add_widget(back)

    def on_enter(self, *args):
        # self.background()
        self.page()


    def on_size(self, *args):
        self.init_background()
        self.page()

    def seller(self, *args):
        sm.transition.direction = 'left'
        sm.current = 'sellerpg'


    def buyer(self,*args):
        sm.transition.direction = 'left'
        sm.current='Buyerpg'
class Buyer_page(Screen):
    bg = None
    Fname = []
    lname = []
    def init_background(self):
        with self.canvas:
            Color(.6, 0, 1, 1)
            self.background = Rectangle(source='oja3.jpg', size=Window.size)

    def page(self):
        with self.canvas:
            FName = Label(text="First Name")
            FName.color = (1, 1, 1, 1)
            FName.pos_hint = {"center_x": .4, "center_y": .85}
            self.add_widget(FName)
            Ftext = TextInput()
            Ftext.multiline = False
            Ftext.pos_hint = {"center_x": .5, "center_y": .80}
            Ftext.size_hint = .3, .05
            self.add_widget(Ftext)
            LName = Label(text="Other Names")
            LName.color = (1, 1, 1, 1)
            LName.pos_hint = {"center_x": .41, "center_y": .74}
            self.add_widget(LName)
            Ltext = TextInput()
            Ltext.multiline = False
            Ltext.pos_hint = {"center_x": .5, "center_y": .69}
            Ltext.size_hint = .3, .05
            self.add_widget(Ltext)

            Email = Label(text="Email")
            Email.color = (1, 1, 1, 1)
            Email.pos_hint = {"center_x": .38, "center_y": .63}
            self.add_widget(Email)
            Etext= TextInput()
            Etext.multiline = False
            Etext.pos_hint = {"center_x": .5, "center_y": .58}
            Etext.size_hint = .3, .05
            self.add_widget(Etext)
            Username = Label(text="Username")
            Username.color = (1, 1, 1, 1)
            Username.pos_hint = {"center_x": .4, "center_y": .52}
            self.add_widget(Username)
            Utext = TextInput()
            Utext.multiline = False
            Utext.pos_hint = {"center_x": .5, "center_y": .47}
            Utext.size_hint = .3, .05
            self.add_widget(Utext)
            Password = Label(text="Enter Password")
            Password.color = (1, 1, 1, 1)
            Password.pos_hint = {"center_x": .42, "center_y": .41}
            self.add_widget(Password)
            Ptext = TextInput()
            Ptext.multiline = False
            Ptext.pos_hint = {"center_x": .5, "center_y": .36}
            Ptext.size_hint = .3, .05
            self.add_widget(Ptext)
            CPassword = Label(text="Enter Password Again")
            CPassword.color = (1, 1, 1, 1)
            CPassword.pos_hint = {"center_x": .44, "center_y": .3}
            self.add_widget(CPassword)
            Ctext = TextInput()
            Ctext.multiline = False
            Ctext.pos_hint = {"center_x": .5, "center_y": .25}
            Ctext.size_hint = .3, .05
            self.add_widget(Ctext)
            register = BRegister_Button()
            register.text = 'register'
            register.pos_hint = {"right": 0.7, "center_y": .1}
            register.size_hint = .06, .06
            self.add_widget(register)
            back = Back_Button()
            back.background_color = (1,1,1,1)
            back.source = 'baK.png'
            back.pos_hint = {"center_x": .1, "center_y": .9}
            back.size_hint = .06, .06
            self.add_widget(back)

    def on_enter(self, *args):
        # self.background()
        self.page()

    def on_size(self, *args):
        self.init_background()
        self.page()
class Seller_page(Screen):
    bg = None
    Ftext =None

    def init_background(self):
        with self.canvas:
            Color(.6, 0, 1, 1)
            self.background = Rectangle(source='oja3.jpg', size=Window.size)

    def page(self):
        self.FName = Label(text="First Name")
        self.FName.color = (1, 1, 1, 1)
        self.FName.pos_hint = {"center_x": .4, "center_y": .85}
        self.add_widget(self.FName)
        Ftext = Myinput()
        self.add_widget(Ftext)
        LName = Label(text="Other Names")
        LName.color = (1, 1, 1, 1)
        LName.pos_hint = {"center_x": .41, "center_y": .74}
        self.add_widget(LName)
        Ltext = TextInput()
        Ltext.multiline = False
        Ltext.pos_hint = {"center_x": .5, "center_y": .69}
        Ltext.size_hint = .3, .05
        self.add_widget(Ltext)

        Email = Label(text="Email")
        Email.color = (1, 1, 1, 1)
        Email.pos_hint = {"center_x": .38, "center_y": .63}
        self.add_widget(Email)
        Etext= TextInput()
        Etext.multiline = False
        Etext.pos_hint = {"center_x": .5, "center_y": .58}
        Etext.size_hint = .3, .05
        self.add_widget(Etext)
        Username = Label(text="Username")
        Username.color = (1, 1, 1, 1)
        Username.pos_hint = {"center_x": .4, "center_y": .52}
        self.add_widget(Username)
        Utext = TextInput()
        Utext.multiline = False
        Utext.pos_hint = {"center_x": .5, "center_y": .47}
        Utext.size_hint = .3, .05
        self.add_widget(Utext)
        Password = Label(text="Enter Password")
        Password.color = (1, 1, 1, 1)
        Password.pos_hint = {"center_x": .42, "center_y": .41}
        self.add_widget(Password)
        Ptext = TextInput()
        Ptext.multiline = False
        Ptext.pos_hint = {"center_x": .5, "center_y": .36}
        Ptext.size_hint = .3, .05
        self.add_widget(Ptext)
        CPassword = Label(text="Enter Password Again")
        CPassword.color = (1, 1, 1, 1)
        CPassword.pos_hint = {"center_x": .44, "center_y": .3}
        self.add_widget(CPassword)
        Ctext = TextInput()
        Ctext.multiline = False
        Ctext.pos_hint = {"center_x": .5, "center_y": .25}
        Ctext.size_hint = .3, .05
        self.add_widget(Ctext)
        register = SRegister_Button()
        register.text = 'register'
        register.pos_hint = {"right": 0.63, "center_y": .2}
        register.size_hint = .06, .06
        self.add_widget(register)
        back = Back_Button()
        back.background_color = (1, 1, 1, 1)
        back.source = 'baK.png'
        back.pos_hint = {"center_x": .1, "center_y": .9}
        back.size_hint = .06, .06
        self.add_widget(back)

    def buyer_name(self):
        pass

    def on_enter(self, *args):
        # self.background()
        self.page()

    def on_size(self, *args):
        self.init_background()
        self.page()
class SellProfile(Screen):
    def init_background(self):
        with self.canvas:
            Color(.6, 0.6, 1, 1)
            self.background = Rectangle(source='oja3.jpg', size=Window.size)

    def page(self):
        Email = Label(text="Email")
        Email.color = (1, 1, 1, 1)
        Email.pos_hint = {"center_x": .38, "center_y": .58}
        self.add_widget(Email)
        Etext = TextInput()
        Etext.multiline = False
        Etext.pos_hint = {"center_x": .5, "center_y": .53}
        Etext.size_hint = .3, .05
        self.add_widget(Etext)
        Username = Label(text="Username")
        Username.color = (1, 1, 1, 1)
        Username.pos_hint = {"center_x": .4, "center_y": .47}
        self.add_widget(Username)
        Utext = TextInput()
        Utext.multiline = False
        Utext.pos_hint = {"center_x": .5, "center_y": .42}
        Utext.size_hint = .3, .05
        self.add_widget(Utext)
        Password = Label(text="Enter Password")
        Password.color = (1, 1, 1, 1)
        Password.pos_hint = {"center_x": .42, "center_y": .36}
        self.add_widget(Password)
        Ptext = TextInput()
        Ptext.multiline = False
        Ptext.pos_hint = {"center_x": .5, "center_y": .31}
        Ptext.size_hint = .3, .05
        self.add_widget(Ptext)
        CPassword = Label(text="Enter Password Again")
        CPassword.color = (1, 1, 1, 1)
        CPassword.pos_hint = {"center_x": .44, "center_y": .25}
        self.add_widget(CPassword)
        Ctext = TextInput()
        Ctext.multiline = False
        Ctext.pos_hint = {"center_x": .5, "center_y": .2}
        Ctext.size_hint = .3, .05
        self.add_widget(Ctext)

    def on_enter(self, *args):
        # self.background()
        self.page()
        self.profile_picture()
    def on_size(self, *args):
        self.init_background()
        self.page()
        self.profile_picture()
class BuyProfile(Screen):
    def init_background(self):
        with self.canvas:
            Color(.6, 0.6, 1, 1)
            self.background = Rectangle(source='oja3.jpg', size=Window.size)
    def page(self):
        Email = Label(text="Email")
        Email.color = (1, 1, 1, 1)
        Email.pos_hint = {"center_x": .38, "center_y": .58}
        self.add_widget(Email)
        Etext = TextInput()
        Etext.multiline = False
        Etext.pos_hint = {"center_x": .5, "center_y": .53}
        Etext.size_hint = .3, .05
        self.add_widget(Etext)
        Username = Label(text="Username")
        Username.color = (1, 1, 1, 1)
        Username.pos_hint = {"center_x": .4, "center_y": .47}
        self.add_widget(Username)
        Utext = TextInput()
        Utext.multiline = False
        Utext.pos_hint = {"center_x": .5, "center_y": .42}
        Utext.size_hint = .3, .05
        self.add_widget(Utext)
        Password = Label(text="Enter Password")
        Password.color = (1, 1, 1, 1)
        Password.pos_hint = {"center_x": .42, "center_y": .36}
        self.add_widget(Password)
        Ptext = TextInput()
        Ptext.multiline = False
        Ptext.pos_hint = {"center_x": .5, "center_y": .31}
        Ptext.size_hint = .3, .05
        self.add_widget(Ptext)
        CPassword = Label(text="Enter Password Again")
        CPassword.color = (1, 1, 1, 1)
        CPassword.pos_hint = {"center_x": .44, "center_y": .25}
        self.add_widget(CPassword)
        Ctext = TextInput()
        Ctext.multiline = False
        Ctext.pos_hint = {"center_x": .5, "center_y": .2}
        Ctext.size_hint = .3, .05
        self.add_widget(Ctext)
    def on_enter(self, *args):
        # self.background()
        self.page()

    def on_size(self, *args):
        self.init_background()
        self.page()



class SRegister_Button(ButtonBehavior,Label):
    def on_press(self):
        Seller_page().buyer_name()
        sm.current='sellprofile'
class BRegister_Button(ButtonBehavior,Label):
    def on_press(self):
        Seller_page().buyer_name()
        sm.current='buyprofile'
class Signup_Button(ButtonBehavior,Label):
    def on_press(self):
        sm.transition.direction = 'left'
        sm.current = 'signub'
class Login_Button(ButtonBehavior,Label):
    def on_press(self):
        sm.transition.direction = 'left'
        sm.current = 'dashboard'
class Back_Button(ButtonBehavior,Image):
    def on_press(self):
        if sm.current == 'signub':
            sm.transition.direction = 'right'
            sm.current='logpage'
        if sm.current == 'Buyerpg':
            sm.transition.direction = 'right'
            sm.current = 'signub'
        if sm.current == 'sellerpg':
            sm.transition.direction = 'right'
            sm.current='signub'
        if sm.current == 'dashboard':
            sm.transition.direction = 'right'
            sm.current = 'logpage'
class picture_Button(ButtonBehavior,Image):
    def on_press(self):
        print(11)

class Myinput(Widget):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rectangle()
        self.text()



    def rectangle(self):
        x,y=Window.size
        self.rect = RoundedRectangle()
        self.rect.size = ((x*0.2),dp(y*0.09))
        self.rect.pos = (self.width, self.height)


    def text(self):

        self.input=TextInput(multiline = False)
        x,y= self.rect.pos
        self.input.pos = ((x+5),(y+5))
        w,h = self.rect.size
        self.input.size= ((w-10),(h-10))
        self.add_widget(self.input)

    def repos(self,x,y):
        self.rect.pos = (x,y)
        self.input.pos = ((x+5),(y+5))
    def on_size(self, *args):
        self.rectangle()
        self.text()

    #def pos_hint(self,**kwargs):
     #   pass



log().run()