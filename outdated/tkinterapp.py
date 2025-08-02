# import pandas
import matplotlib.pyplot as plt
from createplot import mergingData
# from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
# from PIL import ImageTk, Image

window = Tk()
window.title("Plotting the plot!")
window.geometry("740x655") 

def displayplot():
    # importing DataFrame
    df = mergingData()

    topframe = Frame(window)
    topframe.pack(side="top")

    # creating plotconditions
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Close_x'])
    ax.plot(df['Date'], df['Close_y'])

    # create element with which to display plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=topframe)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # create a toolbar to go with the plot
    toolbar = NavigationToolbar2Tk(canvas, topframe)
    toolbar.update()
    canvas.get_tk_widget().pack(side="top")

def setupgui():
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

    labelbalance = Label(middleframe, text="20.000", font=38)
    labelbalance.pack(side="left")

    buttonbuy = Button(middleframe, text="buy order")
    buttonbuy.pack(side="left")

    buttonsell = Button(middleframe, text="sell order")
    buttonsell.pack(side="left")


# Add button to screen
setupgui()

# Run the application
window.mainloop()