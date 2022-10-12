from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from collections import Counter
import mysql.connector

class EmailApp(App):
    def build(self):
        pass

class Mr_Raph(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        error = 'invalid email'
        self.TextInput1= TextInput(pos = ('400','520'),size= ('150','50'), multiline = False)
        self.add_widget(self.TextInput1)
        self.error = Label(pos=('400', '480'), size=('150', '50'))
        self.add_widget(self.error)
        self.TextInput2 = TextInput(pos = ('400','420'),size= ('150','50'), multiline = False)
        self.add_widget(self.TextInput2)
        self.passerror = Label(pos=('400', '380'), size=('150', '50'))
        self.add_widget(self.passerror)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hi"
        )

        mycursor = mydb.cursor()

    def Email(self):
        a = self.TextInput1.text
        count = (Counter(a))
        #if '@' in self.TextInput1.text:
         #   self.error.text = ('')
        #else:
         #   self.error.text = ('Invalid Email')
        if (count['@']) > 1 or self.TextInput1.text[-1] =='@':
            self.error.text = 'Invalid Email'
        else:
            pass
        if self.TextInput1.text[-1] =='@':
            self.error.text = 'invalid email'
        else:
            self.error.text = ''

        if len(self.TextInput2.text) < 8:
            self.passerror.text = ('Password must be a minimum of 8 character')
        else:
            self.passerror.text = ('')

        c = a.split('@')
        d = c[0]
        if c[1] != 'gmail.com':
            self.error.text ='error'
        else:
            pass
        for i in d:
            if i == i.upper() in d:
                self.error.text = 'email cannot contain upper case'
            elif i != i.upper() in d:
                self.error.text = ''


















EmailApp().run()