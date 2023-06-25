import tkinter
import random

"""
시작대기 구현 & 스코어 구현
"""

FNT = ("Times New Roman", 20, "bold")

stage = 0
score = 0

bar_x = 0
bar_y = 540

ball_x = 0
ball_y = 0
ball_xp = 0
ball_yp = 0

block = []
for i in range(5):
    block.append([1] * 10)
for i in range(10):
    block.append([0] * 10)

key = ""
keyoff = False
idx = 0
tmr = 0

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
    cvs.create_text(600, 20, text="SCORE " + str(score), fill="white", font=FNT, tag="BG")


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
    global idx, tmr, score, ball_x, ball_y, ball_xp, ball_yp
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
        score = score + 10

    ball_y = ball_y + ball_yp
    if ball_y >= 600:
        idx = 2
        tmr = 0
        return
    if ball_y < 20:
        ball_y = 20
        ball_yp = -ball_yp
    x = int(ball_x / 80)
    y = int(ball_y / 40)
    if block[y][x] == 1:
        block[y][x] = 0
        ball_yp = -ball_yp
        score = score + 10

    if bar_y - 40 <= ball_y and ball_y <= bar_y:
        if bar_x - 80 <= ball_x and ball_x <= bar_x + 80:
            ball_yp = -10
            score = score + 1
        elif bar_x - 100 <= ball_x and ball_x <= bar_x - 80:
            ball_yp = -10
            ball_xp = random.randint(-20, -10)
            score = score + 2
        elif bar_x + 80 <= ball_x and ball_x <= bar_x + 100:
            ball_yp = -10
            ball_xp = random.randint(10, 20)
            score = score + 2

def main_proc():
    global key, keyoff
    global idx, tmr, stage, score
    global bar_x, ball_x, ball_y, ball_xp, ball_yp

    if idx == 0:
        tmr = tmr + 1
        if tmr == 1:
            stage = 1
            score = 0
        if tmr == 2:
            ball_x = 160
            ball_y = 240
            ball_xp = 10
            ball_yp = 10
            bar_x = 400
            draw_block()
            draw_ball()
            draw_bar()
            cvs.create_text(400, 300, text="START", fill="cyan", font=FNT, tag="TXT")
        if tmr == 30:
            cvs.delete("TXT")
            idx = 1
    elif idx == 1:
        move_ball()
        move_bar()
        draw_block()
        draw_ball()
        draw_bar()

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