from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class PlayIndicatorButton(ToggleButton):
    pass


class PlayIndicatorWidget(BoxLayout):
    buttons = []
    nb_steps = 0
    left_align = NumericProperty(0)

    def set_current_step_index(self, index):
        if index >= len(self.buttons):
            return

        for i in range(0, len(self.buttons)):
            button = self.buttons[i]
            if i == index:
                button.state = "down"
            else:
                button.state = "normal"

    def set_nb_steps(self, nb_steps):
        if not nb_steps == self.nb_steps:
            # reconstuct my layout -> add the buttons
            self.nb_steps = nb_steps
            self.clear_widgets()

            dummy_button = Button()
            dummy_button.size_hint_x = None
            dummy_button.width = self.left_align
            dummy_button.disabled = True
            self.add_widget(dummy_button)

            self.buttons = []
            for i in range(0, nb_steps):
                button = PlayIndicatorButton()
                self.buttons.append(button)
                button.background_color = (0.5, 0.5, 1.0, 1.0)
                button.background_disabled_down = ''
                button.disabled = True
                #if i == 0:
                #    button.state = "down"
                self.add_widget(button)


# nb_steps
# current_step_index
# layout offset on the left


