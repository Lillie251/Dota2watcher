# Dota2watcher
Dota2配信を自動でツイートしてくれる便利なやつ。

# 使ったもの
Python 3.5.2  
OAuthのライブラリは<https://github.com/requests/requests-oauthlib>  
`$ pip install requests requests_oauthlib`でインストールできる

# 問題点と解決策
ツイート140文字超えると多分死ぬ
→配信タイトルを一定の長さで切る

配信者がDota2以外のゲームやってもツイートされる
→配信ゲームでフィルターかけてDota2配信しかツイートしないようにする
