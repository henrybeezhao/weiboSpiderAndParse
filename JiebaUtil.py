#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import jieba
import jieba.analyse
import re
import ImageUtil
import CsvUtil


# 读取文本进行分词
def cut(filePath):
    with open(filePath, encoding="utf-8") as fileHandle:
        # 定义需要过滤的标点符号等
        r = '[，。|！|’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
        for line in fileHandle.readlines():
            # 进行过滤
            line = re.sub(r, '', line)
            # 进行分词
            cutList = jieba.cut(line)
            print("|".join(cutList))


# 读取文本进行分词
def cutList(contentList):
    # 定义需要过滤的标点符号等
    r = '[，。|！|’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    for line in contentList:
        # 进行过滤
        line = re.sub(r, '', line)
        # 进行分词
        cutList = jieba.cut(line)
        print("|".join(cutList))


# 关键词提取，返回一个dict，key：词语，value：比重值
def getKeyWord(content):
    # 这里使用jieba的textrank提取出1000个关键词及其比重
    result = jieba.analyse.textrank(content, topK=1000, withWeight=True)

    # 生成关键词比重字典
    keywords = dict()
    for i in result:
        keywords[i[0]] = i[1]
    print(keywords)
    return keywords


# 读取文件内容，组成字符串进行返回
def getContentFromFile(filePath):
    content = ""
    with open(filePath, encoding="utf-8") as fileHandle:
        for line in fileHandle.readlines():
            line = line.strip()
            content += line + "\n"
    print("from filePath:%s get content:%s" % (filePath, content))
    return content


if __name__ == "__main__":
    # 微博用户的uid
    uid = 5534772673
    # 读取csv文件
    lineList = CsvUtil.readCsv(uid)
    # 读取文件内容，生成str
    content = "\n".join(lineList)
    # 进行关键词提取
    keyWords = getKeyWord(content)
    # 生成词图
    sourceImagePath = "./imageTem/qiaoba2.jpg"
    ImageUtil.generateImageRelySource(sourceImagePath, keyWords)
