import wordcloud, jieba
txt = 'Matplotlib是Python中最常用的可视化工具之一，功能非常强大，可以方便的绘制折线图、条形图、柱形' \
      '图、散点图、盒图等2D图形，还可以绘制基本的3D图形。Matplotlib是Python数据可视化的基础库，在它的' \
      '基础上又衍生出了多个数据可视化的工具集（如Seaborn，将在后面的文章中讲到）。'

w = wordcloud.WordCloud(width=1000,
                        background_color='white',
                        height=700,
                        font_path='C:/Windows/Fonts/msyh.ttc')
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('fx.png')
