#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 设置微博爬取的参数
filter = 1  # 值为0表示爬取全部微博（原创微博+转发微博），值为1表示只爬取原创微博
since_date = '2019-01-01'  # 起始时间，即爬取发布日期从该值到现在的微博，形式为yyyy-mm-dd
pic_download = 1  # 值为0代表不下载微博原始图片,1代表下载微博原始图片
video_download = 1  # 值为0代表不下载微博视频,1代表下载微博视频
