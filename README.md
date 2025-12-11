# Neostat

Web サイトのアクセスカウンターです。

## 特徴

管理者のブラウザからのアクセスはカウントしません。
(管理者のブラウザ = 管理画面にログインしたことのあるブラウザ)

## 注意事項

管理者のブラウザで 3rd パーティ製の Cookie が許可されている必要があります。
許可されていない場合、管理者からのアクセスもカウントされます。

## 開発環境

MySQL

```
CREATE DATABASE neostat;

USE neostat;

CREATE TABLE access_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at INT NOT NULL,
    path VARCHAR(128) NOT NULL,
    x_forwarded VARCHAR(64),
    user_agent VARCHAR(255),
    languages VARCHAR(128),
    referrer VARCHAR(128),
    INDEX (created_at)
)
```

Flask

```
$ git clone https://github.com/ninko-txz/neostat.git
$ cd neostat
$ pip install -r requirements.txt
$ flask run --debug
```

## 任意の UserAgent からのアクセスを無視したい場合

settings.py の IGNORE_USER_AGENTS に UserAgent 名を追記してください。
(デフォルトでは Screenjesus のみが無視されます)

## 環境変数一覧

| Name              | DefaultValue |
| ----------------- | ------------ |
| NS_MYSQL_USERNAME | root         |
| NS_MYSQL_PASSWORD | neostat      |
| NS_MYSQL_HOST     | 127.0.0.1    |
| NS_MYSQL_DB       | neostat      |
| NS_BASIC_USERNAME | admin        |
| NS_BASIC_PASSWORD | password     |
| NS_COOKIE_NAME    | neostat      |
| NS_COOKIE_VALUE   | neostat      |
