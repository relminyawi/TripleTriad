import os
import stat
import sys
import cardInfo as ci
from Tkinter import *
from PIL import Image, ImageTk

class Application:
	def __init__(self):
		self.tk = Tk()
		self.pad = 0
		self._geom = '200x200+0+0'
		self.tk.geometry("{0}x{1}+0+0".format(self.tk.winfo_screenwidth()-self.pad,
			                                  self.tk.winfo_screenheight()-self.pad))
		self.tk.bind('z',self.toggleGeometry)
		self.frame = Frame(self.tk)
		self.frame.pack()
		self.createBackground()

	def createBackground(self):
		self.backgroundImagePath   = os.path.join(os.path.join(os.path.dirname(__file__), 'Images'), 'board.jpg')
		self.backgroundImage       = Image.open(self.backgroundImagePath)
		self.tkBackgroundImage     = ImageTk.PhotoImage(self.backgroundImage)
		self.backgroundLabel       = Label(self.tk,image=self.tkBackgroundImage)
		self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
		self.backgroundLabel.pack()
   
	def toggleGeometry(self, event):
		geom = self.tk.winfo_geometry()
		self.tk.geometry(self._geom)
		self._geom = geom

if __name__ == '__main__':
    app = Application()
    app.tk.mainloop()