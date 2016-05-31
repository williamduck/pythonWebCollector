import pymysql
conn = pymysql.connect(host = '10.9.201.151', unix_socket = '/tmp/mysql.sock',
                       user = 'root', passwd = 'root', db = 'mysql')
cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id = 1")
print(cur.fetchone())
cur.close()
conn.close()
