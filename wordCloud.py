#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""使用词云进行文字内容分析"""

import sys
import os
from os import path

# 自定义类路径
path_pref = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 加入到系统路径中
# sys.path.append(path_pref + r'\utils')


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import DateUtil

# 分析文字，生成对应的图片
"""
wordContentFileName：存放文本内容，必须放到wordfile下面
needCreateJpg:true，生成jpg图片，默认不生成
jpgName：图片名称，默认是时间
"""


def createJpg(wordContentFileName, needCreateJpg=False, jpgName=""):
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, 'wordfile/' + wordContentFileName), encoding="utf-8").read()
    # print(text)

    # 设置字体，使其支持中文显示，需要提前下载对应的字体
    font = r"D:\project_python\simfang.ttf"
    # Generate a word cloud image
    wordcloud = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2).generate(text)
    if needCreateJpg:
        # 把产生的词云保存进图片
        if not jpgName:
            jpgName = "default_" + DateUtil.nowNoSplit()
        if not jpgName.endswith(".jpg"):
            jpgName = jpgName + ".jpg"
        print("生成图片名："+jpgName)
        wordcloud.to_file("wordfile/" + jpgName)

    # Display the generated image:
    # the matplotlib way:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    wordContentFileName = "weibocontent.txt"
    # 生成图片
    createJpg(wordContentFileName, True, "佟丽娅")
