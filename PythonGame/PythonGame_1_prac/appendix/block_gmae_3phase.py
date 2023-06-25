import tkinter
import random

"""
움직임 구현
"""

stage = 0
score = 0

bar_x = 0
bar_y = 540

ball_x = 160
ball_y = 240
ball_xp = 10
ball_yp = 10

block = []
for i in range(5):
    block.append([1] * 10)
for i in range(10):
    block.append([0] * 10)

key = ""

def key_down(e):
    global key
    key = e.keysym


def key_up(e):
    global keyoff
    keyoff = True


def block_color(x, y):  # format() 명령으로 16진수 값 변환 가능
    col = "#{0:x}{1:x}{2:x}".format(15 - x - int(y / 3), x + 1, y * 3 + 3)
    return col


def draw_block():
    cvs.delete("BG")
    for y in range(15):
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


def move_bar():
    global bar_x
    if key == "Left" and bar_x > 80:
        bar_x = bar_x - 40
    if key == "Right" and bar_x < 720:
        bar_x = bar_x + 40


def move_ball():
    global ball_x, ball_y, ball_xp, ball_yp
    ball_x = ball_x + ball_xp
    if ball_x < 20:
        ball_x = 20
        ball_xp = -ball_xp
    if ball_x > 780:
        ball_x = 780
        ball_xp = -ball_xp
    x = int(ball_x / 80)
    y = int(ball_y / 40)
    if block[y][x] == 1:
        block[y][x] = 0
        ball_xp = -ball_xp

    ball_y = ball_y + ball_yp

    if ball_y < 20:
        ball_y = 20
        ball_yp = -ball_yp
    x = int(ball_x / 80)
    y = int(ball_y / 40)
    if block[y][x] == 1:
        block[y][x] = 0
        ball_yp = -ball_yp

    if bar_y - 40 <= ball_y <= bar_y:
        if bar_x - 80 <= ball_x <= bar_x + 80:
            ball_yp = -10
        elif bar_x - 100 <= ball_x <= bar_x - 80:
            ball_yp = -10
            ball_xp = random.randint(-20, -10)
        elif bar_x + 80 <= ball_x <= bar_x + 100:
            ball_yp = -10
            ball_xp = random.randint(10, 20)

def main_proc():
    move_bar()
    move_ball()
    draw_bar()
    draw_ball()
    draw_block()
    root.after(50, main_proc)

root = tkinter.Tk()
root.title("블록 격파 게임")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=800, height=600, bg="black")
main_proc()
cvs.pack()
root.bind("<Key>", key_down)
root.bind("<KeyRelease>", key_up)
root.mainloop()
