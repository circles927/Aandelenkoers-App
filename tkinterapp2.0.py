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
window.geometry("1200x1000") 

budget = 200000

totalAEX = 0
totalLON = 0

unitsAEX = 0
unitsLON = 0

pricing = 0

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
    global pricing
    stockSelected = stockselect.get()
    dateSelected = f"{dateSelectYear.get()}-{dateSelectMonth.get()}-{dateSelectDay.get()}"

    dataFetched = modules.selectData.fetchData(stockSelected, dateSelected)

    if dataFetched is None:
        labelData.config(text="no data found")
    else:
        # dataFetched is a scalar close value; display it
        pricing = dataFetched
        updateNetWorth()
        labelData.config(text=f"Current Pricing: {pricing:.2f}")

def updateNetWorth():
    global budget, totalAEX, totalLON, unitsAEX, unitsLON, pricing
    
    stockSelected = stockselect.get()
    if stockSelected == "AEX":
        totalAEX = unitsAEX * pricing
        labelTotalAEX.config(text=f"Total AEX: {totalAEX:.2f}")
    elif stockSelected == "London_Exchange":
        totalLON = unitsLON * pricing
        labelTotalLON.config(text=f"Total LON: {totalLON:.2f}")
    else:
        labelData.config(text="no stock selected")

def calculateResults(order):
    global budget, totalAEX, totalLON, unitsAEX, unitsLON, pricing
    orderStr = str(order)
    if stockselect.get() == "AEX":
        totalBuy = int(orderStr) * pricing
        totalAEX += totalBuy
        unitsAEX += int(orderStr)
        budget -= totalBuy
        labelbalance.config(text=f"Budget: {budget:.2f}")
        labelTotalAEX.config(text=f"Total AEX: {totalAEX:.2f}")
        labelUnitsAEX.config(text=f"Units AEX: {unitsAEX}")
    elif stockselect.get() == "London_Exchange":
        totalBuy = int(orderStr) * pricing
        totalLON += totalBuy
        unitsLON += int(orderStr)
        budget -= totalBuy
        labelbalance.config(text=f"Budget: {budget:.2f}")
        labelTotalLON.config(text=f"Total LON: {totalLON:.2f}")
        labelUnitsLON.config(text=f"Units LON: {unitsLON}")
    else: 
        print("no stock selected")


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

# ---

labelbalance = Label(window, text=f"Budget: {budget:.2f}", font=38)
labelbalance.place(x=250, y=725)

buttonbuy1 = Button(window, text="buy order 1", width=15, command=lambda: calculateResults(+1))
buttonbuy1.place(x=250, y=760)

buttonsell1 = Button(window, text="sell order 1", width=15, command=lambda: calculateResults(-1))
buttonsell1.place(x=375, y=760)

buttonbuy10 = Button(window, text="buy order 10", width=15, command=lambda: calculateResults(+10))
buttonbuy10.place(x=250, y=795)

buttonsell10 = Button(window, text="sell order 10", width=15, command=lambda: calculateResults(-10))
buttonsell10.place(x=375, y=795)

buttonbuy200 = Button(window, text="buy order 200", width=15, command=lambda: calculateResults(+200))
buttonbuy200.place(x=250, y=830)

buttonsell200 = Button(window, text="sell order 200", width=15, command=lambda: calculateResults(-200))
buttonsell200.place(x=375, y=830)

# create a persistent label to show fetched data (initially empty)
labelData = Label(window, text=f"Current Pricing: {pricing:.2f}", font=20)
labelData.place(x=625, y=575)

labelTotalAEX = Label(window, text=f"Total AEX: {totalAEX:.2f}", font=20)
labelTotalAEX.place(x=600, y=635)

labelUnitsAEX = Label(window, text=f"Units AEX: {unitsAEX}", font=20)
labelUnitsAEX.place(x=800, y=635)

labelTotalLON = Label(window, text=f"Total LON: {totalLON:.2f}", font=20)
labelTotalLON.place(x=600, y=670)

labelUnitsLON = Label(window, text=f"Units LON: {unitsLON}", font=20)
labelUnitsLON.place(x=800, y=670)
# ---

# Add button to screen
# setupgui()

# Run the application
window.mainloop()