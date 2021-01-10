import tkinter as tk
import cmath
import math
import threading
import time


#PIL library allows images to be displayed in Tkinter

class ini(tk.Frame):
    def __init__(self, parent, size=100, **options):
        tk.Frame.__init__(self, parent, padx=0, pady=0, borderwidth=0,highlightthickness=0,
                          **options)
        self.size = size
    def to_absolute(self, x, y):
        return x + self.size/2, y + self.size/2
        


class DrawGauge4(ini):
    def __init__(self, parent,
                 max_value: (float, int)=100.0,
                 min_value: (float, int)= 0.0,
                 size: (float, int)=100,
                 img_data: str=None,
                 bg_col:str='blue',unit: str=None,
                 **options):
        super().__init__(parent, size=size, **options)

        self.averaged_value = 0
        self.array = []

        for i in range(50):
            self.array.append(0)

        self.max_value = float(max_value)
        self.min_value = float(min_value)
        self.size = size
        self.bg_col = bg_col
        self.unit = '' if not unit else unit
     
        self.canvas = tk.Canvas(self, width=self.size, height=self.size-self.size/15,bg=bg_col,highlightthickness=0)
        self.canvas.grid(row=0)
        
        self.draw_background1()
        
        t = threading.Thread(target = self.thread_function)
        t.start()

        initial_value = 0.0
        self.set_value(initial_value)
        #self.thread_function()


    def draw_background1(self, divisions=100):
        green_colour = '#00ff00'
        yellow_colour = '#ffff00'
        red_colour = '#ff0000'
        arc_colour2 = 'blue'
        self.canvas.create_arc(self.size/50, self.size/50, self.size-self.size/50, self.size-self.size/50,
                               style="arc",width=self.size/100,start=300, extent=300,
                               outline = green_colour)
        
        self.canvas.create_arc(self.size/50, self.size/50, self.size-self.size/50, self.size-self.size/50,
                               style="arc",width=self.size/100,start=0, extent=60,
                               outline = yellow_colour)
        
        self.canvas.create_arc(self.size/50, self.size/50, self.size-self.size/50, self.size-self.size/50,
                           style="arc",width=self.size/100,start=-60, extent=60,
                           outline = red_colour)
        
        self.canvas.create_arc(self.size/10, self.size/10, self.size-self.size/10, self.size-self.size/10,
                               style="arc",width=self.size/9,start=240, extent = -300,
                               outline = '#666666')

        
       
        label = self.unit
        self.title = self.canvas.create_text(self.size/2,70*self.size/100, font=("Helvetica",int(self.size/25)),fill="white", text=label,angle=0)



    def thread_function(self):
        while True:
            self.write_number(self.averaged_value)
            time.sleep(1)

 
    


    def running_average(self, val: (float,int)):
        n = 50
        total = 0

        for counter in range(n - 1):

            self.array[counter] = self.array[counter + 1]

        self.array[n - 1] = val

        for i in range(n):
        
            total += self.array [i]
       
        average = total/n
    
        return average



    def set_value(self, number: (float, int)):

        number = number if number <= self.max_value else self.max_value
        number = number if number > self.min_value else self.min_value

        self.averaged_value = self.running_average(number)

        self.outer_gauge_val = self.averaged_value/self.max_value * 300
        self.canvas.delete('arc')

        if(self.outer_gauge_val/3 >= 80):
            arc_colour = '#ff0000'

        elif(self.outer_gauge_val/3 >= 60):
            arc_colour = '#ffff00'
        else:
            arc_colour = '#00ad1d'

        
        
        arc = self.canvas.create_arc(self.size/10, self.size/10, self.size-self.size/10, self.size-self.size/10,
                               style="arc",width=self.size/9,start=240, extent = -self.outer_gauge_val,
                               outline = arc_colour, tags = 'arc')
        
       
        
        
    def write_number(self, number: (float, int)):
        self.canvas.delete('readout')
        label = str('%.0f' % number)
        self.readout = self.canvas.create_text(5*self.size/10,4.5*self.size/10, font=("Helvetica",int(self.size/4.5)),fill="white", text=label,angle=0,tags='readout')
        
 

        
    def set_value_no_average(self, number: (float, int)):
        number = number if number <= self.max_value else self.max_value
        number = number if number > self.min_value else self.min_value
        self.outer_gauge_val = number/self.max_value * 300
        self.canvas.delete('arc')
        
        arc_colour = '#66bdff'
        arc_colour2 = 'blue'
        arc = self.canvas.create_arc(self.size/10, self.size/10, self.size-self.size/10, self.size-self.size/10,
                               style="arc",width=self.size/9,start=240, extent = -self.outer_gauge_val,
                               outline = arc_colour, tags = 'arc')
        
        self.write_number(number)
        
        
class Title(ini):
    def __init__(self, parent,
                 size: (float, int)=100,
                 **options):
        super().__init__(parent, size=size, **options)

    
    def write_title(self, title):
                self.canvas.delete('readout')
                label = str(title)
                self.readout = self.canvas.create_text(5*self.size/10,4.5*self.size/10, 
                font=("Helvetica",int(self.size/4.5)),fill="white", 
                text=label,angle=0,tags='readout')
                

    
        

