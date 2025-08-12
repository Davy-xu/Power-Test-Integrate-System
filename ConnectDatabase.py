import mysql.connector
from mysql.connector import Error

# 默认版本信息，如果无法从main_new获取时使用
DEFAULT_VERSION = "V1.0"

def get_version_from_main():
    """动态获取版本信息，避免循环导入"""
    try:
        import main_new
        return main_new.VERSION
    except ImportError:
        return DEFAULT_VERSION



# 【类】 数据库连接函数
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
        """查询电源测试设备集成控制系统的启用状态"""
        conn = self.mysql_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            # 获取版本信息并构建查询参数
            version = get_version_from_main()
            version_name = f'电源测试设备集成控制系统 {version}'
            query = """
            SELECT `是否启用` 
            FROM tb_cvte_test_system_version_enable 
            WHERE `版本` = %s
            """
            cursor.execute(query, (version_name,))
            result = cursor.fetchone()
            
            if result:
                return result[0]
            else:
                # 如果找不到精确匹配，返回None（禁用）
                return None
                
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def check_instrument_command_exists(self, device_type, device_model, function_type):
        """检查仪器指令是否已存在，如果存在则返回详细信息"""
        conn = self.mysql_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            query = """
            SELECT 指令, 指令参数提醒, 更新时间
            FROM tb_instrument_command 
            WHERE 仪器分类 = %s AND 仪器型号 = %s AND 功能分类 = %s
            """
            cursor.execute(query, (device_type, device_model, function_type))
            result = cursor.fetchone()
            
            if result:
                return {
                    'command': result[0],
                    'params_reminder': result[1],
                    'update_time': result[2]
                }
            else:
                return None
            
        except mysql.connector.Error as e:
            print(f"Error checking instrument command existence: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def get_all_instrument_commands(self):
        """获取所有仪器指令数据"""
        conn = self.mysql_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            query = """
            SELECT 仪器分类, 仪器型号, 功能分类, 指令, 指令参数提醒, 更新时间
            FROM tb_instrument_command 
            ORDER BY 更新时间 DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()
            
            # 转换为字典列表
            commands = []
            for row in results:
                commands.append({
                    'device_type': row[0],
                    'device_model': row[1], 
                    'function_type': row[2],
                    'command': row[3],
                    'params_reminder': row[4],
                    'update_time': row[5].strftime("%Y-%m-%d %H:%M:%S") if row[5] else ""
                })
            
            return commands
            
        except mysql.connector.Error as e:
            print(f"Error getting instrument commands: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def insert_instrument_command(self, device_type, device_model, function_type, command, params_reminder, update_time):
        """插入仪器指令到数据库"""
        conn = self.mysql_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            query = """
            INSERT INTO tb_instrument_command 
            (仪器分类, 仪器型号, 功能分类, 指令, 指令参数提醒, 更新时间) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (device_type, device_model, function_type, command, params_reminder, update_time))
            conn.commit()
            return True
            
        except mysql.connector.Error as e:
            print(f"Error inserting instrument command: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def check_test_program_exists(self, program_name):
        """检查测试项目名称是否已存在"""
        conn = self.mysql_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            query = """
            SELECT COUNT(*) FROM tb_power_equipment_integrated_control_system 
            WHERE 测试项目名称 = %s
            """
            cursor.execute(query, (program_name,))
            result = cursor.fetchone()
            return result[0] > 0 if result else False
            
        except mysql.connector.Error as e:
            print(f"Error checking test program existence: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def insert_test_program(self, program_name, step_number=0):
        """插入测试项目到数据库"""
        conn = self.mysql_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            query = """
            INSERT INTO tb_power_equipment_integrated_control_system 
            (测试项目名称, 测试步骤序号) 
            VALUES (%s, %s)
            """
            cursor.execute(query, (program_name, step_number))
            conn.commit()
            return True
            
        except mysql.connector.Error as e:
            print(f"Error inserting test program: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_all_test_programs(self):
        """获取所有测试项目名称"""
        conn = self.mysql_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            query = """
            SELECT DISTINCT 测试项目名称 FROM tb_power_equipment_integrated_control_system 
            WHERE 测试项目名称 IS NOT NULL AND 测试项目名称 != ''
            ORDER BY 测试项目名称
            """
            cursor.execute(query)
            results = cursor.fetchall()
            
            # 转换为字典列表
            programs = []
            for row in results:
                programs.append({
                    'name': row[0]
                })
            
            return programs
            
        except mysql.connector.Error as e:
            print(f"Error getting test programs: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()





