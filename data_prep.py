import sqlite3
from sqlite3 import Error

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

def select_task_by_priority(conn, subject_id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    timestamps_subject = []
    
    cur = conn.cursor()
    cur.execute("select * from audio_timestamp at2 where user_id = "+str(subject_id),)

    rows = cur.fetchall()

    for row in rows:
        timestamps_subject.append([row[2], row[3]])

    return timestamps_subject
        


def main(subject_id):
    database = r".\database.sqlite"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        return select_task_by_priority(conn, subject_id)

    return 0



