"""
获取当前操作系统用户对象
"""
import paramiko
class getCurentUser():

    def session(self, host, port, username, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, int(port), username, password)
            # print('login %s is successful' % host)
            return ssh
        except Exception as e:
            print(e)

    # 获取Linux用户名
    def get_hostUserName(self, host, port=22, username="wxgz", password="wxgz"):
        cmd_hostUserName = "echo $USER"
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command(cmd_hostUserName)
        hostUserName = stdout.read()
        return hostUserName