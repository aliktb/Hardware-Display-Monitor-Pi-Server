import tkinter as tk
import gaugelib
from PIL import Image, ImageTk
from tkinter import PhotoImage


class DrawPicture(gaugelib.ini):
    def __init__(self, parent,
                 size: (float, int)=100,
                 img_data: str=None,
                 bg_col:str='blue',unit: str=None,bg_sel=1,
                 **options):
        super().__init__(parent, size=size, **options)

        self.size = size
        self.bg_col = bg_col
        self.unit = '' if not unit else unit
        self.canvas = tk.Canvas(self, width=self.size, height=self.size,bg=bg_col,highlightthickness=0)
        self.canvas.grid(row=0)
        self.bg_sel = bg_sel
    
        
     
    def draw_picture(self, validate):
        
        
        if validate == 1:

            self.canvas.delete('pic')
            label= self.unit
            self.img = ImageTk.PhotoImage(Image.open(label))
            pic = self.canvas.create_image(self.size/2,self.size/2,image=self.img,tags = 'pic')
            self.canvas.image = pic
            
            
        elif validate == 0:
            self.canvas.delete('pic')

class DrawPicture_1024(gaugelib.ini):
    def __init__(self, parent,
                 size,
                 img_data: str=None,
                 bg_col:str='blue',unit: str=None,bg_sel=1,
                 **options):
        super().__init__(parent, size=size, **options)

        self.size = size
        self.bg_col = bg_col
        self.unit = '' if not unit else unit
        self.canvas = tk.Canvas(self, width=self.size, height=self.size*0.586,bg=bg_col,highlightthickness=0)
        self.canvas.grid(row=0)
        self.bg_sel = bg_sel
    
        
     
    def draw_picture(self, validate):
        
        
        if validate == 1:
            
            label= self.unit
            self.img = ImageTk.PhotoImage(Image.open(label))
            pic = self.canvas.create_image(self.size/2,self.size/3.4,image=self.img,tags = 'pic')
            self.canvas.image = self.img
            
            
        elif validate == 0:
            self.canvas.delete('pic')

class DrawPicture_bg(gaugelib.ini):
    def __init__(self, parent,
                 size: (float, int)=100,
                 img_data: str=None,
                 bg_col:str='blue', background_pic: str=None,foreground_pic: str=None,bg_sel=1,
                 **options):
        super().__init__(parent, size=size, **options)

        self.size = size
        self.bg_col = bg_col
        self.foreground_pic = '' if not foreground_pic else foreground_pic
        self.background_pic = '' if not background_pic else background_pic
        self.canvas = tk.Canvas(self, width=self.size, height=self.size,bg=bg_col,highlightthickness=0)
        self.canvas.grid(row=0)
        self.bg_sel = bg_sel
    
    def draw_picture(self, validate):    
        backg = self.background_pic
        label = self.foreground_pic
        if validate == 1:

            self.canvas.delete('pic')
            self.img = ImageTk.PhotoImage(Image.open(label))
            pic = self.canvas.create_image(self.size / 2, self.size / 2, image=self.img, tags='pic')
            self.canvas.image = pic
            
            
        elif validate == 0:
            self.canvas.delete('pic')
            self.img = ImageTk.PhotoImage(Image.open(backg))
            pic = self.canvas.create_image(self.size / 2, self.size / 2, image=self.img, tags='pic')
            self.canvas.image = pic
     
