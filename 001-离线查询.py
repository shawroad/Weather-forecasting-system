import sqlite3
import time



if __name__ == '__main__':

    city = input("请输入你要查询的城市:")

    # 指定数据库名
    timedb = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 链接数据库   也就是指定数据库的名字  后面是一个目录
    conn = sqlite3.connect(r'.\{}.db'.format(timedb))

    c = conn.cursor()

    c.execute('''select * from one_air''')
    for air in c.fetchall():
        if city in air:
            print(air)

    conn.commit()  # 提交事务
    conn.close()


