import pymysql


class connect_sql():
    def __init__(self):
        self.sql_connect = pymysql.connect(
            host= '39.101.216.196',
            port= 3306,
            user= 'root',
            password= 'Saint123654@',
            db= 'stroke-data-reporting',
            charset= 'utf8'
        )
        self.cursor = self.sql_connect.cursor()

    #查询数据
    def signle_form(self,form_name,field_name,value):
        sql = "select count(1) from %s where %s = '%s' "%(form_name,field_name,value)
        reseult_sql = self.cursor.execute(sql)
        return reseult_sql

    def close(self):
        self.cursor.close()
        self.sql_connect.close()

cc = connect_sql()
a = cc.signle_form(form_name='t_role',field_name ='name',value ='测试')
print(a)