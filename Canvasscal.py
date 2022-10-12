from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class CanvCal(App):
    def build(self):
        pass

class Calculate(BoxLayout):
    show = StringProperty('0')
    def cancalculator(self):
        pass

    def one(self):
            if self.show == '0':
                self.show = '1'
            elif self.show != '0':
                self.show += '1'
            else:
                self.show = 'error'

    def two(self):
        if self.show == '0':
            self.show = '2'
        elif self.show != '0':
            self.show += '2'
        else:
            self.show = 'error'

    def three(self):
        if self.show == '0':
            self.show = '3'
        elif self.show != '0':
            self.show += '3'
        else:
            self.show = 'error'

    def four(self):
        if self.show == '0':
            self.show = '4'
        elif self.show != '0':
            self.show += '4'
        else:
            self.show = 'error'

    def five(self):
        if self.show == '0':
            self.show = '5'
        elif self.show != '0':
            self.show += '5'
        else:
            self.show = 'error'

    def six(self):
        if self.show == '0':
            self.show = '6'
        elif self.show != '0':
            self.show += '6'
        else:
            self.show = 'error'

    def seven(self):
        if self.show == '0':
            self.show = '7'
        elif self.show != '0':
            self.show += '7'
        else:
            self.show = 'error'

    def eight(self):
        if self.show == '0':
            self.show = '8'
        elif self.show != '0':
            self.show += '8'
        else:
            self.show = 'error'

    def nine(self):
        if self.show == '0':
            self.show = '9'
        elif self.show != '0':
            self.show += '9'
        else:
            self.show = 'error'

    def zero(self):
        if self.show == '0':
            self.show = '0'
        elif self.show != '0':
            self.show += '0'
        else:
            self.show = 'error'

    def clear(self):
        if self.show == '0':
            self.show = '0'
        elif self.show != '0':
            self.show = '0'

    def back(self):
        if self.show == '0':
            self.show = '0'
        elif self.show != '0':
            self.show = self.show[0:-1]

    def bracket1(self):
        if self.show == '0':
            self.show = '('
        elif '+' in self.show or '-' in self.show or '/' in self.show:
            self.show += '('
        else:
            self.show += '*('

    def bracket2(self):
        if self.show == '0':
            self.show = ')'
        elif self.show != '0':
            self.show += ')'
        else:
            self.show = 'error'

    def percent(self):
        if self.show == '0':
            self.show = '%'
        elif self.show != '0':
            self.show += '%'
        else:
            self.show = 'error'

    def divide(self):
        if self.show == '0':
            self.show = '/'
        elif self.show != '0':
            self.show += '/'
        else:
            self.show = 'error'

    def multiply(self):
        if self.show == '0':
            self.show = '*'
        elif self.show != '0':
            self.show += '*'
        else:
            self.show = 'error'

    def minus(self):
        if self.show == '0':
            self.show = '-'
        elif self.show != '0':
            self.show += '-'
        else:
            self.show = 'error'

    def plus(self):
        if self.show == '0':
            self.show = '+'
        elif self.show != '0':
            self.show += '+'
        else:
            self.show = 'error'

    def equals_to(self):
        answer = eval(self.show)
        self.show = str(answer)

    def plusminus(self):
        if self.show == '0':
            self.show = ''
        elif self.show != '0':
            self.show += ''

    def dot(self):
        if self.show == '0':
            self.show += '.'
        elif '.' in self.show:
            self.show += ''
        else:
            self.show += '.'

CanvCal().run()