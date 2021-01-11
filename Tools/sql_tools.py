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
    def signle_form_sql(self,form_name,field_name,value):
        sql = "select * from %s where %s like  '%%%s%%'"%(form_name,field_name,value)

        reseult_sql = self.cursor.execute(sql)
        return reseult_sql

    #查询单个表当前的总数据
    def single_form_data_sql(self,form_name):
        sql = "select * from %s "%(form_name)

        result_sql = self.cursor.execute(sql)

        return result_sql

    #根据左连接查询数据
    def left_join_sql(self,tableA,tableB,condition):
        sql = "select %s from %s left join %s on %s.%s =  %s.%s"%(condition,tableA,tableB,tableA,condition,tableB,condition)

        result_sql = self.cursor.execute(sql)

        return result_sql
    #多条件查询
    def many_condition_sql(self,table,*args):

        sql = "select * from {0} where {1} = '{2}' and {3} = {4}".format(table,args[0],args[1],args[2],args[3])

        result_sql = self.cursor.execute(sql)
        return result_sql
    #对表格插入数据
    def insert_value_sql(self,table,*args):
        
        sql = "insert into %s VALUES('%s')"%(table,args)
        result_sql = self.cursor.execute(sql)
        return result_sql

    #修改表格内的数据
    def updata_sql(self):
        sql = "update %s set = %s  where %s"

    #关闭数据库连接
    def close(self):
        self.cursor.close()
        self.sql_connect.close()
if __name__ == '__main__':

    cc = connect_sql()

    # a = cc.single_form_data(form_name='t_role',field_name ='name',value ='测')
    a = cc.left_join_sql( 't_role','t_role_resource','id')
    cc.close()

    print(a)