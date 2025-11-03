# Neostat

Web サイトのアクセスカウンターです。

## 特徴

管理画面にログインしたことのあるブラウザからのアクセスは無視するので、
純粋なユーザーからのアクセス数だけをカウントすることができます。

## 開発環境

```
# インストール
$ git clone https://github.com/ninko-txz/neostat.git
$ cd neostat
$ pip install -r requirements.txt

# サーバー起動
$ export NEOSTAT_USERNAME=neostat
$ export NEOSTAT_PASSWORD=neostat
$ export NEOSTAT_TOKEN=neostat
$ export NEOSTAT_CORS=https://ninko.neocities.org
$ flask run --debug

# 管理画面を開く
http://localhost:5000/neostat
```

## デフォルト値

| Name             | Value    |
| ---------------- | -------- |
| NEOSTAT_USERNAME | admin    |
| NEOSTAT_PASSWORD | password |
| NEOSTAT_TOKEN    | neostat  |
| NEOSTAT_CORS     | \*       |

## 備考

-   認証済みブラウザによるアクセスカウントを回避するにはブラウザ側で 3rd パーティ製の Cookie が許可されている必要があります。
