from netmiko import ConnectHandler
SW1 = {
    'device_type':'cisco_iso',
    'ip':'10.215.27.165',
    'username':'vnpro',               #username truy cập SSH vào Switch
    'password':'vnpro#123',           #password của SSH
    'secret':'vnpro#321',             #password enable SwitchSwitch
}
net_connect = ConnectHandler(**SW1)   #tạo kết nối tới SW1
net_connect.enable()                    #tạo kết nối vào mode enable

for n in range (10,31):
    taoVlan=['vlan' + str(n)]
    ipVlan=['int vlan'+str(n),'ip add 172.16.'+str(n)+'.1 255.255.255.0','no shutdown']
    output = net_connect.send_config_set(taoVlan)
    output = net_connect.send_config_set(ipVlan)
output = net_connect.send_command('show ip interface brief|i Vlan')
print(output)