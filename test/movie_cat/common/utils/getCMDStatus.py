import paramiko
class getCMDStatus():
    def session(self, host, port, username, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, int(port), username, password)
            # print('login %s is successful' % host)
            return ssh
        except Exception as e:
            print(e)
    def getOperaResultStatus(self,host,username='wxgz',password='wxgz',port=22,tomcatPath='/home/wxgz/',tomcatProjectName='infobeat-web'):
        client = self.session(host, port, username, password)
        Opera_result_cmd = 'echo $?'
        stdin, stdout, stderr = client.exec_command(Opera_result_cmd)
        OperaResultStatus = stdout.read()
        print('getCMDStatus===========执行了'+str(OperaResultStatus))
        return OperaResultStatus