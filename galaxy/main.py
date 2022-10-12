from kivy import Config
Config.set('graphics','width','900')
Config.set('graphics','height','500')

from kivy.app import App
from kivy.graphics import Line, Color
from kivy.properties import NumericProperty, Clock
from kivy.uix.widget import Widget


class Mainwidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    current_offset_y = 0


    speed = 2

    speed_x = 3
    current_speed_x = 0
    current_offset_x = 0

    vertical_lines =[]
    v_NB_lines = 10
    V_lines_spacing = .19#(2 /v_NB_lines)

    horizontal_lines = []
    h_NB_lines = 15
    h_lines_spacing = .1  # (2 /v_NB_lines)


    def on_touch_down(self, touch):
        if touch.x < self.width/2:
            self.current_speed_x -=2
        else:
            self.current_speed_x += 2
            print(2)
    def on_touch_up(self, touch):
        if touch.x < self.width / 2:
            self.current_speed_x = 0
        else:
            self.current_speed_x =0
            print(2)

    def __init__(self,**kwargs):
        super(Mainwidget,self).__init__(**kwargs)
        self.init_vertical_lines()
        self.init_horizontal_lines()
        Clock.schedule_interval(self.update,1/50)
    def on_parent(self,widget,parent):
        pass

    def on_perspective_point_x(self,widget,value):
        #print('x',value)
        pass
    def on_perspective_point_y(self,widget,value):
        #print('y',str(value))
        pass
    def init_vertical_lines(self):
        with self.canvas:
            Color(1,0,0)
            #self.line = Line(points=[100,0,100,100])
            for i in range(0,self.v_NB_lines):
                self.vertical_lines.append( Line())
    def update_vertical_lines(self):
        central_line_x = self.width/2
        #self.line.points=[center_x,0,center_x,100]
        offset = -int(self.v_NB_lines/2)
        spacing = self.V_lines_spacing*self.width
        for i in range (0,self.v_NB_lines):
            line_x = int(central_line_x + offset*spacing+self.current_offset_x)
            x1,y1 = self.transform(line_x,0)
            x2,y2 = self.transform(line_x,self.height)
            self.vertical_lines[i].points=[x1,y1,x2,y2]
            #self.vertical_lines[i].width=(2)
            offset+=1

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1,0,0)
            for i in range(0,self.h_NB_lines):
                self.horizontal_lines.append( Line())
    def update_horizontal_lines(self):
        central_line_x = int(self.width / 2)
        # self.line.points=[center_x,0,center_x,100]
        offset = int(self.v_NB_lines / 2)-1
        spacing = self.V_lines_spacing * self.width
        xmin = central_line_x-offset*spacing+self.current_offset_x
        xmax = central_line_x+offset*spacing+self.current_offset_x
        spacing_y = self.h_lines_spacing * self.height
        for i in range (0,self.h_NB_lines):
            line_y = i*spacing_y-self.current_offset_y
            x1,y1 = self.transform(xmin,line_y)
            x2,y2 = self.transform(xmax,line_y)
            self.horizontal_lines[i].points=[x1,y1,x2,y2]
            #self.vertical_lines[i].width=(2)

    def transform(self,x,y):
        return self.transform_perspective(x,y)
        #return self.transform_2d(x,y)
        pass
    def transform_2d(self,x,y):
        return (x,y)
    def transform_perspective(self,x,y):
        print(self.perspective_point_y)
        lin_y = y * self.perspective_point_y /self.height
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y

        dx = x-self.perspective_point_x
        dy = self.perspective_point_y-lin_y
        factor_y= dy/self.perspective_point_y
        factor_y =factor_y*factor_y*factor_y
        tr_x = self.perspective_point_x + dx*factor_y
        tr_y = self.perspective_point_y-factor_y*self.perspective_point_y
        return (tr_x,tr_y)
    def update(self,dt):

        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset_y += self.speed
        spacing_y = self.h_lines_spacing * self.height
        if self.current_offset_y>=spacing_y:
            self.current_offset_y -= spacing_y

        self.current_offset_x += self.current_speed_x
class Galaxy(App):
    pass


Galaxy().run()