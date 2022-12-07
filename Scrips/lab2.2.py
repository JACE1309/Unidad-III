'''
Jahir Artemio Casas Espínola
Scrip laboratorio 2.2
'''

from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type= 'cisco_ios',
    host= '10.10.20.70',
    port= 2221,
    username= 'admin',
    password= 'admin'
    )

config_commands = [
    'int loopback'
    'ipv4 add 192.168.4.1 255.255.255.0'
    'no shutdown'
    'description LABORATORIO 2'
]

loopbak2 = [
    'int loopback 2'
    'ipv4 add 192.168.4.2 255.255.255.0'
    'no shutdown'
    'description LABORATORIO 2 loopbak 2'
]

sshCli.send_command('configure terminal', expect_string =r"", read_timeout=150)
sshCli.send_config_set("loopbak2")
resultado = sshCli.send_command('show run')
print(resultado)