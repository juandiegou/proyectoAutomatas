#!/usr/bin/env python
"""Hello World, but with more meat."""
import wx
import pygame
import os.path 
from time import sleep
from automata.autom import automata
from automata.graphic import controller
from PIL import Image as im
import time as t


pygame.init()

class Frame(wx.Frame):
    reader,pnl,ruta,img,autom,control=None,None,None,None,None,None
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(Frame, self).__init__(*args, **kw)
        #sonido
        pygame.mixer_music.load("C:/Users/juand/Desktop/proyecto automatas1/src/kiss.mp3")
        pygame.mixer.music.play(-1)
        self.encender(wx.EvtHandler())
        # create a panel in the frame
        self.pnl = wx.Panel(self, 0,pos=(0,0),size=(1200,745))
        self.pnl.SetBackgroundColour('WHITE')
        #self.pintura(wx.EVT_PAINT,pnl)
        pnl2 = wx.Panel(self,0,pos=(1201,0), size=(180,745))
        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.pnl.SetSizer(sizer)
        pnl2.SetSizer(sizer2)
        # create a menu bar
        self.makeMenuBar()
        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Automatas!")
        #crear botonera
        self.crearBotonera(pnl2)

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """
        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        openfile = fileMenu.Append(-1, "&Open File...\tCtrl-o",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)
        ####musica
        ctrlM =wx.Menu()
        ctrlM.AppendSeparator()
        optionsOn= ctrlM.AppendRadioItem(0,"on")
        optionsOff= ctrlM.AppendRadioItem(1,"off")
        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        #Drawing place
        pintar=wx.Menu()
        pp=pintar.Append(2,"Paso a Paso")
        p=pintar.Append(3,"Pintar Automata")
        l=pintar.Append(4,"limpiar")
        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(ctrlM, "&Audio")
        menuBar.Append(pintar,"&Pintar")
        menuBar.Append(helpMenu, "&Help")
        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)
        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.Openfile, openfile)
        self.Bind(wx.EVT_MENU, self.encender, optionsOn)
        self.Bind(wx.EVT_MENU, self.apagar, optionsOff)
        self.Bind(wx.EVT_MENU,self.pintura,p)
        self.Bind(wx.EVT_MENU,self.paint,pp)
        self.Bind(wx.EVT_MENU,self.clean,l)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def encender(self,event):
        pygame.mixer_music.play(-1)
       

    def apagar(self,event):
        pygame.mixer_music.stop()
      
    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)
        e.skip()

    def Openfile(self, event):
        wildcard = "Python source (*.py; *.pyc)|*.py;*.pyc|" "All files (*.*)|*.*"
        dlg = wx.FileDialog(self, message="Select your file",defaultDir=os.getcwd(),defaultFile="*.*", wildcard=wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            picfile = dlg.GetFilename()
            self.ruta= dlg.GetPath()
            #dlg.GetFilename()
            #self.reader=Lector(self.ruta)
            self.autom=automata(self.ruta)

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("About: make for Juan Diego Gallego G \n& Simón Muñoz O",
                    "This is a automata that autosolve",
                     wx.OK|wx.ICON_INFORMATION)

    def pintura(self,e):
        r=2
        if r!=None:
            ig=im.open("src\imgs\Full automata.png")
            ig=ig.resize((1200,670),im.ANTIALIAS)
            ig.save("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/Full automata.png",optimize=True,quality=900)
            w=wx.Bitmap("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/Full automata.png",wx.BITMAP_TYPE_ANY)
            dibujo=wx.ClientDC(self.pnl)  
            dibujo.Clear()
            dibujo.DrawBitmap(w,x=0,y=0,useMask=False)
        else:
            dibujo=wx.ClientDC(self.pnl)
            x,y,tm,i=10,10,4,0
            dibujo.SetPen(wx.Pen('BLACK',tm))
            while i<50:
                dibujo.DrawRectangle(0,0,1200,745)
                dibujo.DrawText('No se ha cargado un JSON',x+i*5,y+i*5)
                t.sleep(0.1)
                dibujo.SetPen(wx.Pen('RED',tm+i*7))
                i+=1
            dibujo.Clear()

    def generar(self,event):
        #self.controler=controlador()
        if self.ruta is None:
            self.Openfile(event)  
        r=wx.MessageBox("Desea Mostrar el automata",
            "generar automata",
            wx.YES |wx.NO )
        if r==2:
            self.pintura(event)

    def clean(self,e):
        t=self.pnl.GetChildren()
        for x in t:
            x.Destroy()
        dibujo=wx.ClientDC(self.pnl)  
        dibujo.SetBackground(wx.WHITE_BRUSH)          
        dibujo.Clear()
       
    def crearBotonera(self,panel2):
        panel2.SetBackgroundColour('LIGHT GREY')
        botonG = wx.Button(panel2,-1,"Generar",pos=(10,70),size=(140,70))
        botonG.Bind(wx.EVT_BUTTON , self.generar)
        botonMA= wx.Button(panel2,-1,"Mostrar solucion", pos=(10,170), size=(140,70))
        botonMA.Bind(wx.EVT_BUTTON , self.draw)
        self.img=wx.StaticBitmap(panel2,wx.ID_ANY,
        wx.Bitmap("C:/Users/juand/Desktop/proyecto automatas1/src/img.png",wx.BITMAP_TYPE_ANY),
        pos=(10,470),size=(140,200))

        #creacion de eventos de cada caja de texto por un boton
        #boton1  

    def draw(self,e):
        if self.autom is not None:
            g=self.autom.get_transversal()
            self.autom.genera_camino()
            dibujo=wx.ClientDC(self.pnl)  
            dibujo.SetBackground(wx.WHITE_BRUSH)          
            dibujo.Clear()
            bitmap=wx.Bitmap("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/Shortest traversal.png",wx.BITMAP_TYPE_PNG)
            if bitmap.Width>1200:
                from PIL import Image
                ig=im.open("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/Shortest traversal.png")
                ig=ig.resize((1200,200),im.ANTIALIAS)
                ig.save("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/Shortest traversal.png",optimize=True,quality=900)
                w=wx.Bitmap("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/Shortest traversal.png",wx.BITMAP_TYPE_ANY)
                bitmap=w
            dibujo.DrawBitmap(bitmap,x=0,y=100,useMask=True)
        
        else:
            dibujo=wx.ClientDC(self.pnl)
            x,y,tm,i=10,10,4,0
            dibujo.SetPen(wx.Pen('BLACK',tm))
            while i<50:
                dibujo.DrawRectangle(0,0,1200,745)
                dibujo.DrawText('No se ha generado una respuesta',x+i*5,y+i*5)
                t.sleep(0.1)
                dibujo.SetPen(wx.Pen('RED',tm+i*7))
                i+=1
            dibujo.Clear()

    def delay(self):
        sleep(5)



    def paint(self,e):
        if self.autom is not None:
            g=self.autom.get_transversal()
            self.autom.genera_paso_a_paso()
            dibujo=wx.ClientDC(self.pnl)  
            dibujo.SetBackground(wx.WHITE_BRUSH)          
            for x in range(len(g)-1):
                dibujo.Clear()
                nombre="img"+str(x)
                bitmap=wx.Bitmap("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/"+nombre+'.png',wx.BITMAP_TYPE_PNG)
                if bitmap.Width>1200:
                    print(bitmap.Width)
                    print(bitmap.Height)
                    from PIL import Image
                    ig=im.open("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/"+nombre+'.png')
                    ig=ig.resize((1200,200),im.ANTIALIAS)
                    ig.save("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/"+nombre+'.png',optimize=True,quality=900)
                    w=wx.Bitmap("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/"+nombre+'.png',wx.BITMAP_TYPE_ANY)
                    bitmap=w
                dibujo.DrawBitmap(bitmap,x=0,y=200,useMask=True)
                self.delay()      
        else:
            dibujo=wx.ClientDC(self.pnl)
            x,y,tm,i=10,10,4,0
            dibujo.SetPen(wx.Pen('BLACK',tm))
            while i<50:
                dibujo.DrawRectangle(0,0,1200,745)
                dibujo.DrawText('No se ha generado una respuesta',x+i*5,y+i*5)
                t.sleep(0.1)
                dibujo.SetPen(wx.Pen('RED',tm+i*7))
                i+=1
            dibujo.Clear()


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    #
    try:
        app = wx.App(0)
        frm = Frame(None,title='Automatas', pos=(0,5),size=(1400,770))
        frm.SetMinSize(wx.Size(1400,770))
        frm.SetMaxSize(wx.Size(1400,770))
        icono = wx.Icon('C:/Users/juand/Desktop/proyecto automatas1/src/img.ico')
        frm.SetIcon(icono)
        frm.Show(show=True)
        app.MainLoop()
    except Exception as e:
       er=str(e)
       from tkinter import messagebox
       messagebox.showerror(message="se presentó un error\n"+er, title="error")
       e.skip()
  