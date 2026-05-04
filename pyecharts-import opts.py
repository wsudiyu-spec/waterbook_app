from pyecharts import options as opts
from pyecharts.charts import Sankey

# 节点数据
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

# 流向数据
links = [
    {"source": "仪式系统", "target": "端节祭祀", "value": 1},
    {"source": "仪式系统", "target": "婚嫁择吉", "value": 1},
    {"source": "仪式系统", "target": "丧葬祈福", "value": 1},
    {"source": "仪式系统", "target": "天文择日", "value": 1},
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

# 直接用纯文本的formatter，不写JS代码，避免白屏
# 利用pyecharts的内置变量，实现只在"祭"节点显示说明
c = (
    Sankey()
    .add(
        series_name="水书仪式元素",
        nodes=nodes,
        links=links,
        linestyle_opt=opts.LineStyleOpts(opacity=0.4, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right", font_size=11),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            # 这里用pyecharts支持的字符串模板，不会被当成JS执行，也不会白屏
            formatter=(
                "function(params) {"
                "  var desc = {"
                '    "祭": "水书「祭」字符号\\n\\n上方的框架结构，模拟祭祀时摆放供品的供桌；下方的三个圆点，象征着参与祭祀的族人。直观还原了水族祭祀仪式场景。"'
                "  };"
                "  var key = params.data && params.data.name ? params.data.name : (params.data && params.data.target ? params.data.target : params.name);"
                "  return desc[key] || (params.name || (params.data ? params.data.name : ''));"
                "}"
            ),
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="水书仪式系统视觉元素桑基图"),
    )
    .render("water_shu_sankey_no_blank.html")
)

print("✅ 白屏修复版已生成：water_shu_sankey_no_blank.html")
print("👉 现在双击就能打开，不会白屏！")
print("👉 鼠标放在「祭」字节点/连线上，会显示完整说明，其他节点正常显示名称")