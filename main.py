# -*- coding: utf-8 -*-

# 標準モジュール
from datetime import datetime
import math
import time

# 自作モジュール
import broadcastTime as castTime

import tweet

import twitch

userlist = ["lillie251",
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
            "ume_dota"]

userdict = {"lillie251": 0,
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
            "ume_dota": 0}

NUM1 = 1

print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + "Program start")
print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + "Setting start")

# 各userのuserdictの数値を初期化
for var in range(0, len(userlist)):
    try:
        if twitch.getInfo(userlist[var]) != None:

            infoStream = twitch.getInfo(userlist[var])  # 配信の情報を取得する
            streamStartTime = twitch.getCreateTime(infoStream)  # 配信開始時間を取得する
            streamNow = castTime.getBroadcastTime(streamStartTime)  # 配信経過時間を取得する
            userdict[userlist[var]] = math.floor(streamNow/45)  # 配信経過時間を45で割った数値を代入する.(小数点切り捨て)
            print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + userlist[var] + "=" + str(userdict[userlist[var]]))

    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] main.py")
    finally:
        time.sleep(5)

print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + "Setting end")

# 以下ループ
while NUM1 == 1:
    for var in range(0, len(userlist)):
        try:
            if twitch.getInfo(userlist[var]) != None:

                infoStream = twitch.getInfo(userlist[var])  # 配信の情報を取得する
                streamStartTime = twitch.getCreateTime(infoStream)  # 配信開始時間を取得する
                streamNow = castTime.getBroadcastTime(streamStartTime)  # 配信経過時間を取得する
                infoStreamChannel = twitch.getChannelInfo(infoStream)  # 配信チャンネルの情報を取得する
                casterName = twitch.getUsername(infoStreamChannel)  # 配信者のTwitchアカウントの名前を取得する
                streamTitle = twitch.getTitle(infoStreamChannel)  # 配信タイトルを取得する
                streamUrl = twitch.getUrl(infoStreamChannel)  # 配信のURLを取得する

                if userdict[userlist[var]] == 12:
                    if streamNow >= 540:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 13

                if userdict[userlist[var]] == 11:
                    if streamNow >= 495:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 12

                if userdict[userlist[var]] == 10:
                    if streamNow >= 450:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 11

                if userdict[userlist[var]] == 9:
                    if streamNow >= 405:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 10

                if userdict[userlist[var]] == 8:
                    if streamNow >= 360:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 9

                if userdict[userlist[var]] == 7:
                    if streamNow >= 315:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 8

                if userdict[userlist[var]] == 6:
                    if streamNow >= 270:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 7

                if userdict[userlist[var]] == 5:
                    if streamNow >= 225:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 6

                if userdict[userlist[var]] == 4:
                    if streamNow >= 180:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 5

                if userdict[userlist[var]] == 3:
                    if streamNow >= 135:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 4

                if userdict[userlist[var]] == 2:
                    if streamNow >= 90:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 3

                if userdict[userlist[var]] == 1:
                    if streamNow >= 45:
                        tweet.doTweetTime(casterName, streamTitle, streamUrl, streamNow)
                        userdict[userlist[var]] = 2

                if userdict[userlist[var]] == 0:
                    tweet.doTweet(casterName, streamTitle, streamUrl)
                    userdict[userlist[var]] = 1

                print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "Caster: " + userlist[var] + " Time: " + str(streamNow) + " minite")

            else:
                print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[INFO] " + str(userlist[var]) + " dont stream")
                userdict[userlist[var]] = 0
        except Exception:
            print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] main.py")
            userdict[userlist[var]] = userdict[userlist[var]] + 1
        finally:
            time.sleep(5)
