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

## Git 规则
- **仅本地使用，禁止 `git push`**
- 中文 commit message
- 不要提交可能含个人信息的文件
