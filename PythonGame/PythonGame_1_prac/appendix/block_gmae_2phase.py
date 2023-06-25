import tkinter

"""
그리기 구현
"""

ball_x = 160
ball_y = 240
ball_xp = 10
ball_yp = 10
bar_x = 400
bar_y = 540

block = []
for i in range(5):
    block.append([1] * 10)

def block_color(x, y):  # format() 명령으로 16진수 값 변환 가능
    col = "#{0:x}{1:x}{2:x}".format(15 - x - int(y / 3), x + 1, y * 3 + 3)
    return col


def draw_block():
    cvs.delete("BG")
    for y in range(5):
        for x in range(10):
            gx = x * 80
            gy = y * 40
            if block[y][x] == 1:
                cvs.create_rectangle(gx + 1, gy + 4, gx + 79, gy + 32, fill=block_color(x, y), width=0, tag="BG")

def draw_bar():
    cvs.delete("BAR")
    cvs.create_rectangle(bar_x - 80, bar_y - 12, bar_x + 80, bar_y + 12, fill="silver", width=0, tag="BAR")
    cvs.create_rectangle(bar_x - 78, bar_y - 14, bar_x + 78, bar_y + 14, fill="silver", width=0, tag="BAR")
    cvs.create_rectangle(bar_x - 78, bar_y - 12, bar_x + 78, bar_y + 12, fill="white", width=0, tag="BAR")


def draw_ball():
    cvs.delete("BALL")
    cvs.create_oval(ball_x - 20, ball_y - 20, ball_x + 20, ball_y + 20, fill="gold", outline="orange", width=2, tag="BALL")
    cvs.create_oval(ball_x - 16, ball_y - 16, ball_x + 12, ball_y + 12, fill="yellow", width=0, tag="BALL")

root = tkinter.Tk()
root.title("블록 격파 게임")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=800, height=600, bg="black")
draw_block()
draw_bar()
draw_ball()
cvs.pack()
root.mainloop()
