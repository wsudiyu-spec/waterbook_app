import streamlit as st
import base64
import logging
import textwrap
import os

# 页面配置
st.set_page_config(
    page_title="水书仪式信息可视化",
    page_icon="🖼️",
    layout="wide"
)

# 标题
# st.title("🖼️ 水书仪式信息可视化交互展示")
# st.markdown("---")

# 图片转base64（带异常处理，找不到图不会崩溃）
def get_img_as_base64(file):
    try:
        with open(file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# ====================== 你只需要改这里的路径 ======================
bg_img_path = r"D:\3D大赛构思初稿\新建文件夹\水书仪式信息可视化_01.png"
video_path = r"D:\3D大赛构思初稿\水族端节1.mp4"

img1_path = r"D:\3D大赛构思初稿\jimeng-2026-04-27-5685.png"
img2_path = r"D:\3D大赛构思初稿\jimeng-2026-04-27-1003.png"
img3_path = r"D:\3D大赛构思初稿\jimeng-2026-04-27-3329.png"
# ==================================================================

img_b64 = get_img_as_base64(bg_img_path)
img1_b64 = get_img_as_base64(img1_path)
img2_b64 = get_img_as_base64(img2_path)
img3_b64 = get_img_as_base64(img3_path)

# 悬浮提示文字
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


bg_html = textwrap.dedent("""\
    <style>
    body{margin:0;padding:0;}
    .wrap{position:relative;width:100%;}
    .bigimg{width:100%;border-radius:14px;box-shadow:0 6px 24px rgba(0,0,0,0.1);display:block;}
    .hover-box{position:absolute;background:rgba(0,100,255,0.3);border:2px solid rgba(0,100,255,0.6);z-index:10;cursor:pointer;transition:background 0.3s;}
    .hover-box:hover{background:rgba(0,100,255,0.5);}
    .tooltip{position:absolute;background:rgba(0,0,0,0.88);color:#fff;padding:16px 20px;border-radius:10px;font-size:15px;line-height:1.8;display:none;z-index:9999;white-space:pre-line;min-width:200px;pointer-events:none;}
    </style>

    <div class="wrap" id="mainWrap">
        <img class="bigimg" src="data:image/png;base64,__IMG__">

        <div class="hover-box" style="left:5%; top:45%; width:4%; height:25%;" data-tooltip="box01"></div>
        <div class="hover-box" style="left:12%; top:45%; width:4%; height:25%;" data-tooltip="box02"></div>
        <div class="hover-box" style="left:19%; top:45%; width:4%; height:25%;" data-tooltip="box03"></div>
        <div class="hover-box" style="left:26%; top:45%; width:4%; height:25%;" data-tooltip="box04"></div>
        <div class="hover-box" style="left:33%; top:45%; width:3%; height:25%;" data-tooltip="box05"></div>
        <div class="hover-box" style="left:38%; top:40%; width:12%; height:30%;" data-tooltip="box06"></div>
        <div class="hover-box" style="left:53%; top:45%; width:3%; height:25%;" data-tooltip="box07"></div>
        <div class="hover-box" style="left:58%; top:45%; width:3%; height:25%;" data-tooltip="box08"></div>
        <div class="hover-box" style="left:68%; top:45%; width:3%; height:25%;" data-tooltip="box09"></div>
        <div class="hover-box" style="left:73%; top:45%; width:3%; height:25%;" data-tooltip="box10"></div>
        <div class="hover-box" style="left:78%; top:45%; width:3%; height:25%;" data-tooltip="box11"></div>
        <div class="hover-box" style="left:83%; top:45%; width:3%; height:25%;" data-tooltip="box12"></div>
        <div class="hover-box" style="left:88%; top:45%; width:3%; height:25%;" data-tooltip="box13"></div>
        <div class="hover-box" style="left:93%; top:45%; width:3%; height:25%;" data-tooltip="box14"></div>

        <div class="tooltip" id="tooltip"></div>

        <script>
            const boxes = document.querySelectorAll('.hover-box');
            const tooltip = document.getElementById('tooltip');
            const wrap = document.getElementById('mainWrap');

            boxes.forEach(box => {
                box.addEventListener('mouseenter', (e) => {
                    const text = box.getAttribute('data-tooltip');
                    tooltip.innerText = text;
                    tooltip.style.display = 'block';
                });

                box.addEventListener('mousemove', (e) => {
                    const rect = wrap.getBoundingClientRect();
                    tooltip.style.left = (e.clientX - rect.left + 20) + 'px';
                    tooltip.style.top = (e.clientY - rect.top + 20) + 'px';
                });

                box.addEventListener('mouseleave', () => {
                    tooltip.style.display = 'none';
                });
            });
        </script>
    </div>
    """)

bg_html = bg_html.replace("__IMG__", img_b64)

st.markdown(bg_html, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 视频
st.subheader("🎥 水族文化科普视频")
st.markdown('''
<style>video{width:100%;max-width:1100px;border-radius:14px;margin:0 auto;}</style>
''', unsafe_allow_html=True)
if video_path and os.path.exists(video_path):
    st.video(video_path)
elif video_path:
    st.warning(f"⚠️ 视频文件不存在: {video_path}")

st.markdown("<br><br>", unsafe_allow_html=True)

# 底部三张图展示
st.subheader("🖼️ 水书文化细节视觉展示")
st.markdown("""
<style>
.card-img {
    height: 300px;
    width: 100%;
    object-fit: cover;
    object-position: center;
    border-radius: 14px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.13);
}
</style>
""", unsafe_allow_html=True)

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