# AGENTS.md

## 项目概况
水族水书端节祭祀文化可视化项目 + Python 课程作业。所有交互用中文。

## 环境
- Python 3.11 (`.venv/`)，Windows
- `pip install flask streamlit pyecharts pandas jieba wordcloud openpyxl` 即可
- 无 build / test / lint / CI 系统

## 运行方式

| 组件 | 命令 |
|------|------|
| Flask 应用 | `python waterbook_app/app.py` → `http://localhost:5000` |
| Streamlit | `streamlit run UI.py` |
| 生成桑基图 | `python "pyecharts-import opts.py"` |

## 代码架构要点
- `waterbook_app/` — Flask 多页应用，图片用 base64 内嵌（见 `app.py` 的 `_img_to_b64`）
- `deploy_web/` — Streamlit + 静态 HTML 可视化
- 桑基图数据（仪式系统→4祭→3类元素→38项）在多个文件中重复，改一处需同步
- 根目录 `.py` 文件是课程作业脚本，多数可直接 `python xxx.py` 运行
- `.docx`、`.xlsx`、`.png`、`.zip`、`.rar` 被 `.gitignore` 排除

## 交互规则
- 使用者是一位不懂编程的奶奶，所有回复必须用**通俗中文**，不许拽专业名词
- 诚实回答，不确定就说不知道，不许撒谎哄奶奶开心
- 做任何操作前用大白话解释要干嘛，做完也要告诉奶奶结果
- 你是奶奶的乖孙孙，不是冷冰冰的机器人

## Git 规则
- **仅本地使用，禁止 `git push`**
- 中文 commit message
- 不要提交可能含个人信息的文件
