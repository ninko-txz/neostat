# Neostat

Web サイトのアクセスカウンターです。

## 特徴

管理画面にログインしたことのあるブラウザからのアクセスはカウントされません。

## 注意事項

管理者のブラウザで 3rd パーティ製の Cookie が許可されている必要があります。
許可されていない場合や Cookie が手動削除された場合、管理者からのアクセスもカウントされます。

## 開発環境

```
# インストール
$ git clone https://github.com/ninko-txz/neostat.git
$ cd neostat && pip install -r requirements.txt

# サーバー起動
$ export NEOSTAT_ORIGIN=https://ninko.neocities.org
$ flask run --debug

# 管理画面を開く
http://localhost:5000/neostat
```

## 環境変数

| Name                | Required | Default  | Description                            |
| ------------------- | -------- | -------- | -------------------------------------- |
| NEOSTAT_ORIGIN      | True     | -        | カウント対象の Web サイトのオリジン    |
| NEOSTAT_USERNAME    | False    | admin    | 管理画面にログインするためのユーザー名 |
| NEOSTAT_PASSWORD    | False    | password | 管理画面にログインするためのパスワード |
| NEOSTAT_TOKEN       | False    | neostat  | 管理者の Cookie に保存されるトークン   |
| NEOSTAT_GEOLOCATION | False    | False    | IP アドレスから国籍を判別するか        |

## 国籍判別機能の有効化

[GeoLite](https://www.maxmind.com/) のデータを利用して、IP アドレスから国を判別できます。

```
# GeoLiteのサイトからDBをダウンロード
https://www.maxmind.com/

# DBを geolite.mmdb という名前でプロジェクトルートに保存

# サーバー起動
$ export NEOSTAT_ORIGIN=https://ninko.neocities.org/
$ export NEOSTAT_GEOLOCATION=True
$ flask run --debug
```

## 特定の UA をカウント対象から除外

ignore_ua.txt に UA の名前を追記してください。
