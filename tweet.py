# -*- coding: utf-8 -*-

from datetime import datetime

from requests_oauthlib import OAuth1Session

# 配信開始時にtweetするメソッド
def doTweet(name, title, sturl):
    CK = ""  # Consumer Key
    CS = ""  # Consumer Secret
    AT = ""  # Access Token
    AS = ""  # Accesss Token Secert

    # ツイート投稿用のUR
    url = "https://api.twitter.com/1.1/statuses/update.json"

    # ツイート本文
    params = {"status": datetime.now().strftime("【%Y/%m/%d %H:%M】\n") + name + "さんが配信をはじめました。\n" + title + "\n\n" + sturl}

    # OAuth認証で POST method で投稿
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(url, params=params)

    # レスポンスを確認
    if req.status_code == 200:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[SUCCESS] Tweet success")
    else:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[FAIL] Tweet fail Error: %d" % req.status_code)


# 配信経過時間をtweetするメソッド
def doTweetTime(name, title, sturl, time):
    CK = ""  # Consumer Key
    CS = ""  # Consumer Secret
    AT = ""  # Access Token
    AS = ""  # Accesss Token Secert

    # ツイート投稿用のUR
    url = "https://api.twitter.com/1.1/statuses/update.json"

    # ツイート本文
    params = {"status": datetime.now().strftime("【%Y/%m/%d %H:%M") + " 開始から" + str(time) + "分経過】\n" + name + "さんの配信\n" + title + "\n\n" + sturl}

    # OAuth認証で POST method で投稿
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(url, params=params)

    # レスポンスを確認
    if req.status_code == 200:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[SUCCESS] Tweet success")
    else:
        print(datetime.now().strftime("[%Y/%m/%d %H:%M:%S]") + "[FAIL] Tweet fail Error: %d" % req.status_code)
