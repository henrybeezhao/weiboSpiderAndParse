#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import weibo
import wordCloud
import CsvUtil
import JiebaUtil
import ImageUtil
import FileUtil
import os


def main():
    # 微博用户的uid
    uid = 5534772673

    # 爬取微博，并且获取微博内容
    # weibo.main(uid)
    # 读取csv文件
    lineList = CsvUtil.readCsv(uid)
    # 写入txt
    CsvUtil.writeTxtFile(uid, lineList)
    # 生成分析图片
    wordCloud.createJpg(uid)
    # 分词后生成词图，读取文件内容，生成str
    wordContent = "\n".join(lineList)
    # 进行关键词提取
    keyWords = JiebaUtil.getKeyWord(wordContent)
    # 生成词图
    sourceImagePath = "./imageTem/qiaoba2.jpg"
    # 获取文件全名
    txtFilePath = FileUtil.getTxtFilePath(uid)
    file_pref = txtFilePath[0:txtFilePath.rfind((os.sep))]
    # 生成图
    ImageUtil.generateImageRelySource(sourceImagePath, keyWords, file_pref + "关键词.jpg")


if __name__ == "__main__":
    main()
