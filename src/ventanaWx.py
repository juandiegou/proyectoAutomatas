#!/usr/bin/env python
"""Hello World, but with more meat."""
import wx
import pygame
from pygame.locals import *
import os
import os.path
import wx.richtext
from lector import Lector
from controlador import controlador
from graph import Grafo
from solucionador import solucionador
from PIL import Image as im

pygame.init()

class Frame(wx.Frame):
    reader=None
    pnl=None
    controller=None
    g=None
    ruta=None

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(Frame, self).__init__(*args, **kw)
        #sonido
        pygame.mixer_music.load("C:/Users/juand/Desktop/proyecto automatas1/src/kiss.mp3")
        #pygame.mixer.music.play(-1)
        #self.encender(wx.EvtHandler())
        # create a panel in the frame
        self.pnl = wx.Panel(self, 0,pos=(0,0),size=(1100,5000))
        self.pnl.SetBackgroundColour('WHITE')



        #self.pintura(wx.EVT_PAINT,pnl)
        pnl2 = wx.Panel(self,0,pos=(1101,0), size=(250,745))
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
        d=pintar.Append(-1,"pintar")

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
        self.Bind(wx.EVT_MENU,self.pintura,d)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def encender(self,event):
        print("encendiendo...")
        pygame.mixer_music.play(-1)


    def apagar(self,event):
        print("apagando...")
        pygame.mixer_music.stop()

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def Openfile(self, event):
        wildcard = "Python source (*.py; *.pyc)|*.py;*.pyc|" "All files (*.*)|*.*"
        dlg = wx.FileDialog(self, message="Select your file",defaultDir=os.getcwd(),defaultFile="*.*", wildcard=wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            picfile = dlg.GetFilename()
            self.ruta= dlg.GetPath()
            print(picfile)
            print(self.ruta)
            self.reader=Lector(self.ruta)
            self.reader.leer()
            #self.g=self.reader.getGrafo()

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a automata that autogenerate",
                      "About: make for Juan Diego Gallego G",
                      wx.OK|wx.ICON_INFORMATION)


    def pintura(self,e):
        ig=im.open("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/nodes.png")
        ig=ig.resize((100,600),im.ANTIALIAS)
        ig.save("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/nodes.png",optimize=True,quality=95)
        img=wx.StaticBitmap(self.pnl,wx.ID_ANY,
        wx.Bitmap("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/nodes.png",wx.BITMAP_TYPE_ANY))




    def generar(self,event):
        #self.controler=controlador()
        if self.ruta==None:
            self.Openfile(event)
        
        inicial=self.reader.getInicial()
        aceptacion=self.reader.getAceptacion()
        s=solucionador()
        g=s.solucionar(inicial,aceptacion)
        c=controlador(g)


    def crearBotonera(self,panel2):
        panel2.SetBackgroundColour('WHEAT')

        botonG = wx.Button(panel2,-1,"generar",pos=(80,540),size=(50,25),style=3)
        botonG.Bind(wx.EVT_COMMAND_RIGHT_CLICK , self.generar)
        #creacion de eventos de cada caja de texto por un boton
        #boton1

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    #
    app = wx.App()
    frm = Frame( None,title='Automatas', pos=(0,0),size=(1450,770))
    icono = wx.Icon('C:/Users/juand/Desktop/proyecto automatas1/src/img.ico')
    frm.SetIcon(icono)
    frm.Show(show=True)
    app.MainLoop()