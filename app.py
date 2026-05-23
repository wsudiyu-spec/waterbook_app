"""
水书仪式信息可视化 — Flask Web 应用
"""
from flask import Flask, render_template, send_file
from pathlib import Path
import base64

app = Flask(__name__)

# ============================================================
# 素材路径 — 均在 resource/ 下按用途分类
# ============================================================
RES = Path(__file__).resolve().parent / "resource"

BG_IMG  = RES / "page1" / "bg.png"
VIDEO   = RES / "page1" / "video.mp4"
IMG1    = RES / "page2" / "card1.png"
IMG2    = RES / "page2" / "card2.png"
IMG3    = RES / "page2" / "card3.png"
PAGE4   = RES / "page4" / "viz.jpg"
SCENE   = RES / "scene"
ELEM    = RES / "element"
BGM     = RES / "bg_music" / "清庙.mp3"

SCENE_CAPTIONS = [
    "守端与祭祖 — 端夜至凌晨，驱邪纳福，祭拜先祖",
    "端坡赛马 — 午后高潮，骑手驰骋端坡，万众呐喊",
    "邀端与宴客 — 清晨至午间，迎宾设宴，共庆丰年",
    "铜鼓与歌舞 — 全天不息，铜鼓震天，歌舞联欢",
]
ELEM_CAPTIONS = [
    "铜鼓纹样 — 水族铜鼓上镌刻的古老图腾符号，象征天地沟通与祖先庇佑",
    "牛角图腾 — 端节祭祀中悬挂的牛角饰物，寓意丰收与族群力量",
    "鱼包韭菜 — 端节祭祖忌荤食素，唯独鱼被视为 “素”，祭祖仪式中最重要的祭品",
]


def _img_to_b64(p):
    try:
        return base64.b64encode(p.read_bytes()).decode()
    except Exception:
        return None


def _scan_images(folder, count):
    """从文件夹取排序后的前 count 个图片，返回 (b64, mime) 列表"""
    exts = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}
    mime_map = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
                '.gif': 'image/gif', '.webp': 'image/webp'}
    files = sorted([f for f in folder.iterdir() if f.suffix.lower() in exts])
    result = []
    for f in files[:count]:
        result.append({
            'b64': _img_to_b64(f) or '',
            'mime': mime_map.get(f.suffix.lower(), 'image/png'),
        })
    return result


@app.route("/")
def index():
    scene_imgs = _scan_images(SCENE, 4)
    elem_imgs  = _scan_images(ELEM, 3)
    return render_template(
        "index.html",
        bg_b64=_img_to_b64(BG_IMG),
        img1_b64=_img_to_b64(IMG1),
        img2_b64=_img_to_b64(IMG2),
        img3_b64=_img_to_b64(IMG3),
        page4_b64=_img_to_b64(PAGE4),
        video_exists=VIDEO.exists(),
        bgm_exists=BGM.exists(),
        scene_images=[e['b64'] for e in scene_imgs],
        scene_count=len(scene_imgs),
        scene_captions=SCENE_CAPTIONS,
        elem_b64=[e['b64'] for e in elem_imgs],
        elem_mime=[e['mime'] for e in elem_imgs],
        elem_captions=ELEM_CAPTIONS,
    )


@app.route("/video")
def video():
    if VIDEO.exists():
        return send_file(str(VIDEO), mimetype="video/mp4")
    return "", 404


@app.route("/bgmusic")
def bgmusic():
    if BGM.exists():
        return send_file(str(BGM), mimetype="audio/mpeg")
    return "", 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
