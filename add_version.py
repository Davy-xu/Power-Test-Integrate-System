"""
添加正确的版本记录到数据库
"""
import mysql.connector
from mysql.connector import Error

def add_correct_version():
    """向数据库添加正确的版本记录"""
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
        
        cursor = conn.cursor()
        
        # 插入正确的版本记录
        insert_query = """
        INSERT INTO tb_cvte_test_system_version_enable 
        (`版本`, `是否启用`, `是否为最新`, `备注`, `维护人信息`) 
        VALUES (%s, %s, %s, %s, %s)
        """
        
        values = (
            "电源测试设备集成控制系统 V1.0",
            "启用", 
            "是",
            "系统版本控制记录",
            "系统管理员"
        )
        
        cursor.execute(insert_query, values)
        conn.commit()
        
        print(f"成功添加版本记录: 电源测试设备集成控制系统 V1.0")
        print(f"影响行数: {cursor.rowcount}")
        
        # 验证添加是否成功
        cursor.execute("SELECT * FROM tb_cvte_test_system_version_enable WHERE `版本` = '电源测试设备集成控制系统 V1.0'")
        result = cursor.fetchone()
        
        if result:
            print("验证成功，记录已添加:")
            print(f"  版本: {result[0]}")
            print(f"  是否启用: {result[1]}")
        
    except mysql.connector.Error as e:
        print(f"数据库错误: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")

if __name__ == "__main__":
    add_correct_version()
