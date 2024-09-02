import mysql.connector
from datetime import datetime
import os

DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USER = os.getenv('DATABASE_HOST')
DATABASE_PASSWORD = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_HOST')


# 데이터베이스 연결 설정
conn = mysql.connector.connect(
    host=DATABASE_HOST,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    database=DATABASE_NAME
)
cursor = conn.cursor()

# 현재 날짜 확인
now = datetime.now()
if now.day == 1:
    # 테이블 초기화 구문 입력
    cursor.execute("TRUNCATE TABLE your_table_name")
    conn.commit()

cursor.close()
conn.close()
