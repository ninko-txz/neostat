import os

MYSQL = {
    "user": os.getenv("NS_MYSQL_USERNAME", "root"),
    "password": os.getenv("NS_MYSQL_PASSWORD", "neostat"),
    "host": os.getenv("NS_MYSQL_HOST", "127.0.0.1"),
    "database": os.getenv("NS_MYSQL_DB", "neostat"),
}

BASIC_USERNAME = os.getenv("NS_BASIC_USERNAME", "admin")
BASIC_PASSWORD = os.getenv("NS_BASIC_PASSWORD", "password")

COOKIE_NAME = os.getenv("NS_COOKIE_NAME", "neostat")
COOKIE_VALUE = os.getenv("NS_COOKIE_VALUE", "neostat")

IGNORE_USER_AGENTS = ["Screenjesus"]
