# Hello World.py - 贝塞尔曲线绘制程序
# 奶奶您好！运行这个程序就能看到漂亮的贝塞尔曲线啦~
# （双击这个文件，或者在命令行输入: python "Hello World.py"）

import turtle
import math

def bezier_point(t, points):
    """用德卡斯特里奥算法计算贝塞尔曲线上 t (0~1) 位置的点"""
    temp = [list(p) for p in points]
    n = len(temp)
    for r in range(1, n):
        for i in range(n - r):
            temp[i][0] = (1 - t) * temp[i][0] + t * temp[i + 1][0]
            temp[i][1] = (1 - t) * temp[i][1] + t * temp[i + 1][1]
    return temp[0]

def draw_control_points(points):
    """画出控制点和连线"""
    turtle.pencolor("gray")
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    for p in points[1:]:
        turtle.goto(p[0], p[1])
    turtle.penup()
    # 画控制点小圆点
    for p in points:
        turtle.goto(p[0], p[1] - 5)
        turtle.pendown()
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

def draw_bezier(points, steps=100):
    """绘制贝塞尔曲线"""
    turtle.pencolor("blue")
    turtle.pensize(3)
    turtle.penup()
    start = bezier_point(0, points)
    turtle.goto(start[0], start[1])
    turtle.pendown()
    for i in range(1, steps + 1):
        t = i / steps
        x, y = bezier_point(t, points)
        turtle.goto(x, y)
    turtle.penup()

def write_title(text):
    """在屏幕上方写标题"""
    turtle.penup()
    turtle.goto(0, 280)
    turtle.pencolor("purple")
    turtle.write(text, align="center", font=("微软雅黑", 20, "bold"))

def main():
    turtle.setup(800, 650)
    turtle.speed(0)
    turtle.bgcolor("lightyellow")
    turtle.title("奶奶的贝塞尔曲线")

    # 控制点坐标
    control_points = [
        (-250, -100),   # 起点
        (-100, 200),    # 控制点1
        (100, -200),    # 控制点2
        (250, 100),     # 终点
    ]

    # 画标题
    write_title("贝塞尔曲线 Bezier Curve")

    # 画控制点和连线
    draw_control_points(control_points)

    # 画贝塞尔曲线
    draw_bezier(control_points)

    # 标注起点和终点
    turtle.penup()
    turtle.goto(control_points[0][0], control_points[0][1] + 20)
    turtle.pencolor("darkred")
    turtle.write("起点", align="center", font=("微软雅黑", 12, "normal"))
    turtle.goto(control_points[-1][0], control_points[-1][1] + 20)
    turtle.write("终点", align="center", font=("微软雅黑", 12, "normal"))

    turtle.hideturtle()
    turtle.done()

main()
