import sqlite3


def get_connection():
    return sqlite3.connect("neostat.db")


def read_sql(path):
    with open(path, "r", encoding="utf-8") as sql_file:
        return sql_file.read()


def execute_sql(sql, fetch=False):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall() if fetch else conn.commit()

    finally:
        cur.close()
        conn.close()


def create_table():
    sql = read_sql("./sql/create-table.sql")
    execute_sql(sql)


def count_up(log):
    sql = read_sql("./sql/count-up.sql")
    execute_sql(sql.format(**log))


def count_view():
    sql = read_sql("./sql/count-view.sql")
    values = execute_sql(sql, fetch=True)
    keys = ["id", "created_at", "page_name", "x_forwarded", "country", "user_agent", "languages", "referrer"]
    return [dict(zip(keys, row)) for row in values]
