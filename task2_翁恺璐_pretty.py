#WordCloud.py
import jieba 
import wordcloud

# 定义文件路径
file_path = "D:\\PYECourse\\paper.txt.txt"
stopwords_path = "D:\\PYECourse\\stopwords.txt"  # 哈工大停用词表文件
output_path = "D:\\PYECourse\\wordcloud.png"

# 加载停用词表文件，合并手动停用词
def load_stopwords(stopwords_file):
    stopwords = {
        "具备", "得到", "已经","体现","认为","不是","可以","需要",
        "通过","我国","尝试","探索","推测","表现","这是","过程",
        "意味","这种","那些","成为","出来","没有","存在","追求","出现",
        "使用","出现","进行","那些","形成","发展","认同","独特","融合",
    }
    # 读取外部停用词表，合并到集合中
    try:
        with open(stopwords_file, "r", encoding="utf-8") as f:  
            for line in f:
                word = line.strip()
                if word:  # 跳过空行，避免加入空字符串
                    stopwords.add(word)
        print(f"成功加载外部停用词表，累计停用词数量：{len(stopwords)}")
    except FileNotFoundError:
        print(f"未找到外部停用词表 {stopwords_file}，仅使用手动停用词")
    # 返回合并后的停用词集合
    return stopwords

try:
    # 加载停用词表，包含手动+外部的所有停用词
    stop_words = load_stopwords(stopwords_path)

    # 读取文件
    with open(file_path, "r", encoding="utf-8") as f:
        t = f.read()
    
    # 原有分词和停用词过滤
    ls = jieba.lcut(t)
    # 过滤条件：非停用词,非空字符串,去除纯空格字符,去除单个字符的词
    filtered_ls = [word for word in ls if word not in stop_words and word.strip() and len(word.strip()) > 1]
    txt = " ".join(filtered_ls) 
    
    # 设置词云的字体、大小、背景色，限制词云显示的最大词汇数50,关闭词汇组合，避免重复显示拆分词汇生成并保存词云
    w = wordcloud.WordCloud(font_path="msyh.ttc",width=1000, height=700, background_color="white",max_words=50,collocations=False)
    w.generate(txt)
    w.to_file(output_path)
    print(f"词云生成成功！保存路径：{output_path}")

except FileNotFoundError:
    # 捕获文件未找到异常，打印指定提示语
    print("请检查目录下是否存在paper.txt文件")