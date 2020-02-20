import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from math import *
import random

class calcWindow(Gtk.Window) :
    def __init__(self):
        Gtk.Window.__init__(self,title="Scientific Calculator")
        outerbox = Gtk.Box(spacing=10,orientation = Gtk.Orientation.VERTICAL)
        self.add(outerbox)
        self.entry = Gtk.Entry()
        outerbox.pack_start(self.entry,True,True,0)
        grid = Gtk.Grid()
        outerbox.pack_start(grid,True,True,0)
        button9 = Gtk.Button(label = "9" ) 
        button8 = Gtk.Button(label= "8" ) 
        button7 = Gtk.Button(label="7") 
        delete = Gtk.Button(label="DEL") 
        ac = Gtk.Button(label="AC") 
        button4 = Gtk.Button(label="4") 
        button5 = Gtk.Button(label="5") 
        button6 = Gtk.Button(label="6") 
        multiply = Gtk.Button(label= "*") 
        divide = Gtk.Button(label= "/" ) 
        button1 = Gtk.Button(label= "1" ) 
        button2 = Gtk.Button(label= "2" ) 
        button3 = Gtk.Button(label= "3" ) 
        plus = Gtk.Button(label= "+" ) 
        minus = Gtk.Button(label="-" ) 
        button = Gtk.Button(label= "9" ) 
        ans = Gtk.Button(label= "=" ) 
        dot = Gtk.Button(label="." )
        openbr = Gtk.Button(label="(" )
        closebr = Gtk.Button(label= ")" )
        clear = Gtk.Button(label= "C" )
        root = Gtk.Button(label=" root " )
        fact = Gtk.Button(label="!" )
        sin = Gtk.Button(label="sin" )
        button0 = Gtk.Button(label = "0" )
        cos = Gtk.Button(label="cos" )
        otherbuttons =(divide , plus , minus , multiply )

        for buttonname in otherbuttons:
            buttonname.connect('clicked', self.buttonclicked)
        
        digits=[button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8 ,button9 , button0 , openbr , closebr ]
        for i in digits :
            i.connect('clicked',self.buttonclicked)
        #connecting special buttons
        ans.connect('clicked',self.evaluate)
        #ac.connect('clicked',clear)
        delete.connect('clicked',self.delsingle)
        clear.connect("clicked",self.cleartext)

        root.connect('clicked',self.froot)

        fact.connect('clicked',self.facto)

        sin.connect('clicked',self.sine)
        dot.connect('clicked',self.buttonclicked)

        grid.attach(openbr, 0,0,1,1)
        grid.attach(closebr, 1,0,1,1)
        grid.attach(clear, 2,0,1,1)
        grid.attach(delete, 3,0,1,1)
        grid.attach_next_to(divide,delete,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(multiply,divide,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(plus,multiply,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(minus,plus,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(root,minus,Gtk.PositionType.LEFT,1,1)
        grid.attach_next_to(fact,root,Gtk.PositionType.LEFT,1,1)
        grid.attach(multiply, 3,4,1,1)
        grid.attach(plus, 3,5,1,1)
        grid.attach(minus, 3,6,1,1)
        grid.attach(root, 2,6,1,1)
        grid.attach(fact, 1,6,1,1)
        grid.attach(ans, 0,6,4,1)

        digit=[button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8 ,button9 , button0 ]
        random.shuffle(digit)
        r=1
        c=0
        for button in digit:
            grid.attach(button,c,r,1,1)
            c=(c+1)%3
            if(c==0):
                r=r+1


        # # grid.add(button9)
        # # grid.attach(button8 , 1 , 0 , 1 , 1 )
        # # grid.attach_next_to(button7,button8,Gtk.PositionType.RIGHT,1,1)
        # # grid.attach_next_to(divide,button7,Gtk.PositionType.RIGHT,1,1)
        # # grid.attach_next_to(button6,button9,Gtk.PositionType.BOTTOM,1,1)
        # # grid.attach_next_to ( button5 , button6 ,Gtk.PositionType.RIGHT, 1 , 1 )
        # # grid.attach_next_to ( button4 , button5 ,Gtk.PositionType.RIGHT, 1 , 1 )
        # grid.attach_next_to ( multiply , button4 ,Gtk.PositionType.RIGHT, 1 , 1 )
        # # grid.attach_next_to ( button3 , button6 ,Gtk.PositionType.BOTTOM, 1 , 1 )
        # # grid.attach_next_to ( button2 , button3 ,Gtk.PositionType.RIGHT, 1 , 1 )
        # # grid.attach_next_to ( button1 , button2 ,Gtk.PositionType.RIGHT, 1 , 1 )
        # grid.attach_next_to (minus , button1 ,Gtk.PositionType.RIGHT, 1 , 1 )
        # # grid.attach_next_to ( button0 , button3 ,Gtk.PositionType.BOTTOM, 1 , 1 )
        # grid.attach_next_to ( dot , button0 ,Gtk.PositionType.RIGHT, 1 , 1 )
        # grid.attach_next_to ( root , dot ,Gtk.PositionType.RIGHT, 1 , 1 )
        # grid.attach_next_to ( plus , root ,Gtk.PositionType.RIGHT, 1 , 1 )
        # grid.attach_next_to(openbr,button9 ,Gtk.PositionType.TOP, 1 , 1 )
        # grid.attach_next_to(closebr, button8 ,Gtk.PositionType.TOP, 1 , 1 )
        # grid.attach_next_to(clear, button7 ,Gtk.PositionType.TOP, 1 , 1 )
        # grid.attach_next_to (delete, divide ,Gtk.PositionType.TOP, 1 , 1 )
        # grid.attach_next_to (ans, button0 ,Gtk.PositionType.BOTTOM, 1 , 1 )
        # grid.attach_next_to (fact, root ,Gtk.PositionType.BOTTOM, 1 , 1 )
        # grid.attach_next_to (sin, plus ,Gtk.PositionType.BOTTOM, 1 , 1 )
        # grid.attach_next_to (cos, ans ,Gtk.PositionType.RIGHT, 1 , 1 )

    def buttonclicked(self, button):
        text = self.entry.get_text()
        text = text+button.props.label
        self.entry.set_text(text)

    def cleartext(self, button):
        self.entry.set_text("")

    def evaluate(self, button) :
        eq = self.entry.get_text()
        try:
            self.entry.set_text(str(eval(eq)))
        except:
            self.entry.set_text("ERROR!!!")
    def delsingle(self, button):
        text = self.entry.get_text()
        text=text [: -1]
        self.entry.set_text(text)
    def froot(self,button):
        text = float(self.entry.get_text())
        text=str(sqrt(text))
        self.entry.set_text(text)
    def facto(self,button):
        text = int(self.entry.get_text())
        text=str(factorial(text))
        self.entry.set_text(text)
    def sine(self,button):
        text = float(self.entry.get_text())
        text=str(sin(text))
        self.entry.set_text(text)


calcWindow = calcWindow ()
calcWindow.connect ('destroy',Gtk.main_quit )
calcWindow.show_all()
Gtk.main()