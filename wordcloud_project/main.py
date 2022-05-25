from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image

with open('words.txt', 'r', encoding='utf-8') as text:
    with PIL.Image.open('boris.png') as pic:
        Word_pic = np.array(pic)
        color_map = ImageColorGenerator(Word_pic)
        wc = WordCloud(mask=Word_pic,
                       background_color='white',
                       contour_color='grey',
                       contour_width=1,
                       min_font_size=3,
                       height=600,
                       width=400,
                       max_words=1000).generate(text.read())

wc.recolor(color_func=color_map)
wc.to_file('wordcloud.png')
