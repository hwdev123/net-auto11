from netmiko import ConnectHandler
from getpass import getpass
from getpass import getuser

username = getuser()
# password = getpass("Password: ")

CAT_3650 = {
    "host": "10.50.50.200",
    "username": username,
    "password": "cisco123",
    "device_type": "cisco_xe"
}

net_connect = ConnectHandler(**CAT_3650)

config = [
    "vlan 100", "name MGMT", "int vlan 100", "ip add 10.100.100.200 255.255.255.0", "no shut", "description MGMT VLAN"
]

config_output = net_connect.send_config_set(config)

prompt = net_connect.find_prompt()
hostname = prompt[:-1]
print("*" * 80)
print(f"Connecting to: {hostname}")
print("*" * 80)
print(config_output)
print("*" * 80)
print("Device Successfully configured")
print("*" * 80)
net_connect.cleanup()


