"""
获取tomcat信息
"""
import paramiko


class TomcatInfo():
    def session(self, host, port, username, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, int(port), username, password)
            # print('login %s is successful' % host)
            return ssh
        except Exception as e:
            print(e)

    # # 获取tomcat状态
    ## 0：tomcat进程正常
    ## 非0：tomcat进程不在
    def getTomcatStatus(self, host, username='wxgz', password='wxgz', port=22, tomcatPath='/home/wxgz/',
                        tomcatProjectName='infobeat-web'):
        tomcatStatus_cmd = 'ps -ef|grep %s|grep -v grep' % tomcatProjectName
        # tomcatStatus = 'ps -ef|grep %s' %tomcatProjectName
        print('检查tomcat进程：' + str(tomcatStatus_cmd))
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command(tomcatStatus_cmd + ';' + 'echo $?', get_pty=True)
        tomcatStatus = stdout.read()
        tomcatStatus = str(tomcatStatus, encoding='utf-8').strip()[-1]
        print('======tomcatStatus echo $? =========:' + tomcatStatus)
        if tomcatStatus == '0':
            print(tomcatProjectName + "服务进程正常")
        else:
            print(print(tomcatProjectName + "服务进程不正常"))
        return tomcatStatus

    def rebootTomcat(self, host, username='wxgz', password='wxgz', port=22, tomcatPath='/home/wxgz/',
                     tomcatProjectName='infobeat-web'):
        # tomcatOpera_cmd = 'sh %s%s/bin/startup.sh >> /dev/null && echo $?'%(tomcatPath,tomcatProjectName)
        tomcatOpera_cmd = 'sh %s%s/bin/startup.sh' % (tomcatPath, tomcatProjectName)
        print('重启tomcat服务：' + str(tomcatOpera_cmd))
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command(tomcatOpera_cmd + ';' + 'echo $?', get_pty=True)
        rebootResult = str(stdout.read(), encoding='utf-8').strip()
        rebootResultStatus = rebootResult[-1]
        if rebootResultStatus == '0':
            print('重启成功！')
        else:
            tomcatStatus = self.getTomcatStatus(host)
            if tomcatStatus == '0':
                print('重启失败，进程已经存在！')
            else:
                print('重启失败，原因请登录服务器查看')
        #
        # print('此处为空:', str(stdout.read(),encoding='utf-8'))
        #
        # print('未删减前：', len(result))
        #
        # print('删减后：', len(result.strip()))
        # after = result.strip()
        # j = 0
        # for i in after:
        #     print('第'+str(j)+'序列'+i)
        #     j+=1
        # print(type(tomcatOperaStatus))
        # print('命令执行结果状态',after[-1])
        # print('重启操作结果：' +tomcatOperaStatus )

        # tomcatStatus_cmd = 'ps -ef|grep %s|grep -v grep >> /dev/null && echo $?' % tomcatProjectName
        # client = self.session(host, port, username, password)
        # stdin, stdout, stderr = client.exec_command(tomcatStatus_cmd)
        # tomcatStatus = stdout.read()
        # tomcatOperaResultStatus = str(tomcatStatus, encoding='utf-8')
        # if tomcatOperaResultStatus != None:
        #     print('重启操作成功')
        # else:
        #     print('重启操作失败')
        return rebootResultStatus
