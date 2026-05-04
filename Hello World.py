# Hello World.py - 动态贝塞尔曲线 + 数学之美
# 奶奶您运行这个，会看到会动的炫酷贝塞尔曲线！

import turtle
import math
import time

def bezier_point(t, points):
    """德卡斯特里奥算法：计算贝塞尔曲线上 t (0~1) 位置的点"""
    temp = [list(p) for p in points]
    n = len(temp)
    for r in range(1, n):
        for i in range(n - r):
            temp[i][0] = (1 - t) * temp[i][0] + t * temp[i + 1][0]
            temp[i][1] = (1 - t) * temp[i][1] + t * temp[i + 1][1]
    return temp[0]

def hsv_to_rgb(h, s, v):
    """HSV 转 RGB，用于彩虹色"""
    h = h % 1.0
    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i = i % 6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)

def main():
    turtle.setup(900, 750)
    turtle.bgcolor("black")
    turtle.title("奶奶的炫酷数学曲线")
    turtle.tracer(0, 0)  # 关闭自动刷新，手动控制动画
    turtle.hideturtle()

    # 移动画布原点，让中心在屏幕中间
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    # 4 个控制点，各自按不同轨道运动
    # 每个控制点有：圆心(cx, cy), 半径, 角速度, 初始角度
    orbits = [
        {"cx": -250, "cy": 0,   "r": 120, "speed": 1.3, "phase": 0},
        {"cx": -80,  "cy": 180, "r": 100, "speed": 1.7, "phase": 1.2},
        {"cx": 80,   "cy": -180,"r": 110, "speed": 2.1, "phase": 2.5},
        {"cx": 250,  "cy": 0,   "r": 130, "speed": 1.5, "phase": 3.8},
    ]

    steps = 200       # 曲线分段数
    hue_offset = 0    # 颜色循环

    running = True

    while running:
        t_now = time.time()

        # 计算当前控制点位置
        control_points = []
        for orb in orbits:
            angle = orb["phase"] + t_now * orb["speed"]
            x = orb["cx"] + orb["r"] * math.cos(angle)
            y = orb["cy"] + orb["r"] * math.sin(angle)
            control_points.append((x, y))

        pen.clear()

        # --- 画控制点连线（半透明灰色） ---
        pen.pencolor("#333333")
        pen.pensize(1)
        pen.penup()
        pen.goto(control_points[0][0], control_points[0][1])
        pen.pendown()
        for p in control_points[1:]:
            pen.goto(p[0], p[1])
        pen.penup()

        # --- 画控制点（发光的彩色点） ---
        for i, p in enumerate(control_points):
            # 光晕
            pen.goto(p[0], p[1])
            hue = (hue_offset + i * 0.25) % 1.0
            r, g, b = hsv_to_rgb(hue, 0.8, 1.0)
            turtle.colormode(1.0)
            pen.fillcolor(r, g, b)
            pen.pencolor(r, g, b)
            # 画实心点
            pen.pendown()
            pen.begin_fill()
            pen.circle(6)
            pen.end_fill()
            pen.penup()
            # 光晕外圈
            pen.goto(p[0], p[1] - 12)
            pen.pencolor(r * 0.5, g * 0.5, b * 0.5)
            pen.pensize(1)
            pen.pendown()
            pen.circle(12)
            pen.penup()

        # --- 画贝塞尔曲线（彩虹色渐变） ---
        prev_point = bezier_point(0, control_points)
        for i in range(1, steps + 1):
            t_val = i / steps
            point = bezier_point(t_val, control_points)

            hue = (hue_offset + t_val * 0.8) % 1.0
            r, g, b = hsv_to_rgb(hue, 1.0, 1.0)
            pen.pencolor(r, g, b)
            pen.pensize(3)
            pen.penup()
            pen.goto(prev_point[0], prev_point[1])
            pen.pendown()
            pen.goto(point[0], point[1])
            prev_point = point
        pen.penup()

        # --- 画标题 ---
        pen.goto(0, 320)
        pen.pencolor("white")
        pen.write("德卡斯特里奥算法 · 贝塞尔曲线", align="center",
                  font=("微软雅黑", 18, "bold"))
        pen.goto(0, 290)
        hue = (hue_offset + 0.5) % 1.0
        r, g, b = hsv_to_rgb(hue, 1.0, 1.0)
        pen.pencolor(r, g, b)
        pen.write("四个控制点绕圆运动，贝塞尔曲线随之起舞",
                  align="center", font=("微软雅黑", 12, "normal"))

        turtle.update()
        hue_offset += 0.005  # 颜色缓慢旋转

    turtle.done()

main()
