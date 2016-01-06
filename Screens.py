import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import queue
import threading
import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

class HomeView(tk.Tk):
    controller =''
    frames ={}
    queue = ''
    def __init__(self, controller, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Sea of BTC client")
        self.controller = controller
        self.queue = queue.Queue()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomePage, LivePage, PieChartPage, AboutPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def start_stream(self, text):
        self.controller.start_stream(text)

    def get_about(self):
        return self.frames[AboutPage]

class WelcomePage(tk.Frame):
    controller = ''

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        entry1 = ttk.Entry(self)
        entry1.pack()

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(LivePage))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PieChartPage))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: self.open_graph(entry1.get()) )
        button3.pack()

    def open_graph(self, parameter):
        t = threading.Thread(target=self.controller.show_frame(AboutPage))
        t.daemon = True
        t.start()
        self.controller.start_stream(parameter)



class LivePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(WelcomePage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(PieChartPage))
        button2.pack()


class PieChartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(WelcomePage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                             command=lambda: controller.show_frame(LivePage))
        button2.pack()


class AboutPage(tk.Frame):
    xar = []
    yar = []
    def __init__(self, parent, controller):
        print("ABOUT PAGE CALLED")
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(WelcomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def update(self, text):
        x = 0
        y = 0
        print("Update called")
        x += 1
        if text.startswith("pos"):
            y += 1
        elif text.startswith("neg"):
            y -= 1

        self.xar.append(x)
        self.yar.append(y)

        a.clear()
        a.plot(self.xar,self.yar)

#ani = animation.FuncAnimation(f, update, interval=1000)

