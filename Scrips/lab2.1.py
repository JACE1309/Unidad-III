'''
Jahir Artemio Casas Espínola 
Scrip Laboratorio 2.1
'''

from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type= 'cisco_ios',
    host= '10.10.20.70',
    port= 2221,
    username= 'admin',
    password= 'admin'
    )

#output = sshCli.send_command("show ip int brief", expect_string =r"#",
#                             read_timeout=10)
#print("show ip int brief:\n{}\n".format(output))
#print(output)


#sshCli = ConnectHandler(**sshCli)
sshCli.send_command('configure terminal', expect_string =r"", read_timeout=150)
sshCli.send_config_set(['int loopback 1','ipv4 address 2.2.2.2 255.255.0',"description laborarorio 2"])
output = sshCli.send_command('do show run')


