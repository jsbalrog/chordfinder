import wx
        
class Frame (wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'pyChordFinder', size = (700, 450))

        self.Center()
        # Create a panel to house everything
        self.panel = wx.Panel(self, -1)

        # Create a wxGridBagSizer to organize our widgets
        #self.sizer = wx.GridBagSizer(7, 7)

        # Create a label for our application
        #self.label = wx.StaticText(self.panel, -1, 'Select chord characteristics', style=wx.TE_CENTER )
      
        # Key panel
        wx.StaticBox(self.panel, -1, 'Key', pos=(40, 50), size=(170, 130))
        # Create key list
        self.keyList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.keys1 = wx.ListBox(self.panel, -1, pos=(50, 70), name='Keys', choices=self.keyList, size=(150,100), style=wx.LB_HSCROLL)
        
        # Create sharp/flat radio buttons
        self.accidentalList = ['natural', '#', 'b']
        self.accidental1 = wx.RadioBox(self.panel, -1, 'Sharp/Flat', pos=(250, 50), choices=self.accidentalList, majorDimension=1, style=wx.RA_SPECIFY_COLS)

        # Create major/minor radio buttons
        self.formulaList = ['maj', 'm', '+', '*', '5', '6', 'm6', '7', 'maj7', 'm7']
        self.formula1 = wx.RadioBox(self.panel, -1, 'Formula', pos=(370, 50), choices=self.formulaList, majorDimension=1, style=wx.RA_SPECIFY_COLS)
        #self.major = wx.RadioButton(self.panel, -1, 'major', style = wx.RB_GROUP)
        #self.minor = wx.RadioButton(self.panel, -1, 'minor')

        # Additions panel
        wx.StaticBox(self.panel, -1, 'Additions', pos=(480, 50), size=(170, 150))
        # Create additional wxCheckBox instances
        self.add2 = wx.CheckBox(self.panel, -1, 'add2', pos=(490, 70))
        self.add4 = wx.CheckBox(self.panel, -1, 'add4', pos=(490, 95))
        self.add6 = wx.CheckBox(self.panel, -1, 'add6', pos=(490, 120))
        self.add9 = wx.CheckBox(self.panel, -1, 'add9', pos=(490, 145))
        self.add11 = wx.CheckBox(self.panel, -1, 'add11', pos=(490, 170))

        # Create a button
        self.button = wx.Button(self.panel, 100, 'Submit', pos=(320, 380))

        # Catch a click to the button
        wx.EVT_BUTTON(self.panel, 100, self.submit)

        # Add everything to the sizer
        #self.label, (0, 0)
        #self.keys1, (1, 0)
        #self.accidental1, (1, 1)
        #self.formula1, (1, 2)
        #self.sizer.Add(self.minor, (2, 0))
        #self.sizer.Add(wx.StaticBox(self, -1, 'Additions', (5, 5), size=(240, 170)), (1,3))
        #self.add2, (1, 3)
        #self.add4, (2, 3)
        #self.add6, (3, 3)
        #self.add9, (4, 3)
        #self.add11, (5, 3)
        #self.button, (6, 0), (1, 4)

        # Center everything
        #self.horizontal = wx.BoxSizer(wx.HORIZONTAL)
        #self.horizontal.Add((0, 0),1)
        #self.horizontal.Add(self.sizer)
        #self.horizontal.Add((0, 0), 1)
        #self.vertical = wx.BoxSizer(wx.VERTICAL)
        #self.vertical.Add((0, 0), 1)
        #self.vertical.Add(self.horizontal, 0, wx.ALIGN_CENTER)
        #self.vertical.Add((0, 0), 1)

        # Attach the sizer to the panel
        #self.panel.SetSizerAndFit(self.vertical)
        self.Show(True)
        
    # This method is triggered when the button is clicked
    def submit(self, event):
        message = ''
      
        # Check what key is selected
        x = 0
        for choice in self.keyList:
            if self.keys1.IsSelected(x):
                message = message + choice
            x = x + 1
         
        # Check what accidental, if any is selected
        print self.accidental1.GetSelection()
        if self.accidental1.GetSelection() != 0:
            message = message + self.accidentalList[self.accidental1.GetSelection()]
      
        # Check what formula is selected
        message = message + self.formulaList[self.formula1.GetSelection()]
      
        # Check whether or not each checkbox is clicked
        # If one is, add a string to the message variable
        if self.add2.GetValue():
            message = message + 'add2'
        if self.add4.GetValue():
            message = message + 'add4'
        if self.add6.GetValue():
            message = message + 'add6'
        if self.add9.GetValue():
            message = message + 'add9'
        if self.add11.GetValue():
            message = message + 'add11'

        # Display a dialog with the results
        #dialog = wx.MessageDialog(self, message, 'Chord', style = wx.OK)
        #dialog.ShowModal()
        #dialog.Destroy()
        filename = message + '.png'
        dialog = ChordDialog(None, 01, 'Chord', file=filename)
        dialog.ShowModal()
        dialog.Destroy()

class ChordDialog(wx.Dialog):  
    def __init__(self, parent, id, title, file):  
        style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER) # XOR to remove the resizeable border          
        wx.Dialog.__init__(self, parent, id, title=title, size=(100, 100), style=style)  
        self.panel = wx.Panel(self, -1)  
        self.panel.SetBackgroundColour('White') # make the background of the window white  
        self.image = wx.Image(file, wx.BITMAP_TYPE_ANY, -1) # auto-detect file type
        self.ShowBitmap()
                
    def ShowBitmap(self):
        
        # Convert to Bitmap for wxPython to draw it to screen
        self.bitmap = wx.StaticBitmap(self.panel, -1, wx.BitmapFromImage(self.image))
        # Make the application's window as large as the image
        self.SetClientSize(self.bitmap.GetSize())
        self.Center() # open in the center of the screen

class App(wx.App):
   
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    application = App()

    application.MainLoop()