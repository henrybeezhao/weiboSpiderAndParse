#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""excel操作工具类"""

import csv
import os

import FileUtil


# 读取文件
def readCsv(userId):
    resultList = []
    # 根据uid获取对应的文件路径
    filePathe = FileUtil.getFilePathByUid(userId)
    print(filePathe)
    print(filePathe[0:filePathe.rfind((os.sep))])
    with open(filePathe, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if reader.line_num == 1:
                continue
            resultList.append(row[1] + "\n")
    print("list size:%d" % len(resultList))
    return resultList


# 写入txt文件
def writeTxtFile(userId, lineList):
    writeFilePath = FileUtil.getTxtFilePath(userId)
    # 写入文件
    fileHandle = open(writeFilePath, "w", encoding="utf-8")
    fileHandle.writelines(lineList)


if __name__ == "__main__":
    userId = 1345566427
    # 读取正文
    lineList = readCsv(userId)
    # 写入txt
    writeTxtFile(userId, lineList)
