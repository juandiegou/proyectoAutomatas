
import wx

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        self.img1=wx.Image("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/Shortest traversal.png", wx.BITMAP_TYPE_ANY)
        self.img2=wx.Image("C:/Users/juand/Desktop/proyecto automatas1/src/imgs/img4.png", wx.BITMAP_TYPE_ANY)
        self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(self.img1), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_bitmap3, 1, wx.EXPAND, 0 )
        self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(self.img2))
        bSizer11.Add( self.m_bitmap4, 1, wx.EXPAND, 0 )
        self.Bind(wx.EVT_SIZE, self.onResize)
        self.SetSizer( bSizer11 )
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__( self ):
        pass

    def onResize(self, event):
        # self.Layout()
        frame_size = self.GetSize()
        frame_h = (frame_size[0]-10) / 2
        frame_w = (frame_size[1]-10) / 2
        img1 = self.img1.Scale(frame_h,frame_w)
        img2 = self.img2.Scale(frame_h,frame_w)
        self.m_bitmap3.SetBitmap(wx.BitmapFromImage(img1))
        self.m_bitmap4.SetBitmap(wx.BitmapFromImage(img2))
        self.Refresh()
        self.Layout()

app = wx.App(0)
MyFrame2(None).Show()
app.MainLoop()