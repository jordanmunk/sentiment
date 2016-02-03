import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
    NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

figure = Figure(figsize=(5, 5), dpi=100)
figure_axes = figure.add_subplot(111)
figure2 = Figure(figsize=(5, 5), dpi=100)
piechart = figure2.add_subplot(111)

pos = 0
neg = 0
neut = 0

class HomeView(tk.Tk):
    controller = ''
    frames = {}

    def __init__(self, mainController, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Anton's Bad Sentiment Analyzer")
        self.controller = mainController

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomePage, AboutView, PieChartView, LiveView):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def start_stream(self, text):
        self.controller.start_stream(text)

    def get_live(self):
        return self.frames[LiveView]
    def get_pie(self):
        return self.frames[PieChartView]

    def get_pie(self):
        return self.frames[PieChartView]


class WelcomePage(tk.Frame):
    controller = ''

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Anton's Bad Sentiment Analyzer",
                         font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label2 = tk.Label(self, text="Tweets worden opgeslagen in "
                                     "StreamedTweets.txt totdat je in een "
                                     "sessie meer dan 10.000 tweets hebt "
                                     "opgehaald.",
                         )
        label2.pack(pady=10, padx=10)
        button = ttk.Button(self, text="About",
                            command=lambda: controller.show_frame(AboutView))
        button.pack()

        button2 = ttk.Button(self, text="Pie Chart",
                             command=lambda: controller.show_frame(
                                 PieChartView))
        button2.pack()

        button3 = ttk.Button(self, text="Live graphing",
                             command=lambda: self.controller.show_frame(
                                 LiveView))
        button3.pack()


class AboutView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="About", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label2 = tk.Label(self, text="Gemaakt voor het vak ISCP in "
                                     "studiejaar 2015-2016")
        label2.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(
                                 WelcomePage))
        button1.pack()

        label2 = tk.Label(self, text="Geschreven door Anton Steenvoorden",
                          font=LARGE_FONT)
        label2.pack(pady=10, padx=10)


class PieChartView(tk.Frame):
    canvas = None
    controller = None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pie chart", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        labels = 'Positive', 'Neutral', 'Negative'
        amount = [pos, neut, neg]
        print(amount)
        colors = ['green', 'lightskyblue', 'red']
        explode = (0, 0.05, 0)  # proportion with which to offset each
        # wedge
        entry1 = ttk.Entry(self)
        entry1.pack()
        button3 = ttk.Button(self, text="Start stream ",
                             command=lambda: controller.start_stream(
                                 entry1.get()))
        button3.pack()

        piechart.pie(amount,  # data
                     explode=explode,  # offset parameters
                     labels=labels,  # slice labels
                     colors=colors,  # array of colours
                     autopct='%1.1f%%',  # print the values inside the wedges
                     shadow=True,  # enable shadow
                     startangle=70  # starting angle
                     )
        piechart.axis('equal')
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.stop())
        button1.pack()
        self.canvas = FigureCanvasTkAgg(figure2, self)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH,
                                         expand=True)

        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def stop(self):
        self.controller.show_frame(WelcomePage)
        self.controller.controller.stop_stream()

    def update(self):
        piechart.clear()
        piechart.pie([pos, neut, neg])
        self.canvas.draw_idle()

class LiveView(tk.Frame):
    xar = []
    yar = []
    x = 0
    y = 0
    canvas = None
    controller = None

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Live graphing !", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.stop())
        button1.pack()

        entry1 = ttk.Entry(self)
        entry1.pack()
        button3 = ttk.Button(self, text="Start stream ",
                             command=lambda: controller.start_stream(
                                 entry1.get()))
        button3.pack()

        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH,
                                         expand=True)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def stop(self):
        self.controller.show_frame(WelcomePage)
        self.controller.controller.stop_stream()

    def update(self, text):
        print("Update called")
        self.x += 1
        if text.startswith("pos"):
            self.y += 1
            global pos
            pos += 1
        elif text.startswith("neg"):
            self.y -= 1
            global neg
            neg += 1
        elif text.startswith("neut"):
            global neut
            neut += 1
        self.xar.append(self.x)
        self.yar.append(self.y)

        figure_axes.clear()
        figure_axes.plot(self.xar, self.yar)
        self.canvas.draw()

# ani = animation.FuncAnimation(f, update, interval=1000)
