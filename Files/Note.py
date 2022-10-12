import os

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager


class NoteApp(App):
    show = 'p'
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='noteapp'))
        sm.add_widget(SavedNote(name='saved'))
        sm.add_widget(CreateNote(name='new'))
        return sm

class MainScreen(Screen):
    def Exit(self):
        exit(0)
        #App.get_running_app().stop()
class SavedNote(Screen):
    show = StringProperty()
    def view(self):
        list = os.listdir("C:\\Users\\OLUROCK\\PycharmProjects\\pythonProject\\Files")
        for i in list :
            print(i)


    def delete(self):
        self.show = ''
    def edit(self):
        pass

class CreateNote(Screen):
    def save(self):
        file = open("Files/"+self.ids.Title.text,'w+')
        path = 'C:\\Users\\OLUROCK\\PycharmProjects\\pythonProject\\Files'
        os.chdir(path)
        os.path.join('path', 'file')




NoteApp().run()