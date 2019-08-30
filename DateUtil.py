#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime


# 返回当前日期
def nowNoSplit():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


if __name__ == "__main__":
    print(nowNoSplit())
