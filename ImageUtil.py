#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os


# 按照某个图片的形状生成词云
# sourceImagePath:原始图片路径
# keywords：需要生成使用的关键词，格式为dict
def generateImageRelySource(sourceImagePath, keywords, cutJpgName="关键词.jpg"):
    dpath = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # 初始化图片
    image = Image.open(sourceImagePath)
    graph = np.array(image)

    # 设置字体，使其支持中文显示，需要提前下载对应的字体
    font = dpath + "\simfang.ttf"
    # 生成云图，这里需要注意的是WordCloud默认不支持中文，所以这里需要加载中文黑体字库
    wc = WordCloud(font_path=font,
                   background_color='white', max_words=1000, mask=graph)
    wc.generate_from_frequencies(keywords)
    # 写入文件
    wc.to_file(cutJpgName)
    # 按照背景图进行图片的生成
    image_color = ImageColorGenerator(graph)
    # 进行图片展示
    plt.imshow(wc)
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")  # 关闭图像坐标系
    plt.show()
