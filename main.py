from tkinter import *

root = Tk()
window_width = 400
window_height = 450
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(f"{screen_width}x{screen_height}")
# find center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
# set the window position
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
# set the background color
root.configure(bg="black")
# set the change tk name
root.title("Calculator")
# set the change default logo
root.iconbitmap('calculator.ico')
root.attributes("-topmost", True) #'-transparentcolor', 'blue' '-alpha', 0.5
root.resizable(False, False)

# --------------------------------------------------------------------
def nolr():
    ekran.insert(END, "0")

def birr():
    ekran.insert(END, "1")

def ikkir():
    ekran.insert(END, "2")

def uchr():
    ekran.insert(END, "3")

def tortr():
    ekran.insert(END, "4")

def beshr():
    ekran.insert(END, "5")

def oltir():
    ekran.insert(END, "6")

def yettir():
    ekran.insert(END, "7")

def sakkizr():
    ekran.insert(END, "8")

def toqqizr():
    ekran.insert(END, "9")

######################################################################
# Arifmetik amallar
def tozalash():
    ekran.delete(0, END)

def birdel():
    result = ekran.get()
    ekran.delete(first=len(result)-1, last=END)

def nuqtab():
    try:
        if ekran.get()[-1] not in ['.', '/', '*', '+', '-']:
            ekran.insert(END, '.')
    except:
        pass

def plminb():
    try:
        if ekran.get()[0] == "-":
            ekran.delete(0, 1)
        else:
            ekran.insert(0, "-")
    except:
        pass

def bolb():
    try:
        if ekran.get()[-1] not in ['.', '/', '*', '+', '-']:
            ekran.insert(END, '/')
    except:
        pass
    
def kopaytirb():
    try:
        if ekran.get()[-1] not in ['.', '/', '*', '+', '-']:
            ekran.insert(END, '*')
    except:
        pass
    
def qoshb():
    try:
        if ekran.get()[-1] not in ['.', '/', '*', '+', '-']:
            ekran.insert(END, '+')
    except:
        pass

def ayirb():
    try:
        if ekran.get()[-1] not in ['.', '/', '*', '+', '-']:
            ekran.insert(END, '-')
    except:
        pass

def tengb():
    try:
        if ekran.get() == "":
           pass
        elif ekran.get()[0] == "":
           ekran.delete(0, END)
        else:
            natija = ekran.get()
            natija = eval(natija)
            tozalash()
            ekran.insert(END, natija)
    except:
        pass
    
######################################################################

# --------------------------------------------------------------------
ekran = Entry(root, bd=5, font=('Arial', 25), width=20, justify=RIGHT)
ekran.place(x=13, y=10)
# 1 - qator
c = Button(root, text="C", font=('Arial', 20), bg='orange', fg='black', padx=67, command=tozalash)
c.place(x=10, y=90)

tozala = Button(root, text="<x", font=('Arial', 20), bg='orange', fg='black', width=4, command=birdel)
tozala.place(x=214, y=90)

bolish = Button(root, text="/", font=('Arial', 20),  bg='orange', fg='black', width=4, command=bolb)
bolish.place(x=316, y=90)
# 2 - qator
yetti = Button(root, text="7", font=('Arial', 20), bg='white', fg='black', width=4, command=yettir)
yetti.place(x=10, y=160)

sakkiz = Button(root, text="8", font=('Arial', 20), bg='white', fg='black', width=4, command=sakkizr)
sakkiz.place(x=112, y=160)

toqqiz = Button(root, text="9", font=('Arial', 20), bg='white',  fg='black', width=4, command=toqqizr)
toqqiz.place(x=214, y=160)

kopaytirish = Button(root, text="*", font=('Arial', 20), bg='orange', fg='black', width=4, command=kopaytirb)
kopaytirish.place(x=316, y=160)
# 3 - qator
tort = Button(root, text="4", font=('Arial', 20), bg='white', fg='black', width=4, command=tortr)
tort.place(x=10, y=230)

besh = Button(root, text="5", font=('Arial', 20), bg='white', fg='black', width=4, command=beshr)
besh.place(x=112, y=230)

olti = Button(root, text="6", font=('Arial', 20), bg='white', fg='black', width=4, command=oltir)
olti.place(x=214, y=230)

ayirish = Button(root, text="-", font=('Arial', 20), bg='orange', fg='black', width=4, command=ayirb)
ayirish.place(x=316, y=230)
# 4 - qator
bir = Button(root, text="1", font=('Arial', 20), bg='white', fg='black', width=4, command=birr)
bir.place(x=10, y=300)

ikki = Button(root, text="2", font=('Arial', 20), bg='white', fg='black', width=4, command=ikkir)
ikki.place(x=112, y=300)

uch = Button(root, text="3", font=('Arial', 20), bg='white', fg='black', width=4, command=uchr)
uch.place(x=214, y=300)

qoshish = Button(root, text="+", font=('Arial', 20), bg='orange', fg='black', width=4, command=qoshb)
qoshish.place(x=316, y=300)
# 5 - qator
plmin = Button(root, text="+/-", font=('Arial', 20), bg='orange', fg='black', width=4, command=plminb)
plmin.place(x=10, y=370)

nol = Button(root, text="0", font=('Arial', 20), bg='white', fg='black', width=4, command=nolr)
nol.place(x=112, y=370)

nuqta = Button(root, text=".", font=('Arial', 20), bg='orange', fg='black', width=4, command=nuqtab)
nuqta.place(x=214, y=370)

teng = Button(root, text="=", font=('Arial', 20), bg='orange', fg='black', width=4, command=tengb)
teng.place(x=316, y=370)

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()

root.mainloop()
