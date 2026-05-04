# 快速部署指南

## 方式一：静态HTML部署（最简单）

### 步骤：
1. 将整个 `deploy_web` 文件夹上传到你的服务器
2. 确保服务器支持静态文件（Nginx、Apache、IIS等）
3. 访问HTML文件即可

### 文件说明：
- `html/水族水书先生年龄结构可视化.html` - 在线版本（需要网络连接CDN）
- `html/index_offline.html` - 离线版本（使用本地JS文件，推荐）

### 推荐做法：
使用 `index_offline.html`，它不依赖外部CDN，可以完全离线运行。

## 方式二：Streamlit应用部署

### 前提条件：
- 服务器已安装 Python 3.7+
- 服务器已安装 pip

### 步骤：

1. **安装依赖**
```bash
cd /path/to/deploy_web
pip install -r requirements.txt
```

2. **修改文件路径**
编辑 `scripts/clickable_demo.py` 文件，将以下路径改为你服务器上的实际路径：
```python
bg_img_path = r"你的图片路径"
video_path = r"你的视频路径"
img1_path = r"图片1路径"
img2_path = r"图片2路径"
img3_path = r"图片3路径"
```

3. **运行应用**
```bash
cd scripts
streamlit run clickable_demo.py
```

4. **配置防火墙**
确保服务器的8501端口已开放（或自定义端口）

5. **后台运行（可选）**
```bash
nohup streamlit run clickable_demo.py &
```

### 使用systemd管理（推荐）

创建服务文件 `/etc/systemd/system/streamlit.service`：
```ini
[Unit]
Description=Streamlit Application
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/deploy_web/scripts
ExecStart=/path/to/python -m streamlit run clickable_demo.py
Restart=always

[Install]
WantedBy=multi-user.target
```

启动服务：
```bash
sudo systemctl start streamlit
sudo systemctl enable streamlit
```

## 常见问题

### Q: HTML文件显示空白？
A: 检查是否加载了echarts.js文件。如果使用在线版本，确保服务器可以访问外网。

### Q: Streamlit应用无法访问？
A: 检查防火墙设置，确保端口已开放。使用 `streamlit run --server.port 8501` 指定端口。

### Q: 图片/视频无法显示？
A: 确保文件路径正确，并且Streamlit应用有读取权限。

## 性能优化建议

1. **静态HTML**：
   - 使用CDN加速（如果在线）
   - 启用Gzip压缩
   - 设置浏览器缓存

2. **Streamlit应用**：
   - 使用Nginx反向代理
   - 启用HTTPS
   - 配置负载均衡（多实例）

## 安全建议

1. 使用HTTPS加密传输
2. 配置防火墙规则
3. 定期更新依赖包
4. Streamlit应用建议添加访问控制
