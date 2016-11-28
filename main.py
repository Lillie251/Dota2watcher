# -*- coding: utf-8 -*-

# 標準モジュール
from datetime import datetime
import math
import time

# 自作モジュール
import broadcastTime as castTime

import tweet

import twitch

USER_LIST = ["lillie251",
             "baseballdogs",
             "marusuman",
             "enocinoco",
             "deshooooo",
             "imotsumuri",
             "ridingkun",
             "holt009",
             "null_p_e",
             "itukorobu",
             "hitujiha",
             "dotamara2",
             "awai_o",
             "kaerukun4365",
             "silverjumper123",
             "ume_dota",
             "heromuu",
             "zappa3594",
             "17uu"]

USER_DICT = {"lillie251": 0,
             "baseballdogs": 0,
             "marusuman": 0,
             "enocinoco": 0,
             "deshooooo": 0,
             "imotsumuri": 0,
             "ridingkun": 0,
             "holt009": 0,
             "null_p_e": 0,
             "itukorobu": 0,
             "hitujiha": 0,
             "dotamara2": 0,
             "awai_o": 0,
             "kaerukun4365": 0,
             "silverjumper123": 0,
             "ume_dota": 0,
             "heromuu": 0,
             "zappa3594": 0,
             "17uu": 0}

print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + "Program start")
print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + "Setting start")

# 各userのUSER_DICTの数値を初期化
for var in range(0, len(USER_LIST)):
    try:
        if twitch.getInfo(USER_LIST[var]) != None:

            infoStream = twitch.getInfo(USER_LIST[var])  # 配信の情報を取得する
            streamStartTime = twitch.getCreateTime(infoStream)  # 配信開始時間を取得する
            streamNow = castTime.getBroadcastTime(streamStartTime)  # 配信経過時間を取得する
            USER_DICT[USER_LIST[var]] = math.floor(streamNow / 45)  # 配信経過時間を45で割った数値を代入する.(小数点切り捨て)
            print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + USER_LIST[var] + "=" + str(USER_DICT[USER_LIST[var]]))

    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] main.py")
    finally:
        time.sleep(5)

print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + "Setting end")

# 以下ループ
while True:
    for var in range(0, len(USER_LIST)):
        try:
            if twitch.getInfo(USER_LIST[var]) != None:

                infoStream = twitch.getInfo(USER_LIST[var])  # 配信の情報を取得する
                streamGameTitle = twitch.getGameTitle(infoStream)  # 配信中にゲームタイトルを取得する

                if streamGameTitle == "Dota 2":

                    streamStartTime = twitch.getCreateTime(infoStream)  # 配信開始時間を取得する
                    streamNow = castTime.getBroadcastTime(streamStartTime)  # 配信経過時間を取得する
                    infoStreamChannel = twitch.getChannelInfo(infoStream)  # 配信チャンネルの情報を取得する
                    casterName = twitch.getUsername(infoStreamChannel)  # 配信者のTwitchアカウントの名前を取得する
                    streamTitle = twitch.getTitle(infoStreamChannel)  # 配信タイトルを取得する
                    streamUrl = twitch.getUrl(infoStreamChannel)  # 配信のURLを取得する

                    if USER_DICT[USER_LIST[var]] == 12:
                        if streamNow < 585:
                            if streamNow >= 540:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 13
                        else:
                            USER_DICT[USER_LIST[var]] = 13

                    if USER_DICT[USER_LIST[var]] == 11:
                        if streamNow < 540:
                            if streamNow >= 495:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 12
                        else:
                            USER_DICT[USER_LIST[var]] = 12

                    if USER_DICT[USER_LIST[var]] == 10:
                        if streamNow < 495:
                            if streamNow >= 450:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 11
                        else:
                            USER_DICT[USER_LIST[var]] = 11

                    if USER_DICT[USER_LIST[var]] == 9:
                        if streamNow < 450:
                            if streamNow >= 405:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 10
                        else:
                            USER_DICT[USER_LIST[var]] = 10

                    if USER_DICT[USER_LIST[var]] == 8:
                        if streamNow < 405:
                            if streamNow >= 360:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 9
                        else:
                            USER_DICT[USER_LIST[var]] = 9

                    if USER_DICT[USER_LIST[var]] == 7:
                        if streamNow < 360:
                            if streamNow >= 315:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 8
                        else:
                            USER_DICT[USER_LIST[var]] = 8

                    if USER_DICT[USER_LIST[var]] == 6:
                        if streamNow < 315:
                            if streamNow >= 270:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 7
                        else:
                            USER_DICT[USER_LIST[var]] = 7

                    if USER_DICT[USER_LIST[var]] == 5:
                        if streamNow < 270:
                            if streamNow >= 225:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 6
                        else:
                            USER_DICT[USER_LIST[var]] = 6

                    if USER_DICT[USER_LIST[var]] == 4:
                        if streamNow < 225:
                            if streamNow >= 180:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 5
                        else:
                            USER_DICT[USER_LIST[var]] = 5

                    if USER_DICT[USER_LIST[var]] == 3:
                        if streamNow < 180:
                            if streamNow >= 135:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 4
                        else:
                            USER_DICT[USER_LIST[var]] = 4

                    if USER_DICT[USER_LIST[var]] == 2:
                        if streamNow < 135:
                            if streamNow >= 90:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 3
                        else:
                            USER_DICT[USER_LIST[var]] = 3

                    if USER_DICT[USER_LIST[var]] == 1:
                        if streamNow < 90:
                            if streamNow >= 45:
                                tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                                USER_DICT[USER_LIST[var]] = 2
                        else:
                            USER_DICT[USER_LIST[var]] = 2

                    if USER_DICT[USER_LIST[var]] == 0:
                        tweet.doTweet(casterName, streamTitle, streamUrl)
                        USER_DICT[USER_LIST[var]] = 1

                    print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "Caster: " + USER_LIST[var] + " Time: " + str(streamNow) + " minite")
                else:
                    print(USER_LIST[var] + " stream " + streamGameTitle)

            else:
                print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + str(USER_LIST[var]) + " dont stream")
                USER_DICT[USER_LIST[var]] = 0
        except Exception:
            print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] main.py")
            USER_DICT[USER_LIST[var]] = USER_DICT[USER_LIST[var]] + 1
        finally:
            time.sleep(5)
