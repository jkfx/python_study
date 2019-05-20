import jieba
import wordcloud
from scipy.misc import imread
mk = imread('xz.png')
f = open('新时代中国特色社会主义.txt', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path='C:/Windows/Fonts/msyh.ttc',
                        width=1000, height=700,
                        background_color='white', mask=mk)
w.generate(txt)
w.to_file('govrpt_5.png')
