import streamlit as st
import base64

st.set_page_config(
    page_title="水书仪式信息可视化",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ 水书仪式信息可视化交互展示")
st.markdown("---")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 你的本地路径
bg_img_path = r"D:\研1\3D大赛构思初稿\新建文件夹\水书仪式信息可视化_01.png"
video_path = r"D:\研1\3D大赛构思初稿\水族端节1.mp4"
img_b64 = get_img_as_base64(bg_img_path)

# 下方三张图片路径
img1_path = r"D:\研1\3D大赛构思初稿\jimeng-2026-04-27-5685.png"
img2_path = r"D:\研1\3D大赛构思初稿\jimeng-2026-04-27-1003.png"
img3_path = r"D:\研1\3D大赛构思初稿\jimeng-2026-04-27-3329.png"

# 弹窗内容
text_top = """端节是水族最隆重的传统年节，
相当于汉族的春节。
主要流行于贵州三都、荔波等水族聚居区。
节日从农历八月持续到十月，
分批轮流进行，
被誉为世界上历时最长的年节。"""

text_bottom = """📊 非遗传承人群年龄结构分布
────────────────────────
70–79岁 │ ████████████████████████  40%（100人）
80–89岁 │ ███████████████████      35%（88人）
60–69岁 │ ██████                   20%
50–59岁 │ ▏                         5%
50岁以下│ ▏                         近乎断层
40岁以下│ 　                        0人
────────────────────────
📌 60岁以上合计占比：95%"""

html = f'''
<style>
.wrap{{position:relative;width:100%;max-width:1400px;margin:0 auto;}}
.bigimg{{width:100%;border-radius:12px;box-shadow:0 5px 20px #0002;}}
.top_zone{{position:absolute;left:0;top:0;width:100%;height:66%;z-index:10;}}
.bot_zone{{position:absolute;left:0;top:66%;width:100%;height:34%;z-index:10;}}
.tip1,.tip2{{
    position:absolute;
    background:rgba(0,0,0,0.85);
    color:#fff;
    padding:14px 18px;
    border-radius:10px;
    font-size:14px;
    line-height:1.7;
    display:none;
    pointer-events:none;
    z-index:9999;
    white-space:pre-line;
    min-width:350px;
}}
.top_zone:hover ~ .tip1{{display:block;}}
.bot_zone:hover ~ .tip2{{display:block;}}
</style>

<div class="wrap" onmousemove="
    let x = event.offsetX + 20;
    let y = event.offsetY + 20;
    document.querySelector('.tip1').style.left = x+'px';
    document.querySelector('.tip1').style.top = y+'px';
    document.querySelector('.tip2').style.left = x+'px';
    document.querySelector('.tip2').style.top = y+'px';
">
    <img class="bigimg" src="data:image/png;base64,{img_b64}">
    <div class="top_zone"></div>
    <div class="bot_zone"></div>
    <div class="tip1">{text_top}</div>
    <div class="tip2">{text_bottom}</div>
</div>
'''

st.markdown(html, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 视频
st.subheader("🎥 水族文化科普视频")
st.markdown('''
<style>video{width:100%;max-width:1000px;border-radius:12px;display:block;margin:0 auto;}</style>
''',unsafe_allow_html=True)
st.video(video_path)

st.markdown("<br><br>", unsafe_allow_html=True)

# ====================== 底部三张图：最终完美版 ======================
st.subheader("🖼️ 水书文化细节视觉展示")
st.markdown("""
<style>
/* 核心：填满框 + 统一高度 + 自动裁剪 */
.card-img {
    height: 280px;
    width: 100%;
    object-fit: cover;   /* 填满框，自动裁剪 */
    object-position: center; /* 居中裁剪 */
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

img1_b64 = get_img_as_base64(img1_path)
img2_b64 = get_img_as_base64(img2_path)
img3_b64 = get_img_as_base64(img3_path)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<img src="data:image/png;base64,{img1_b64}" class="card-img">', unsafe_allow_html=True)
    st.caption("水书文字符号")
with c2:
    st.markdown(f'<img src="data:image/png;base64,{img2_b64}" class="card-img">', unsafe_allow_html=True)
    st.caption("祭祀仪式形态")
with c3:
    st.markdown(f'<img src="data:image/png;base64,{img3_b64}" class="card-img">', unsafe_allow_html=True)
    st.caption("水族传统纹样")