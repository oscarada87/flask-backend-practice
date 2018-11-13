import sys, os
import jieba
jieba.tmp_dir = os.path.dirname(os.path.abspath(__file__)) + '/tmp'
import jieba.analyse
from wordcloud import WordCloud ,ImageColorGenerator
from scipy.misc import imread  # 處理圖的函数
from collections import Counter
import matplotlib.pyplot as plt
frame = imread('trump.png')  # 圖片
jieba.case_sensitive = True # 可控制對於詞彙中的英文部分是否為case sensitive, 預設False
stopwords = []
with open('stopWords.txt', 'r', encoding='UTF-8') as file:
    for data in file.readlines():
        data = data.strip()
        stopwords.append(data)

print(str(jieba.tmp_dir))
class jiebacut:
    def __init__(self, content):
        self.content = content
        self.data = []
    def cut(self,num):
#        seg_list = jieba.cut(self.content[num]['content'].replace(' ',''))
#        self.data.extend(seg_list)
        seg_list = jieba.analyse.extract_tags(self.content[num]['content'].replace(' ',''), topK=30, withWeight=True, allowPOS=())
        for i in range(0,len(seg_list)):
            self.data.append(seg_list[i][0])
        self.data = list(filter(lambda a: a not in stopwords and a != '\n', self.data))
    def make(self):
        for i in range(0, len(self.content)):
            self.cut(i)
        sorted(Counter(self.data).items(), key=lambda x:x[1], reverse=True)
        font = 'msjh.ttc'#chinese
        wc = WordCloud(background_color="white",font_path=font,mask=frame,max_font_size=200, random_state=42,stopwords=stopwords,max_words=500)#collocations=False
        wc.generate_from_frequencies(frequencies=Counter(self.data))
        image_colors = ImageColorGenerator(frame)#對應顏色
        plt.figure()
        plt.imshow(wc.recolor(color_func=image_colors))
        plt.axis('off')
        wc.to_file('test.png')#save