import paramiko
from movie_cat.common.libs.linux_info import GetLinuxMessage
hostname = GetLinuxMessage.get_hostname('172.10.4.100',port=22,username='wxgz',password='!234Qwer')
print(hostname)

# #获取Linux主机名
#     def get_hostname(self, host, port=22, username="root", password="Szlocal!!!"):
#             cmd_hostname = "cat /etc/hostname"
#             client = self.session(host, port, username, password)
#             stdin, stdout, stderr = client.exec_command(cmd_hostname)
#             hostname = stdout.read()
#             return hostname