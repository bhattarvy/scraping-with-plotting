import matplotlib.pyplot as plt
from urllib import urlopen
from	io	import	StringIO
import	csv
from bs4 import BeautifulSoup
from Tkinter import *
def plot(p):


    data	=	urlopen(p).read().decode('ascii',	'ignore')

    dataFile	=	StringIO(data)
    dictReader	=	csv.DictReader(dataFile)
    x=[0]
    y=[0]
    for	row	in	dictReader:
        y.append(row[' "NICOTINE"'])
        x.append(row['TAR'])
        #y.append(row['NICOTINE'])

    plt.plot(x,y)
    plt.show()
def donothing():
    def fuck(u):
        html=urlopen("https://people.sc.fsu.edu/~jburkardt/datasets/triola/triola.html")
        bsObj=BeautifulSoup(html)
        scrollbar = Scrollbar(root)
        scrollbar.pack( side = RIGHT, fill=Y )
        mylist = Listbox(root, yscrollcommand = scrollbar.set )
        for x in bsObj.findAll("a"):
            mylist.insert(END, x['href'])
        mylist.pack( side = LEFT, fill = BOTH )
        scrollbar.config( command = mylist.yview )
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button",command=fuck("https://people.sc.fsu.edu/~jburkardt/datasets/triola/triola.html"))
    button.pack()
    E1 = Entry(filewin, bd =5)

    E1.pack()
    print(E1.get())
    button=Button(filewin,text="plotit",command=plot("https://people.sc.fsu.edu/~jburkardt/datasets/triola/cigaret.csv"))
    button.pack()
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)


menubar.add_cascade(label="File", menu=filemenu)


root.config(menu=menubar)
root.mainloop()
