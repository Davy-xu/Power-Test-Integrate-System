"""
测试更新后的数据库查询方法
"""
import mysql.connector
from mysql.connector import Error

class ReadDataBase:
    def mysql_connection(self):
        try:
            conn = mysql.connector.connect(
                host="p-dbsec-mysql.gz.cvte.cn",
                port="10008",
                user="tv_td_platform",
                password="Abs#Yh2NusCK",
                database="tv_td_platform"
            )
            return conn
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")
            return None
    
    def get_system_enable_status(self):
        """查询电源测试设备集成控制系统 V1.0的启用状态"""
        conn = self.mysql_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            # 先尝试精确匹配
            query1 = """
            SELECT `是否启用` 
            FROM tb_cvte_test_system_version_enable 
            WHERE `版本` = '电源测试设备集成控制系统 V1.0'
            """
            cursor.execute(query1)
            result = cursor.fetchone()
            
            if result:
                return result[0]
            
            # 如果没有精确匹配，查找包含"电源"的最新版本
            query2 = """
            SELECT `是否启用` 
            FROM tb_cvte_test_system_version_enable 
            WHERE `版本` LIKE '%电源%' 
            ORDER BY `版本` DESC 
            LIMIT 1
            """
            cursor.execute(query2)
            result = cursor.fetchone()
            
            if result:
                return result[0]
            else:
                return None
                
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def test_final():
    """最终测试"""
    db = ReadDataBase()
    
    print("正在查询电源系统的启用状态...")
    
    enable_status = db.get_system_enable_status()
    
    if enable_status is not None:
        print(f"查询结果: {enable_status}")
        print(f"数据类型: {type(enable_status)}")
        
        # 输出一个值
        print(f"\n最终结果: {enable_status}")
    else:
        print("查询失败或未找到数据")

if __name__ == "__main__":
    test_final()
