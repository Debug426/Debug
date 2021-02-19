from tkinter import Tk
from tkinter import Listbox

myWindow = Tk()

List1 = Listbox(myWindow)
List2 = Listbox(myWindow)

li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

for item in li:
    List1.insert(0, item)

for item in movie:
    List2.insert(0, item)

List1.pack()
List2.pack()

myWindow.mainloop()
