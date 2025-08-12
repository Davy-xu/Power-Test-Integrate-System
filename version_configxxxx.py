"""
版本配置文件
独立的版本信息，避免循环导入
"""

# 版本信息配置
VERSION = "V1.0"
BUILD_DATE = "20250805_112233"
VERSION_STRING = f"{VERSION} {BUILD_DATE}"

def get_version_info():
    """获取版本信息"""
    return VERSION_STRING

def get_version():
    """获取版本号"""
    return VERSION

def get_build_date():
    """获取构建日期"""
    return BUILD_DATE
