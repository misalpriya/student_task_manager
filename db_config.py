import mysql.connector

def get_database_connection():
    connection=mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='36dmhzzv3UFMCEB.root',
        password='SOVJ1HS8AmsAG9H5',
        database='student_task_manager'
    )
    return connection

# # def get_database_connection():
#     connection=mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='priya@1206',
#         database='student_tasks_manager'
#     )
#     return connection