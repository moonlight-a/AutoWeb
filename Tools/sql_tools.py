import pymysql


class connect_sql():
    def __init__(self):
        self.sql_connect = pymysql.connect(
            host= '39.101.216.196',
            port= 3306,
            user= 'root',
            password= 'Saint123654@',
            database= 'stroke-data-reporting',
            charset= 'utf8'
        )
        self.cursor = self.sql_connect.cursor()

    #根据条件查询数据
    def signle_form(self,form_name,field_name,value):
        sql = "select * from %s where %s like  '%%%s%%'"%(form_name,field_name,value)

        reseult_sql = self.cursor.execute(sql)
        return reseult_sql

    #查询单个表当前的总数据
    def single_form_data(self,form_name):
        sql = "select * from %s "%(form_name)

        result_sql = self.cursor.execute(sql)

        return result_sql

    #根据左连接查询数据
    def left_join(self,tableA,tableB,value):
        sql = "select %s from %s where left join %s on %s.%s =  %s.%s"%(value,tableA,tableB,tableA,value,tableB,value)

        result_sql = self.cursor.execute(sql)

        return result_sql

    #对表格插入数据
    def insert_value(self,table,*args):
        
        sql = "insert into %s VALUES()"
    #关闭数据库连接
    def close(self):
        self.cursor.close()
        self.sql_connect.close()

cc = connect_sql()

# a = cc.single_form_data(form_name='t_role',field_name ='name',value ='测')
a = cc.left_join(tableA= 'A',tableB='B',value='C')
cc.close()

print(a)