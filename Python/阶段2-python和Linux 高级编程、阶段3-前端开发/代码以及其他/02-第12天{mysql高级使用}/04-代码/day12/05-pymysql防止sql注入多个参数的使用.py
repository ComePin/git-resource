# 1. 导包
import pymysql

if __name__ == '__main__':

    # 2. 创建连接对象
    # connect = Connection = Connect 本质上是一个函数，使用这三个里面的任何一个函数都可以创建一个连接对象
    # 1. host : 服务器的主机地址
    # 2. port: mysql数据库的端口号
    # 3. user： 用户名
    # 4. password：密码
    # 5. database: 操作的数据库
    # 6. charset: 操作数据库使用的编码格式
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="mysql",
                           database="python41",
                           charset="utf8")

    # 3. 获取游标， 目的就是要执行sql语句
    cursor = conn.cursor()
    # 准备sql, 使用防止sql注入的sql语句， %s是sql语句的参数和字符串里面的%s不一样，不要加上引号
    sql = "insert into students(name, age, gender, c_id) values(%s, %s, %s, %s)"
    print(sql)

    try:
        # 4. 执行sql语句
        # 1. sql
        # 2. 执行sql语句的传入的参数，参数类型可以是元组，列表，字典
        cursor.execute(sql,["司马懿", 76, '男', 3]);
        conn.commit()
    except Exception as e:
        conn.rollback()

    finally:
        # 5. 关闭游标
        cursor.close()
        # 6. 关闭连接
        conn.close()