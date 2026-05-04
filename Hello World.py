# Hello World.py - 超级炫酷贝塞尔曲线
# 双击运行，给养老院老头们开开眼！

import turtle
import math
import colorsys

def interpolate_color(t):
    """彩虹渐变色"""
    hue = (t * 0.8) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (r, g, b)

def hex_color(r, g, b):
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

def bezier_point(t, points):
    temp = [list(p) for p in points]
    n = len(temp)
    for r in range(1, n):
        for i in range(n - r):
            temp[i][0] = (1 - t) * temp[i][0] + t * temp[i + 1][0]
            temp[i][1] = (1 - t) * temp[i][1] + t * temp[i + 1][1]
    return temp[0]

def draw_star(x, y, size, color):
    """画星星"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.pensize(1)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()

def draw_spiral(cx, cy, turns, radius, color):
    """画螺旋装饰"""
    turtle.penup()
    turtle.goto(cx, cy)
    turtle.pencolor(color)
    turtle.pensize(1)
    turtle.pendown()
    for i in range(turns * 36):
        angle = i * 10
        r = radius * i / (turns * 36)
        x = cx + r * math.cos(math.radians(angle))
        y = cy + r * math.sin(math.radians(angle))
        turtle.goto(x, y)
    turtle.penup()

def draw_bezier_rainbow(points, steps=150):
    """彩虹渐变色贝塞尔曲线"""
    turtle.pensize(4)
    turtle.penup()
    start = bezier_point(0, points)
    turtle.goto(start[0], start[1])
    turtle.pendown()
    for i in range(1, steps + 1):
        t = i / steps
        color = interpolate_color(t)
        turtle.pencolor(color)
        x, y = bezier_point(t, points)
        turtle.goto(x, y)
    turtle.penup()

def draw_double_bezier(points1, points2, steps=120):
    """画双重曲线形成丝带效果"""
    for i in range(steps):
        t = i / steps
        x1, y1 = bezier_point(t, points1)
        x2, y2 = bezier_point(t, points2)
        color = interpolate_color(t * 1.2)
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pencolor(color)
        turtle.pensize(2)
        turtle.pendown()
        turtle.goto(x2, y2)
    turtle.penup()

def draw_glow_dots(points, count=12):
    """沿曲线画发光点"""
    for i in range(count):
        t = i / (count - 1)
        x, y = bezier_point(t, points)
        color = interpolate_color(t * 1.5)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pencolor(color)
        turtle.fillcolor(color)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(4)
        turtle.end_fill()
        turtle.penup()

def write_flashy_title():
    """炫酷标题"""
    turtle.penup()
    turtle.goto(0, 290)
    turtle.pencolor("#FFD700")
    turtle.write("✨ 奶 奶 的 贝 塞 尔 曲 线 ✨", align="center",
                 font=("微软雅黑", 24, "bold"))
    turtle.goto(0, 260)
    turtle.pencolor("#FF69B4")
    turtle.write("Bezier Curve - Super Cool Edition", align="center",
                 font=("Courier New", 14, "italic"))

def draw_floating_circles():
    """背景装饰圆"""
    positions = [(-300, 200), (300, 250), (-350, -150), (280, -200),
                 (-200, -250), (200, -280), (-380, 0), (380, 50)]
    for i, (x, y) in enumerate(positions):
        hue = (i * 0.12) % 1.0
        turtle.penup()
        turtle.goto(x, y)
        turtle.pencolor(hex_color(*colorsys.hsv_to_rgb(hue, 0.4, 0.5)))
        turtle.pensize(1)
        turtle.pendown()
        for _ in range(36):
            turtle.circle(25, 10)
        turtle.penup()

def draw_grid():
    """背景网格"""
    turtle.pencolor("#1a1a2e")
    turtle.pensize(0.5)
    for x in range(-400, 401, 100):
        turtle.penup()
        turtle.goto(x, 300)
        turtle.pendown()
        turtle.goto(x, -300)
    for y in range(-300, 301, 100):
        turtle.penup()
        turtle.goto(-400, y)
        turtle.pendown()
        turtle.goto(400, y)
    turtle.penup()

def draw_starry_sky():
    """星空背景"""
    import random
    turtle.pensize(1)
    for _ in range(50):
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        size = random.randint(1, 3)
        brightness = random.randint(3, 8) / 10.0
        color = hex_color(brightness, brightness, brightness * 1.2)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pencolor(color)
        turtle.fillcolor(color)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()
        turtle.penup()

def draw_sparkle_trail(points, sparkles=20):
    """沿曲线撒亮点"""
    for i in range(sparkles):
        t = i / (sparkles - 1)
        x, y = bezier_point(t, points)
        color = interpolate_color(t + 0.2)
        offset_x = (i % 3 - 1) * 10
        offset_y = ((i * 7) % 3 - 1) * 8
        draw_star(x + offset_x, y + offset_y, 3, hex_color(*color))

def main():
    turtle.setup(900, 700)
    turtle.speed(0)
    turtle.tracer(0, 0)
    turtle.bgcolor("#0a0a1a")
    turtle.title("奶奶的超级炫酷贝塞尔曲线")
    turtle.colormode(1.0)

    # 背景
    draw_grid()
    draw_starry_sky()
    draw_floating_circles()

    # 标题
    write_flashy_title()

    # 主曲线
    main_curve = [
        (-280, -80),    # 起点
        (-180, 180),    # 控制点1
        (80, 60),       # 控制点2
        (280, -60),     # 终点
    ]

    # 副曲线
    sub_curve = [
        (-280, -60),
        (-180, 200),
        (80, 80),
        (280, -40),
    ]

    # 第三条曲线
    curve3 = [
        (-300, -200),
        (-150, 50),
        (150, -220),
        (300, 30),
    ]

    # 螺旋装饰
    draw_spiral(-350, 220, 3, 60, "#FFD700")
    draw_spiral(350, -220, 3, 60, "#FF69B4")
    draw_spiral(350, 230, 2, 40, "#00CED1")
    draw_spiral(-350, -230, 2, 40, "#7B68EE")

    # 画曲线
    draw_bezier_rainbow(main_curve)
    draw_bezier_rainbow(sub_curve)
    draw_bezier_rainbow(curve3)

    # 发光点
    draw_glow_dots(main_curve, 15)
    draw_glow_dots(sub_curve, 12)
    draw_glow_dots(curve3, 14)

    # 撒星星
    draw_sparkle_trail(main_curve, 20)
    draw_sparkle_trail(curve3, 18)

    # 角落大星星
    draw_star(-360, 280, 15, "#FFD700")
    draw_star(360, 280, 15, "#FFD700")
    draw_star(-360, -280, 12, "#FF69B4")
    draw_star(360, -280, 12, "#FF69B4")

    # 底部签名
    turtle.penup()
    turtle.goto(0, -290)
    turtle.pencolor("#888888")
    turtle.write("by wsudiyu-spec · 养老院最强 · 双击运行！",
                 align="center", font=("微软雅黑", 10, "italic"))

    turtle.hideturtle()
    turtle.update()
    turtle.done()

main()
