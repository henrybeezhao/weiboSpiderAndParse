#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

from weibo import Weibo


# 根据uid获取文件读取路径
def getFilePathByUid(uid):
    # 初始化weibo
    weibo = Weibo(uid)
    weibo.get_user_info()
    # 获取用户信息
    filePath = weibo.get_filepath("csv")
    return filePath


# 获取txt文件名
def getTxtFilePath(userId):
    # 根据uid获取对应的文件路径
    filePathe = getFilePathByUid(userId)
    file_pref = filePathe[0:filePathe.rfind((os.sep))]
    # 定义文件名
    writeFilePath = file_pref + os.sep + str(userId) + ".txt"
    return writeFilePath


if __name__ == "__main__":
    uid = 1345566427
    print(getFilePathByUid(uid))
