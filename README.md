# 水书仪式信息可视化

Flask 多页 Web 应用，展示水族端节仪式的交互图谱、视觉元素图集和桑基图谱。

## 快速启动

```bash
cd waterbook_app
pip install flask
python app.py
# → http://localhost:5000
```

## 项目结构

```
waterbook_app/
├── app.py                  # Flask 应用，素材加载、路由
├── requirements.txt        # Flask>=2.0
├── README.md
├── resource/               # 所有素材 (带 project 走即可)
│   ├── page1/
│   │   ├── bg.png          # 主页背景大图 (全屏)
│   │   └── video.mp4       # 端节视频
│   ├── page2/
│   │   ├── card1.png       # 卡片1: 铜鼓纹样
│   │   ├── card2.png       # 卡片2: 牛角图腾
│   │   └── card3.png       # 卡片3: 鱼鸟纹饰
│   ├── scene/              # "端节-序" 弹窗四图
│   │   ├── scene1.png      # 端节全景
│   │   ├── scene2.png      # 祭祀布置
│   │   ├── scene3.png      # 仪式进行
│   │   └── scene4.png      # 青铜礼器
│   └── element/            # 页面2 卡片点击弹出的细节大图
│       ├── elem01.png      # 铜鼓纹样细节
│       ├── elem02.jpg      # 牛角图腾细节
│       └── elem03.png      # 鱼鸟纹饰细节
├── templates/
│   └── index.html          # Jinja2 单页模板 (3 页面切换)
└── static/
    ├── css/style.css       # 所有样式
    └── js/
        ├── main.js         # 片头动画、热区弹窗、视频、场景弹窗、元素弹窗
        └── sankey.js       # ECharts 桑基图
```

## 页面功能

| 页面 | 功能 |
|------|------|
| **page1 仪式图谱** | 全屏背景图 + 14 个热区(tooltip) + 片头标题动画(0~3.2s) + 播放圆点(视频弹窗) + 香炉烟雾 + "端节-序"场景弹窗(4图依次浮现) |
| **page2 视觉图集** | 3 张卡片，点击弹出元素细节大图 + 文字说明 |
| **page3 桑基图谱** | ECharts 桑基图(切换时自动 resize) |

## 交互说明

- **片头动画**: 0.3s 标题浮入，2.8s 虚化消散，3.2s 圆点+烟雾激活
- **视频弹窗**: 点藏青色圆点 → 打开，X/Esc/点遮罩 → 关闭，重开从 0 播放
- **场景弹窗("端节-序")**: 点击热区 → 标题 0.1s + 四图依次(0.8/2.0/3.2/4.5s) + 关闭按钮 5.5s
- **元素详情弹窗**: 点卡片 → 大图 0.3s + 说明 0.6s + 关闭按钮 1.0s
- **关闭**: 所有弹窗支持 X 按钮 / Esc / 点遮罩背景关闭

## 要改的内容

### 改文本
- `app.py` 的 `SCENE_CAPTIONS` — 场景弹窗四图说明
- `app.py` 的 `ELEM_CAPTIONS` — 元素详情弹窗说明
- `index.html` 里各 hot-box 的 `data-tip` — 热区 tooltip 文字

### 改图片
- 直接替换 `resource/` 下对应文件（保持文件名不变）
- 如需改名，同步改 `app.py` 的路径常量

### 改样式
- `style.css` — 热区位置(top/left/width/height)用百分比，动画时间在各 keyframes 和 transition-delay

## 路径说明

`app.py` 使用相对路径 `os.path.dirname(__file__)` 拼接 `resource/`，项目整体迁移无需改路径。
