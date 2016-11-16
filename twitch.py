# -*- coding: utf-8 -*-

from datetime import datetime

import requests

twitch_api = 'https://api.twitch.tv/kraken/streams/'
client_id = '?client_id='  #Twitchのclient_id
username = ""


def getInfo(name):
    try:
        username = name
        r = requests.get(twitch_api + username + client_id)
        info = r.json()
        infoStream = info.get("stream")
    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] twitch.py getInfo()")
    finally:
        return infoStream


def getChannelInfo(infoStream):
    try:
        infostr = infoStream
        infoStreamChannel = infostr.get("channel")
    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] twitch.py getChannelInfo()")
    finally:
        return infoStreamChannel


# 配信者名を取得するメソッド
def getUsername(infoStreamChannel):
    try:
        infostr = infoStreamChannel
        userName = infostr.get("display_name")
    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] twitch.py getUsername()")
    finally:
        return userName


# 配信開始時間を表示するメソッド
def getCreateTime(infoStream):
    try:
        infostr = infoStream
        streamStartTime = infostr.get("created_at")
    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] twitch.py getCreateTime()")
    finally:
        return streamStartTime


# 配信タイトルを取得するメソッド
def getTitle(infoStreamChannel):
    try:
        infostr = infoStreamChannel
        streamTitle = infostr.get("status")
    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] twitch.py getTitle()")
    finally:
        return streamTitle


# 配信のURLを取得するメソッド
def getUrl(infoStreamChannel):    
    try:
        infostr = infoStreamChannel
        streamUrl = infostr.get("url")
    except Exception:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[ERROR] twitch.py getUrl()")
    finally:
        return streamUrl
