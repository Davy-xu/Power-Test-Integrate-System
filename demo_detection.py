#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""演示地址检测功能"""

import socket

def demo_address_detection():
    print("🔍 演示地址检测功能...")
    
    addresses = []
    
    # 检测COM口
    try:
        import serial.tools.list_ports
        com_ports = serial.tools.list_ports.comports()
        for port in com_ports:
            addresses.append(port.device)
        print(f"✅ 检测到 {len(com_ports)} 个COM口: {[p.device for p in com_ports]}")
    except ImportError:
        print("⚠️ 未安装pyserial，使用默认COM口列表")
        addresses.extend(["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8"])
    
    # 检测IP地址
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"🌐 本机IP: {local_ip}")
        
        # 生成示例TCPIP地址
        example_ips = [
            "172.19.71.25",  # 示例IP
            "192.168.1.100", "192.168.1.101", "192.168.1.102",
            local_ip
        ]
        
        for ip in example_ips:
            addresses.append(f"TCPIP0::{ip}::inst0::INSTR")
            addresses.append(f"TCPIP::{ip}::INSTR")
            
    except Exception as e:
        print(f"❌ IP检测失败: {e}")
    
    # 显示结果
    com_addresses = [addr for addr in addresses if addr.startswith('COM')]
    tcpip_addresses = [addr for addr in addresses if addr.startswith('TCPIP')]
    
    print(f"\n📋 地址检测结果:")
    print(f"  COM口 ({len(com_addresses)} 个):")
    for addr in com_addresses[:5]:  # 显示前5个
        print(f"    • {addr}")
    
    print(f"  TCPIP地址 ({len(tcpip_addresses)} 个):")
    for addr in tcpip_addresses[:8]:  # 显示前8个
        print(f"    • {addr}")
    
    print(f"\n🎯 总共检测到 {len(addresses)} 个地址")
    print("\n✅ 设备端口功能已更新完成:")
    print("  • 移除了'连接'按钮")
    print("  • 添加了'刷新'功能")
    print("  • 自动检测COM口和IP地址")
    print("  • 支持TCPIP0::IP::inst0::INSTR格式")

if __name__ == "__main__":
    demo_address_detection()
