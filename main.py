#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import weibo
import wordCloud
import CsvUtil


def main():
    # 微博用户的uid
    uid = 1227368500
    # 爬取微博，并且获取微博内容
    weibo.main(uid)
    #读取csv文件
    lineList = CsvUtil.readCsv(uid)
    # 写入txt
    CsvUtil.writeTxtFile(uid, lineList)
    # 生成分析图片
    wordCloud.createJpg(uid)

if __name__=="__main__":
    main()
