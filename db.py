import mysql.connector

import settings


def get_access_log():
    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**settings.MYSQL)
        cursor = conn.cursor(dictionary=True)

        sql = """
            SELECT id, created_at, path, x_forwarded, user_agent, languages, referrer
            FROM access_logs 
            ORDER BY created_at DESC
        """
        cursor.execute(sql)

        return cursor.fetchall()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def save_access_log(*values):
    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(**settings.MYSQL)
        cursor = conn.cursor()

        sql = """
            INSERT INTO access_logs 
            (created_at, path, x_forwarded, user_agent, languages, referrer)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, values)
        conn.commit()

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()
