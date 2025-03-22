from netmiko import ConnectHandler

SW1 = {
    'device_type': 'cisco_ios',  # Đổi từ 'cisco_iso' sang 'cisco_ios'
    'ip': '10.215.27.165',
    'username':'vnpro',               #username truy cập SSH vào Switch
    'password':'vnpro#123',           #password của SSH
    'secret':'vnpro#321',             #password enable SwitchSwitch
}

# Kết nối SSH
net_connect = ConnectHandler(**SW1)
net_connect.enable()  # Vào chế độ enable

# Cấu hình VLAN từ 10 đến 30
for n in range(10, 31):
    commands = [
        f'vlan {n}',
        f'name VLAN_{n}',
        'exit',
        f'interface vlan {n}',
        f'ip address 172.16.{n}.1 255.255.255.0',
        'no shutdown'
    ]
    output = net_connect.send_config_set(commands)
    print(output)  # Hiển thị output để kiểm tra

# Hiển thị thông tin các VLAN đã tạo
output = net_connect.send_command('show ip interface brief | include Vlan')
print(output)

# Đóng kết nối
net_connect.disconnect()