# Neostat

Webサイトのアクセスカウンターです。

## 開発環境

```
# インストール
$ git clone https://github.com/ninko-txz/neostat.git
$ cd neostat
$ pip install -r requirements.txt

# サーバー起動
$ export NEOCITIES_ORIGIN=https://ninko.neocities.org
$ flask run --debug
```

## 備考

-   NEOCITIES_ORIGIN が設定されていない場合、全てのオリジンを許可します
