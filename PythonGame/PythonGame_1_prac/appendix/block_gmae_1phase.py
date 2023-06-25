import tkinter

"""
윈도우 창 구현
"""

root = tkinter.Tk()
root.title("블록 격파 게임")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=800, height=600, bg="black")
cvs.pack()
root.mainloop()
