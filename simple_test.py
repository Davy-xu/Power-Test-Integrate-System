"""
简单的数据库查询测试
"""
import mysql.connector
from mysql.connector import Error

def test_query():
    """直接测试查询"""
    try:
        # 建立连接
        conn = mysql.connector.connect(
            host="p-dbsec-mysql.gz.cvte.cn",
            port="10008",
            user="tv_td_platform",
            password="Abs#Yh2NusCK",
            database="tv_td_platform"
        )
        
        print("数据库连接成功!")
        
        # 查询电源测试设备集成控制系统 V1.0的启用状态
        cursor = conn.cursor()
        query = """
        SELECT `是否启用` 
        FROM tb_cvte_test_system_version_enable 
        WHERE `版本` = '电源测试设备集成控制系统 V1.0'
        """
        
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            print(f"查询结果: {result[0]}")
            print(f"数据类型: {type(result[0])}")
        else:
            print("未找到匹配的数据")
            # 让我们看看有哪些版本包含"电源"
            cursor.execute("SELECT `版本`, `是否启用` FROM tb_cvte_test_system_version_enable WHERE `版本` LIKE '%电源%'")
            power_results = cursor.fetchall()
            print("包含'电源'的版本:")
            for row in power_results:
                print(f"  版本: {row[0]}, 是否启用: {row[1]}")
            
    except mysql.connector.Error as e:
        print(f"数据库错误: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")

if __name__ == "__main__":
    test_query()
