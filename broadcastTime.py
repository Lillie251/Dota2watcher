# -*- coding: utf-8 -*-

from datetime import datetime
import math
import time


# 配信開始時間から配信経過時間を計算するメソッド
def getBroadcastTime(createTime):
    try:
        timeNow = str(datetime.utcnow())

        # Stringを時刻に変換する
        time_t1 = time.strptime(createTime, '%Y-%m-%dT%H:%M:%SZ')
        time_t2 = time.strptime(timeNow, '%Y-%m-%d %H:%M:%S.%f')

        # エポック秒に変換する
        epo_time_t1 = time.mktime(time_t1)
        epo_time_t2 = time.mktime(time_t2)

        # 現在の時間から配信を開始した時間の差分を出す
        streamTime = (epo_time_t2 - epo_time_t1)

        # 秒なので60で割ることで分に変換。小数点を切り捨てる
        streamMinute = math.floor(streamTime / 60)
    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") +
              "[ERROR] broadcastTime.py getBroadcastTime()")
    finally:
        return streamMinute


# 現在の時間を取得するメソッド
def getTimeNow():
    timeNow = datetime.now().strftime("[%Y/%m/%d %H:%M:%S]")
    return timeNow
