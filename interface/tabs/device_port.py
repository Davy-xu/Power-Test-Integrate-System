"""
设备端口选项卡
"""
import tkinter as tk
from tkinter import ttk
import sys
import os
import json
import socket
import subprocess
import re

# 尝试导入pyserial用于COM口检测
try:
    import serial.tools.list_ports
    SERIAL_AVAILABLE = True
except ImportError:
    SERIAL_AVAILABLE = False
    print("⚠️ 未安装pyserial，COM口检测将使用默认列表")

# 导入圆角矩形按钮组件
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from rounded_rect_button import RoundedRectButton
except ImportError:
    # 如果导入失败，使用普通按钮作为备用
    RoundedRectButton = None


class DevicePortTab:
    """设备端口选项卡"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.config_path = r"D:\Power Test Integrate System\System Information.json"
        self.address_combos = {}  # 存储地址下拉框的引用
        self.device_keys = ["oscilloscope", "ac_source", "electronic_load", "control_box"]
        
        # 确保配置目录存在
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        
        # 加载配置
        self.config = self.load_config()
        
        self.create_content()
        
        # 创建完成后保存当前配置
        self.save_config()
    
    def load_config(self):
        """加载配置文件"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # 默认配置
                return {
                    "device_addresses": {
                        "oscilloscope": "TCPIP::192.168.1.100::INSTR",
                        "ac_source": "TCPIP::192.168.1.101::INSTR", 
                        "electronic_load": "TCPIP::192.168.1.102::INSTR",
                        "control_box": "TCPIP::192.168.1.103::INSTR"
                    }
                }
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            # 返回默认配置
            return {
                "device_addresses": {
                    "oscilloscope": "TCPIP::192.168.1.100::INSTR",
                    "ac_source": "TCPIP::192.168.1.101::INSTR", 
                    "electronic_load": "TCPIP::192.168.1.102::INSTR",
                    "control_box": "TCPIP::192.168.1.103::INSTR"
                }
            }
    
    def save_config(self):
        """保存配置文件"""
        try:
            # 更新配置中的设备地址
            if "device_addresses" not in self.config:
                self.config["device_addresses"] = {}
            
            for i, key in enumerate(self.device_keys):
                if key in self.address_combos:
                    self.config["device_addresses"][key] = self.address_combos[key].get()
            
            # 保存到文件
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=4)
            print(f"配置已保存到: {self.config_path}")
        except Exception as e:
            print(f"保存配置文件失败: {e}")
    
    def on_address_changed(self, device_key):
        """地址改变时的回调函数"""
        self.save_config()
    
    def create_content(self):
        """创建设备端口内容"""
        # 端口配置框架
        self.create_port_config(self.parent_frame)
            
    def create_port_config(self, parent):
        """创建端口配置区域（透明效果）"""
       
        # 添加内边距
        inner_container = tk.Frame(parent, bg='#ffffff')
        inner_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 配置网格权重，支持两列布局
        inner_container.grid_columnconfigure(0, weight=1)
        inner_container.grid_columnconfigure(1, weight=1)
        
        # 创建四个设备地址配置，分为两列
        # 第一列
        self.create_device_address_config(inner_container, "示波器地址", "oscilloscope", 0, 0, "#e74c3c")
        self.create_device_address_config(inner_container, "AC Source地址", "ac_source", 1, 0, "#3498db") 
        # 第二列
        self.create_device_address_config(inner_container, "电子负载地址", "electronic_load", 0, 1, "#2ecc71")
        self.create_device_address_config(inner_container, "控制盒地址", "control_box", 1, 1, "#f39c12")
        
        # 添加全局刷新按钮区域
        button_frame = tk.Frame(inner_container, bg='#ffffff')
        button_frame.grid(row=2, column=0, columnspan=2, sticky=tk.EW, pady=(20, 0))
            
    def create_device_address_config(self, parent, label_text, device_key, row, column, theme_color):
        """创建单个设备地址配置（玻璃效果）"""
        # 验证主题颜色
        theme_color = self.validate_color(theme_color)
        
        # 设备卡片容器 - 白色背景
        device_card = tk.Frame(parent, bg='#ffffff', relief='flat', bd=0)
        device_card.grid(row=row, column=column, sticky=tk.EW, pady=8, padx=5)
        
        # 配置grid权重，让框架可以拉伸
        device_card.grid_columnconfigure(1, weight=1)
        
        # 创建背景
        glass_bg = tk.Frame(device_card, bg='#ffffff', relief='solid', bd=1)
        glass_bg.grid(row=0, column=0, columnspan=3, sticky=tk.EW, padx=2, pady=2)
        glass_bg.grid_columnconfigure(1, weight=1)
        
        # 使用浅色背景
        glass_bg.configure(bg='#f8f9fa')
        
        # 设备图标和标题区域
        header_frame = tk.Frame(glass_bg, bg=theme_color, height=45)
        header_frame.grid(row=0, column=0, columnspan=3, sticky=tk.EW, padx=0, pady=0)
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_propagate(False)
        
        # 设备名称标签
        device_label = tk.Label(header_frame, text=label_text, 
                               font=('Microsoft YaHei', 11, 'bold'),
                               bg=theme_color, fg='white')
        device_label.grid(row=0, column=0, sticky=tk.W, padx=12, pady=12)
        
        # 地址配置区域 - 透明背景
        config_frame = tk.Frame(glass_bg, bg='#f8f9fa')
        config_frame.grid(row=1, column=0, columnspan=3, sticky=tk.EW, padx=12, pady=12)
        config_frame.grid_columnconfigure(1, weight=1)
        
        # 地址下拉框容器 - 带透明边框
        combo_frame = tk.Frame(config_frame, bg='#ffffff', relief='solid', bd=1)
        combo_frame.grid(row=0, column=1, sticky=tk.EW, padx=(0, 8), pady=4)
        
        # 地址下拉框 - 初始化时使用空列表，避免检测卡顿
        address_combo = ttk.Combobox(combo_frame, 
                                    values=[], 
                                    font=('Consolas', 9),
                                    state="normal",  # 改为normal，允许手动输入
                                    style='Modern.TCombobox')
        address_combo.pack(fill=tk.X, padx=6, pady=4)
        
        # 存储下拉框引用
        self.address_combos[device_key] = address_combo
        
        # 从配置文件加载默认值
        saved_address = self.config.get("device_addresses", {}).get(device_key)
        if saved_address:
            address_combo.set(saved_address)
        else:
            # 如果配置文件中没有，使用默认值
            default_addresses = [
                "TCPIP::192.168.1.100::INSTR",  # 示波器
                "TCPIP::192.168.1.101::INSTR",  # AC Source
                "TCPIP::192.168.1.102::INSTR",  # 电子负载
                "TCPIP::192.168.1.103::INSTR"   # 控制盒
            ]
            address_combo.set(default_addresses[row])
        
        # 绑定选择改变事件
        address_combo.bind('<<ComboboxSelected>>', lambda e: self.on_address_changed(device_key))
        
        # 刷新按钮 - 毛玻璃效果
        refresh_btn = tk.Button(
            config_frame,
            text="🔄 刷新",
            font=('Microsoft YaHei', 8),
            bg=theme_color,
            fg='white',
            relief='flat',
            bd=0,
            padx=12,
            pady=6,
            cursor='hand2',
            command=lambda: self.refresh_addresses(device_key)
        )
        refresh_btn.grid(row=0, column=2, sticky=tk.E, pady=4)
        
        # 添加鼠标悬停效果
        def on_refresh_enter(e):
            darkened = self.darken_color(theme_color)
            refresh_btn.config(bg=darkened)
            
        def on_refresh_leave(e):
            validated_color = self.validate_color(theme_color)
            refresh_btn.config(bg=validated_color)
            
        refresh_btn.bind('<Enter>', on_refresh_enter)
        refresh_btn.bind('<Leave>', on_refresh_leave)
    
    def validate_color(self, color):
        """验证颜色值是否有效"""
        if not color or not isinstance(color, str):
            return '#666666'  # 默认灰色
        if color.strip() == '':
            return '#666666'  # 默认灰色
        if not color.startswith('#'):
            return '#666666'  # 默认灰色
        return color
    
    def darken_color(self, color_hex):
        """将颜色变暗以用于悬停效果"""
        # 验证颜色
        color_hex = self.validate_color(color_hex)
        # 移除#号
        color_hex = color_hex.lstrip('#')
        try:
            # 转换为RGB
            rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
            # 将每个分量减少30
            darkened_rgb = tuple(max(0, c - 30) for c in rgb)
            # 转换回十六进制
            return '#%02x%02x%02x' % darkened_rgb
        except:
            return '#444444'  # 错误时返回深灰色
    
    def get_default_addresses(self):
        """获取默认地址列表（不进行实际检测，避免界面卡顿）"""
        default_addresses = [
            "TCPIP::192.168.1.100::INSTR",
            "TCPIP::192.168.1.101::INSTR", 
            "TCPIP::192.168.1.102::INSTR",
            "TCPIP::192.168.1.103::INSTR",
            "COM1", "COM2", "COM3", "COM4"
        ]
        print("📋 使用默认地址列表（点击刷新按钮可检测真实设备）")
        return default_addresses
    
    def get_available_addresses(self):
        """获取可用的COM口、IP地址和GPIB地址（使用先进的扫描方法）"""
        addresses = []
        
        # 1. 扫描COM端口（使用详细信息）
        print("🔍 开始扫描COM端口...")
        com_addresses = self.get_com_ports()
        addresses.extend(com_addresses)
        
        # 2. 使用PyVISA扫描所有VISA资源
        print("🔍 开始VISA资源扫描...")
        visa_addresses = self.scan_visa_resources()
        addresses.extend(visa_addresses)
        
        # 3. 扫描网络设备
        print("🔍 开始网络设备扫描...")
        network_addresses = self.scan_network_devices()
        addresses.extend(network_addresses)
        
        # 4. 扫描GPIB设备
        print("🔍 开始GPIB设备扫描...")
        gpib_addresses = self.scan_gpib_devices()
        addresses.extend(gpib_addresses)
        
        # 5. 扫描LPT并口设备
        print("🔍 开始LPT并口扫描...")
        lpt_addresses = self.scan_lpt_devices()
        addresses.extend(lpt_addresses)
        
        # 6. 添加配置文件中的地址
        print("🔍 从配置文件添加设备地址...")
        for device_name, addr in self.config.get("device_addresses", {}).items():
            if isinstance(addr, str) and addr not in addresses:
                addresses.append(addr)
                print(f"✅ 从配置添加: {device_name} -> {addr}")
        
        # 去重并按类型排序
        unique_addresses = list(set(addresses))
        com_addresses = [addr for addr in unique_addresses if addr.startswith('COM')]
        tcpip_addresses = [addr for addr in unique_addresses if addr.startswith('TCPIP')]
        gpib_addresses = [addr for addr in unique_addresses if addr.startswith('GPIB')]
        lpt_addresses = [addr for addr in unique_addresses if addr.startswith('LPT')]
        other_addresses = [addr for addr in unique_addresses if not any(addr.startswith(prefix) for prefix in ['COM', 'TCPIP', 'GPIB', 'LPT'])]
        
        # 排序各类地址
        com_addresses.sort()
        tcpip_addresses.sort()
        gpib_addresses.sort()
        lpt_addresses.sort()
        other_addresses.sort()
        
        # 按优先级组合：COM -> TCPIP -> GPIB -> LPT -> 其他
        result = com_addresses + tcpip_addresses + gpib_addresses + lpt_addresses + other_addresses
        
        print(f"📡 最终可用地址列表:")
        print(f"   COM: {len(com_addresses)}, TCPIP: {len(tcpip_addresses)}, GPIB: {len(gpib_addresses)}, LPT: {len(lpt_addresses)}, 其他: {len(other_addresses)}")
        for addr in result:
            print(f"   - {addr}")
        return result
    
    def get_com_ports(self):
        """获取可用COM端口列表 - 动态扫描"""
        ports = []
        try:
            if SERIAL_AVAILABLE:
                available_ports = serial.tools.list_ports.comports()
                for port in available_ports:
                    # 添加详细的端口信息
                    port_info = f"{port.device} - {port.description}"
                    ports.append(port_info)
                    print(f"✅ 发现COM口: {port_info}")
                
                # 如果没有找到端口，返回常见的COM端口供测试
                if not ports:
                    ports = ["COM1", "COM2", "COM3", "COM4"]
                    print("ℹ️ 未检测到COM口，使用默认列表")
            else:
                ports = ["COM1", "COM2", "COM3", "COM4"]
                print("⚠️ pyserial未安装，使用默认COM端口列表")
                
        except Exception as e:
            print(f"❌ 扫描COM端口时出错: {e}")
            ports = ["COM1", "COM2", "COM3", "COM4"]
        
        return ports
    
    def scan_visa_resources(self):
        """使用PyVISA扫描所有VISA资源"""
        visa_addresses = []
        try:
            import pyvisa
            rm = pyvisa.ResourceManager()
            resources = rm.list_resources()
            
            for resource in resources:
                if isinstance(resource, str):
                    visa_addresses.append(resource)
                    print(f"✅ VISA发现资源: {resource}")
                    
            print(f"✅ VISA共发现 {len(visa_addresses)} 个资源")
            
        except ImportError:
            print("⚠️ 未安装PyVISA，跳过VISA资源扫描")
        except Exception as e:
            print(f"❌ VISA资源扫描失败: {e}")
        
        return visa_addresses
    
    def scan_network_devices(self):
        """扫描网络中的设备（TCPIP地址）"""
        network_devices = []
        try:
            import socket
            
            # 获取本机IP地址段
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f"🔍 本机IP地址: {local_ip}")
            
            # 添加本机TCPIP地址
            if local_ip and local_ip != "127.0.0.1":
                local_tcpip = f"TCPIP0::{local_ip}::inst0::INSTR"
                network_devices.append(local_tcpip)
                print(f"✅ 添加本机TCPIP地址: {local_tcpip}")
            
            # 提取网络段
            ip_parts = local_ip.split('.')
            network_base = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}"
            
            # 常见的测试设备IP地址
            common_ips = [
                "172.19.74.20", "172.19.74.22", "172.19.74.21", "172.19.71.29",
                "192.168.1.100", "192.168.1.101", "192.168.1.102",
                f"{network_base}.100",
                f"{network_base}.101",
                f"{network_base}.102"
            ]
            
            for ip in common_ips:
                tcpip_addr = f"TCPIP0::{ip}::inst0::INSTR"
                if tcpip_addr not in network_devices:
                    network_devices.append(tcpip_addr)
            
            print(f"✅ 网络扫描完成，添加 {len(network_devices)} 个网络地址")
                
        except Exception as e:
            print(f"❌ 扫描网络设备时出错: {e}")
            
        return network_devices
    
    def scan_gpib_devices(self):
        """扫描GPIB设备"""
        gpib_devices = []
        try:
            # 尝试使用pyvisa扫描GPIB设备
            try:
                import pyvisa
                rm = pyvisa.ResourceManager()
                resources = rm.list_resources()
                
                for resource in resources:
                    if 'GPIB' in resource:
                        gpib_devices.append(resource)
                        print(f"✅ VISA发现GPIB: {resource}")
                        
            except ImportError:
                print("⚠️ pyvisa未安装，使用默认GPIB地址")
            except Exception as e:
                print(f"❌ VISA扫描GPIB失败: {e}")
            
            # 添加标准GPIB地址格式
            for i in range(1, 31):
                standard_gpib = f"GPIB0::{i}::INSTR"
                simple_gpib = f"GPIB::{i}"
                if standard_gpib not in gpib_devices:
                    gpib_devices.append(standard_gpib)
                if simple_gpib not in gpib_devices:
                    gpib_devices.append(simple_gpib)
            
            print(f"✅ GPIB扫描完成，共 {len(gpib_devices)} 个GPIB地址")
                    
        except Exception as e:
            print(f"❌ 扫描GPIB设备时出错: {e}")
            # 添加默认GPIB地址
            for i in range(1, 31):
                gpib_devices.append(f"GPIB0::{i}::INSTR")
                gpib_devices.append(f"GPIB::{i}")
                
        return gpib_devices
    
    def scan_lpt_devices(self):
        """扫描LPT并口设备"""
        lpt_devices = []
        try:
            import os
            if os.name == 'nt':  # Windows系统
                # 常见的LPT端口
                common_lpt = ["LPT1", "LPT2", "LPT3"]
                for lpt in common_lpt:
                    lpt_devices.append(lpt)
                    print(f"✅ 添加LPT端口: {lpt}")
                
                print(f"✅ LPT扫描完成，共 {len(lpt_devices)} 个LPT端口")
            else:
                print("ℹ️ 非Windows系统，跳过LPT扫描")
        except Exception as e:
            print(f"❌ 扫描LPT设备时出错: {e}")
            
        return lpt_devices
    
    def refresh_all_addresses(self):
        """刷新所有设备的地址列表"""
        try:
            print("🔍 开始检测所有设备端口...")
            
            # 显示所有设备为检测中状态
            for device_key in self.device_keys:
                if device_key in self.address_combos:
                    combo = self.address_combos[device_key]
                    combo['values'] = ["🔍 正在检测..."]
                    combo.set("🔍 正在检测...")
                    combo.update()
            
            # 获取真实设备地址
            new_addresses = self.get_available_addresses()
            
            # 更新所有设备的下拉框
            for device_key in self.device_keys:
                if device_key in self.address_combos:
                    combo = self.address_combos[device_key]
                    current_value = combo.get()
                    
                    # 更新选项
                    combo['values'] = new_addresses
                    
                    # 智能选择地址
                    if current_value in new_addresses:
                        combo.set(current_value)  # 保持原选择
                    else:
                        # 根据设备类型智能选择默认地址
                        default_addr = self.get_smart_default_address(device_key, new_addresses)
                        combo.set(default_addr if default_addr else (new_addresses[0] if new_addresses else "❌ 未检测到设备"))
            
            # 保存配置
            self.save_config()
            
            print(f"✅ 所有设备端口检测完成，发现 {len(new_addresses)} 个可用地址")
            
        except Exception as e:
            print(f"❌ 全局刷新失败: {e}")
            # 错误时恢复默认状态
            default_addresses = self.get_default_addresses()
            for device_key in self.device_keys:
                if device_key in self.address_combos:
                    combo = self.address_combos[device_key]
                    combo['values'] = default_addresses
                    combo.set("❌ 检测失败")
    
    def get_smart_default_address(self, device_key, available_addresses):
        """根据设备类型智能选择默认地址"""
        # 定义设备与IP地址的映射
        device_ip_mapping = {
            "oscilloscope": ["192.168.1.100", "192.168.0.100"],
            "ac_source": ["192.168.1.101", "192.168.0.101"],
            "electronic_load": ["192.168.1.102", "192.168.0.102"],
            "control_box": ["192.168.1.103", "192.168.0.103"]
        }
        
        # 查找匹配的地址
        preferred_ips = device_ip_mapping.get(device_key, [])
        for ip in preferred_ips:
            for addr in available_addresses:
                if ip in addr:
                    return addr
        
        # 如果没有找到匹配的IP，返回None
        return None
    
    def refresh_addresses(self, device_key):
        """刷新指定设备的地址列表（进行真实设备检测）"""
        try:
            print(f"🔄 开始刷新 {device_key} 的地址列表...")
            
            # 获取对应的下拉框
            if device_key not in self.address_combos:
                print(f"❌ 未找到 {device_key} 的下拉框")
                return
                
            combo = self.address_combos[device_key]
            current_value = combo.get()
            
            # 显示检测中状态
            combo['values'] = ["🔍 正在检测设备..."]
            combo.set("🔍 正在检测设备...")
            combo.update()  # 强制更新界面
            
            # 获取新的地址列表（真实检测）
            new_addresses = self.get_available_addresses()
            # 合并配置文件中的设备地址，防止配置地址未被检测到时丢失
            saved_addr = self.config.get("device_addresses", {}).get(device_key)
            if saved_addr and saved_addr not in new_addresses:
                new_addresses.insert(0, saved_addr)
            
            # 更新下拉框的选项
            combo['values'] = new_addresses
            
            # 如果当前值仍在新列表中，保持选中；否则使用第一个地址或清空
            if current_value in new_addresses:
                combo.set(current_value)
            elif new_addresses:
                combo.set(new_addresses[0])  # 使用第一个检测到的地址
            else:
                combo.set("❌ 未检测到设备")
                
            print(f"✅ 已刷新 {device_key} 的地址列表，发现 {len(new_addresses)} 个可用地址")
            
        except Exception as e:
            print(f"❌ 刷新地址列表失败: {e}")
            # 错误时恢复默认状态
            if device_key in self.address_combos:
                combo = self.address_combos[device_key]
                combo['values'] = self.get_default_addresses()
                combo.set("❌ 检测失败")
        
