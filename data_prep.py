import sqlite3
from sqlite3 import Error

timestamps_subject = []

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_task_by_priority(conn):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("select * from audio_timestamp at2 where user_id = 1",)

    rows = cur.fetchall()

    for row in rows:
        timestamps_subject.append([row[2], row[3]])
        


def main():
    database = r".\database.sqlite"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn)



main()