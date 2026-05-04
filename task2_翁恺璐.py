#词频统计
import jieba
txt = open("D:\\PYECourse\\paper.txt.txt", "r", encoding="utf-8").read() 
excludes = {"作为", "进行", "研究", "借鉴"}
words=jieba.lcut(txt)
counts = {} # dict()
for word in words:
    if len(word)==1 or word in excludes:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items=list(counts.items())

# 以词频降序排序
items.sort(key=lambda x : x[1], reverse = True)
for i in range(12):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))

import wordcloud
c = wordcloud.WordCloud(width=1000, height=700, background_color="white")
c.generate("wordcloud by Python")
c.to_file("D:\\PYECourse\\wordcloud.png")