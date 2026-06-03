import mysql.connector

def get_database_connection():
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='priya@1206',
        database='student_tasks_manager'
    )
    return connection