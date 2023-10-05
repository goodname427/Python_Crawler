import pymysql

conn = pymysql.connect(host='43.138.203.16', user='root',password='asd1335438725', database='py',port=3306)
cursor = conn.cursor()
# sql语句执性，列表元组
info_list = [('我不是药神','徐峥','2018-07-05'),('你好,李焕英','贾玲','2021-02-12')]
sql = 'insert into movieinfo values(%s,%s,%s)'
cursor.executemany(sql,info_list)
conn.commit()
# 关闭
cursor.close()
conn.close()
