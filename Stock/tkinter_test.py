import tkinter as tk
from tkinter import ttk
import matplotlib 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
from matplotlib import style
import matplotlib.animation as animation
from datetime import datetime
import numpy as np
import pandas as pd



LARGE_FONT = ("Verdana",12)
style.use("ggplot");

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
	path = "dataset.csv"
	lines = open(path, mode='r').readlines()

	data = []
	lines.pop(0)

	for l in lines:
		date = datetime.strptime(l.replace('\n','').split(',')[0],'%m/%d/%Y')
		value = float(l.replace('\n','').split(',')[1])

		data.append([date,value])

	xlist = []
	ylist = []

	for point in data:
		xlist.append(point[0])
		ylist.append(point[1])

	#plt.title('Stock Indicator')
	#plt.ylabel('Stock Price')
	#plt.xlabel('Date and Time')

	a.clear()
	a.plot(xlist, ylist)


class StockPriceApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.iconbitmap(self, default="Stocks.ico" )
		tk.Tk.wm_title(self, "Stock Trading App")

		container = tk.Frame(self)
		container.pack(side="top", fill = "both",expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen):

			frame = F(container, self) #intial page we run on

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text = "Choose Which StockTrend to Follow", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonstart1 = ttk.Button(self, text="AFDIS",command = lambda: controller.show_frame(PageOne))
		buttonstart1.pack()

		buttonstart2 = ttk.Button(self, text="BAT",command = lambda: controller.show_frame(PageTwo))
		buttonstart2.pack()

		buttonstart3 = ttk.Button(self, text="DELTA",command = lambda: controller.show_frame(PageThree))
		buttonstart3.pack()

		buttonstart4 = ttk.Button(self, text="ECONET",command = lambda: controller.show_frame(PageFour))
		buttonstart4.pack()

		buttonstart5 = ttk.Button(self, text="INNSCOR",command = lambda: controller.show_frame(PageFive))
		buttonstart5.pack()

		buttonstart6 = ttk.Button(self, text="LAFARGE",command = lambda: controller.show_frame(PageSix))
		buttonstart6.pack()

		buttonstart7 = ttk.Button(self, text="OLD MUTUAL",command = lambda: controller.show_frame(PageSeven))
		buttonstart7.pack()

		buttonstart8 = ttk.Button(self, text="PPC",command = lambda: controller.show_frame(PageEight))
		buttonstart8.pack()

		buttonstart9 = ttk.Button(self, text="HWANGE COLLIERY",command = lambda: controller.show_frame(PageNine))
		buttonstart9.pack()

		buttonstart10 = ttk.Button(self, text="RIOZIM",command = lambda: controller.show_frame(PageTen))
		buttonstart10.pack()



class PageOne(tk.Frame):
	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text = "AFDIS", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageOne = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageOne.pack()

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageTwo(tk.Frame):
	def __init__(self, parent, controller):

		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text = "BAT", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageTwo = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageTwo.pack()

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageThree(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "DELTA", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageThree = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageThree.pack()
		

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageFour(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "ECONET", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageThree = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageThree.pack()
		

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageFive(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "INNSCOR", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageThree = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageThree.pack()
		

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageSix(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "LAFARGE", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageThree = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageThree.pack()
		

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageSeven(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "OLD MUTUAL", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageThree = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageThree.pack()

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageEight(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "PPC", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageThree = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageThree.pack()
		

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageNine(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "HWANGE", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageThree = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageThree.pack()
		
		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class PageTen(tk.Frame):
	def __init__(self, parent,controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = ".RIOZIM.", font = LARGE_FONT)
		label.pack(pady = 10,padx = 10)

		buttonPageThree = ttk.Button(self, text="Back to Home",command = lambda: controller.show_frame(StartPage))
		buttonPageThree.pack()

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # show can be used but deprecated in this version
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)




app = StockPriceApp()
ani = animation.FuncAnimation(f, animate, interval = 1000)# 1 second
app.mainloop()