#WordCloud1.py
import jieba 
import wordcloud
f = open("D:\\PYECourse\\paper.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
# 定义需要过滤的停用词
stop_words = {"是", "的", "等","与","也"}
# 过滤掉停用词和空字符
filtered_ls = [word for word in ls if word not in stop_words and word.strip()]
txt = " ".join(filtered_ls) 
w = wordcloud.WordCloud(font_path="msyh.ttc",width=1000, height=700, background_color="white",max_words=15)
w.generate(txt)
w.to_file("D:\\PYECourse\\wordcloud.png")