# tkinter app
# import pandas
import matplotlib.pyplot as plt
import modules
import sys

# from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
# from PIL import ImageTk, Image

window = Tk()
window.title("Plotting the plot!")
window.geometry("1000x950") 

def on_closing():
    try:
        plt.close('all')          # stop/close matplotlib figures and timers
    except Exception:
        pass
    window.quit()                # exit the Tk mainloop
    window.destroy()             # destroy the window
    sys.exit(0)                  # ensure the Python process exits (helps the debugger)

# make the window close button call the handler
window.protocol("WM_DELETE_WINDOW", on_closing)

def displayplot():
    # importing DataFrame
    df = modules.createplot2.mergingData()

    topframe = Frame(window)
    topframe.pack(side="top")

    # creating plotconditions
    fig, ax = plt.subplots()
    ax.plot(df['timestamp'], df['close_x'])
    ax.plot(df['timestamp'], df['close_y'])

    # create element with which to display plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=topframe)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # create a toolbar to go with the plot
    toolbar = NavigationToolbar2Tk(canvas, topframe)
    toolbar.update()
    canvas.get_tk_widget().pack(side="top")

def fetchdata():
    stockSelected = stockselect.get()
    dateSelected = f"{dateSelectYear.get()}-{dateSelectMonth.get()}-{dateSelectDay.get()}"

    dataFetched = modules.selectData.fetchData(stockSelected, dateSelected)

    if dataFetched is None:
        labelData.config(text="no data found")
    else:
        # dataFetched is a scalar close value; display it
        labelData.config(text=str(dataFetched))


bottomframe = Frame(window)
bottomframe.pack(side="bottom")

middleframe = Frame(window)
middleframe.pack(side="bottom")

emptylabel1 = Label(bottomframe, text="", height=2)
emptylabel1.pack(side="bottom")

button = Button(bottomframe, width=10, height=2, text='plot', command=displayplot)
button.pack(side="bottom")

emptylabel2 = Label(bottomframe, text="---", height=2)
emptylabel2.pack(side="top")

label1 = Label(window, text="select stock", font=28)
label1.place(x=250, y=575)

stockselect = Spinbox(window, values=("AEX", "London_Exchange"), width=20)
stockselect.place(x=250, y=605)

labeldate = Label(window, text="select date", font=28)
labeldate.place(x=250, y=645)

dateSelectYear = Spinbox(window, from_=2005, to=2025, width=5)
dateSelectYear.place(x=250, y=675)

dateSelectMonth = Spinbox(window, from_=1, to=12, width=3)
dateSelectMonth.place(x=300, y=675)

dateSelectDay = Spinbox(window, from_=1, to=31, width=3)
dateSelectDay.place(x=340, y=675)

selectionMadeButton = Button(window, text="select date", command=fetchdata)
selectionMadeButton.place(x=380, y=675)

# create a persistent label to show fetched data (initially empty)
labelData = Label(window, text="", font=16)
labelData.place(x=600, y=575)

labelbalance = Label(window, text="20.000", font=38)
labelbalance.place(x=250, y=725)

buttonbuy = Button(window, text="buy order")
buttonbuy.place(x=250, y=750)

buttonsell = Button(window, text="sell order")
buttonsell.place(x=320, y=750)

# Add button to screen
# setupgui()

# Run the application
window.mainloop()