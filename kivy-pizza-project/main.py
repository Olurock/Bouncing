from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import CoverBehavior

from models import Pizza

class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 cheeses", "mozarella, emmental, brie, blue cheese", 9.5, True),
            Pizza("Chorizo", "tomato, chorizo, cheese", 11.2, False),
            Pizza("Calzone", "cheese, ham, mushrooms", 10, False)
        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [pizza.get_dictionary() for pizza in self.pizzas]


class PizzaApp(App):
    def build(self):
        pass


PizzaApp().run()
