from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *

#class from the code editor example
class LineNumberArea(QWidget):
	def __init__(self,*args,**kwargs):
		super(LineNumberArea,self).__init__()
		self.setParent(args[0])
	
	def sizeHint(self):
		return QSize(self.parent().lineNumberAreaWidth(), 0)

	def paintEvent(self,event):
		self.parent().lineNumberAreaPaintEvent(event)