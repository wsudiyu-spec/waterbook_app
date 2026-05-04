# 水族水书文化可视化 Web 项目

## 项目概述
这是一个关于水族水书文化的数据可视化Web项目，包含以下内容：
- 水书先生年龄结构可视化（饼图和柱状图）
- 水书仪式信息交互展示（Streamlit应用）

## 项目结构
```
deploy_web/
├── html/                           # 静态HTML页面
│   └── 水族水书先生年龄结构可视化.html
├── scripts/                        # Python脚本
│   ├── from pyecharts import options as opts.py   # 生成图表的脚本
│   └── clickable_demo.py           # Streamlit交互展示脚本
├── assets/                         # 资源文件夹（如需添加图片、视频等）
├── README.md                       # 本文件
└── requirements.txt                # Python依赖包
```

## 部署说明

### 方式一：静态HTML部署（推荐）
直接将 `html/` 文件夹下的HTML文件上传到Web服务器即可。

**服务器要求：**
- 任何支持静态文件的Web服务器（Nginx、Apache、IIS等）
- 无需安装Python环境

**部署步骤：**
1. 将 `html/` 文件夹内容上传到服务器的网站根目录
2. 配置Web服务器指向该目录
3. 通过浏览器访问HTML文件

**优点：**
- 简单快速
- 无需服务器端编程
- 性能好

### 方式二：Streamlit应用部署
如果需要交互式展示功能，可以部署Streamlit应用。

**服务器要求：**
- Python 3.7+
- 需要安装相关Python包

**部署步骤：**
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 运行Streamlit应用：
   ```bash
   streamlit run scripts/clickable_demo.py
   ```

3. 配置反向代理（可选）：
   - Nginx配置示例见下方

## Python依赖包

核心依赖：
```
streamlit>=1.0.0
pyecharts>=2.0.0
```

## Nginx配置示例

### 静态HTML部署
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    root /path/to/deploy_web/html;
    index 水族水书先生年龄结构可视化.html;
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Streamlit应用（通过Nginx反向代理）
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## 文件说明

### 水族水书先生年龄结构可视化.html
- 使用pyecharts生成的静态图表
- 包含饼图和柱状图两个标签页
- 展示水书先生的年龄分布数据
- 数据：总计约250人，平均年龄70岁+

### clickable_demo.py
- Streamlit交互式Web应用
- 展示水书仪式信息可视化
- 包含图片展示和视频播放功能
- 需要配置本地图片路径

## 注意事项

1. **HTML文件**：可以直接在浏览器打开，无需服务器
2. **Streamlit应用**：需要修改 `clickable_demo.py` 中的文件路径
3. **外部资源**：HTML文件引用了pyecharts的CDN资源，需要网络连接
4. **图片资源**：Streamlit应用需要配置正确的图片路径

## 联系方式
如有问题，请联系项目维护者。
