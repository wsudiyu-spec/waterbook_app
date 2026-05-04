from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Line, Tab
from pyecharts.globals import ThemeType

# ====================== 数据 ======================
age_labels = ["90岁以上", "80-89岁", "70-79岁", "60-69岁", "50-59岁", "40-49岁", "40岁以下"]
age_numbers = [13, 88, 100, 38, 10, 1, 0]  # 总计约250人
age_percent = ["5%", "35%", "40%", "15%", "4%", "0.4%", "0%"]

# ====================== 饼图：年龄结构占比 ======================
pie = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width="1000px", height="600px"))
    .add(
        series_name="水书先生年龄分布",
        data_pair=list(zip(age_labels, age_numbers)),
        radius=["30%", "70%"],  # 环形图
        label_opts=opts.LabelOpts(formatter="{b}: {c}人 ({d}%)")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="水族水书先生年龄结构分布图（2025年，全国精通级）",
            subtitle="总计约250人 | 平均年龄70岁+ | 传承严重断层",
            title_textstyle_opts=opts.TextStyleOpts(font_size=18)
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item"),
        legend_opts=opts.LegendOpts(pos_left="left", orient="vertical")
    )
)

# ====================== 柱状图：人数对比 ======================
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width="1000px", height="600px"))
    .add_xaxis(age_labels)
    .add_yaxis("水书先生人数", age_numbers)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="水书先生各年龄段人数统计"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        visualmap_opts=opts.VisualMapOpts(max_=110, min_=0)
    )
)

# ====================== 组合成一个HTML文件（可切换查看） ======================
tab = Tab()
tab.add(pie, "年龄结构占比（饼图）")
tab.add(bar, "各年龄段人数（柱状图）")

# 生成HTML
tab.render("水族水书先生年龄结构可视化.html")
print("✅ 图表已生成：水族水书先生年龄结构可视化.html")