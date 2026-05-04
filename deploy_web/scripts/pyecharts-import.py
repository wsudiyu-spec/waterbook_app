from pyecharts import options as opts
from pyecharts.charts import Sankey

# 数据准备：按层级拆分的节点和流向数据
nodes = [
    {"name": "仪式系统"},
    {"name": "端节祭祀"},
    {"name": "婚嫁择吉"},
    {"name": "丧葬祈福"},
    {"name": "天文择日"},
    {"name": "核心文字符号(字)"},
    {"name": "关键实体媒介(物)"},
    {"name": "空间场景元素(境)"},
    {"name": "祖"}, {"name": "祭"}, {"name": "鱼"}, {"name": "年"},
    {"name": "铜鼓纹理"}, {"name": "牛角杯形态"}, {"name": "鱼包韭菜结构"},
    {"name": "宗祠建筑构件"}, {"name": "长席阵列"}, {"name": "祭坛布局"},
    {"name": "和合"}, {"name": "繁衍"}, {"name": "吉日历法字"},
    {"name": "伴嫁竹篮编织纹"}, {"name": "特定红绳结绳法"},
    {"name": "迎亲路径图谱"}, {"name": "堂屋红黑色彩构成"},
    {"name": "灵魂"}, {"name": "指路"}, {"name": "阴阳转换字"},
    {"name": "引魂幡剪纸轮廓"}, {"name": "法师芦笙"}, {"name": "纸扎"},
    {"name": "墓地风水方位图"}, {"name": "丧葬行进路线"},
    {"name": "星宿"}, {"name": "天干地支"}, {"name": "节气字"},
    {"name": "罗盘刻度"}, {"name": "历书排版"}, {"name": "算筹排列"},
    {"name": "星空方位映射图"}, {"name": "祭天高台阶梯"}
]

# 定义节点间的流向关系
links = [
    # 仪式系统 -> 各仪式
    {"source": "仪式系统", "target": "端节祭祀", "value": 1},
    {"source": "仪式系统", "target": "婚嫁择吉", "value": 1},
    {"source": "仪式系统", "target": "丧葬祈福", "value": 1},
    {"source": "仪式系统", "target": "天文择日", "value": 1},
    # 各仪式 -> 三类元素
    {"source": "端节祭祀", "target": "核心文字符号(字)", "value": 1},
    {"source": "端节祭祀", "target": "关键实体媒介(物)", "value": 1},
    {"source": "端节祭祀", "target": "空间场景元素(境)", "value": 1},
    {"source": "婚嫁择吉", "target": "核心文字符号(字)", "value": 1},
    {"source": "婚嫁择吉", "target": "关键实体媒介(物)", "value": 1},
    {"source": "婚嫁择吉", "target": "空间场景元素(境)", "value": 1},
    {"source": "丧葬祈福", "target": "核心文字符号(字)", "value": 1},
    {"source": "丧葬祈福", "target": "关键实体媒介(物)", "value": 1},
    {"source": "丧葬祈福", "target": "空间场景元素(境)", "value": 1},
    {"source": "天文择日", "target": "核心文字符号(字)", "value": 1},
    {"source": "天文择日", "target": "关键实体媒介(物)", "value": 1},
    {"source": "天文择日", "target": "空间场景元素(境)", "value": 1},
    # 核心文字符号 -> 具体字
    {"source": "核心文字符号(字)", "target": "祖", "value": 1},
    {"source": "核心文字符号(字)", "target": "祭", "value": 1},
    {"source": "核心文字符号(字)", "target": "鱼", "value": 1},
    {"source": "核心文字符号(字)", "target": "年", "value": 1},
    {"source": "核心文字符号(字)", "target": "和合", "value": 1},
    {"source": "核心文字符号(字)", "target": "繁衍", "value": 1},
    {"source": "核心文字符号(字)", "target": "吉日历法字", "value": 1},
    {"source": "核心文字符号(字)", "target": "灵魂", "value": 1},
    {"source": "核心文字符号(字)", "target": "指路", "value": 1},
    {"source": "核心文字符号(字)", "target": "阴阳转换字", "value": 1},
    {"source": "核心文字符号(字)", "target": "星宿", "value": 1},
    {"source": "核心文字符号(字)", "target": "天干地支", "value": 1},
    {"source": "核心文字符号(字)", "target": "节气字", "value": 1},
    # 关键实体媒介 -> 具体物
    {"source": "关键实体媒介(物)", "target": "铜鼓纹理", "value": 1},
    {"source": "关键实体媒介(物)", "target": "牛角杯形态", "value": 1},
    {"source": "关键实体媒介(物)", "target": "鱼包韭菜结构", "value": 1},
    {"source": "关键实体媒介(物)", "target": "伴嫁竹篮编织纹", "value": 1},
    {"source": "关键实体媒介(物)", "target": "特定红绳结绳法", "value": 1},
    {"source": "关键实体媒介(物)", "target": "引魂幡剪纸轮廓", "value": 1},
    {"source": "关键实体媒介(物)", "target": "法师芦笙", "value": 1},
    {"source": "关键实体媒介(物)", "target": "纸扎", "value": 1},
    {"source": "关键实体媒介(物)", "target": "罗盘刻度", "value": 1},
    {"source": "关键实体媒介(物)", "target": "历书排版", "value": 1},
    {"source": "关键实体媒介(物)", "target": "算筹排列", "value": 1},
    # 空间场景元素 -> 具体境
    {"source": "空间场景元素(境)", "target": "宗祠建筑构件", "value": 1},
    {"source": "空间场景元素(境)", "target": "长席阵列", "value": 1},
    {"source": "空间场景元素(境)", "target": "祭坛布局", "value": 1},
    {"source": "空间场景元素(境)", "target": "迎亲路径图谱", "value": 1},
    {"source": "空间场景元素(境)", "target": "堂屋红黑色彩构成", "value": 1},
    {"source": "空间场景元素(境)", "target": "墓地风水方位图", "value": 1},
    {"source": "空间场景元素(境)", "target": "丧葬行进路线", "value": 1},
    {"source": "空间场景元素(境)", "target": "星空方位映射图", "value": 1},
    {"source": "空间场景元素(境)", "target": "祭天高台阶梯", "value": 1},
]

# 生成桑基图
c = (
    Sankey()
    .add(
        series_name="水书仪式元素",
        nodes=nodes,
        links=links,
        linestyle_opt=opts.LineStyleOpts(opacity=0.3, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="水书仪式系统视觉元素桑基图"))
    .render("water_shu_sankey.html")
)

print("桑基图已生成：water_shu_sankey.html")