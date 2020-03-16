from subprocess import Popen,PIPE
import re
import os,sys
import paramiko


class GetLinuxMessage:
#登录远程Linux系统
    def session(self, host, port, username, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, int(port), username, password)
            #print('login %s is successful' % host)
            return ssh
        except Exception as e:
            print(e)
#获取Linux主机名
    def get_hostname(self, host, port=22, username="root", password="Szlocal!!!"):
            cmd_hostname = "cat /etc/hostname"
            client = self.session(host, port, username, password)
            stdin, stdout, stderr = client.exec_command(cmd_hostname)
            hostname = stdout.read()
            return hostname

# 获取Linux系统总memory信息
    def get_total_memory(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        # with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('MemTotal'):
                memory = int(i.split()[1].strip())
            else:
                pass
        return memory
# 获取Linux系统空闲memory信息
    def get_free_memory(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        # with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('MemFree'):
                memory = int(i.split()[1].strip())
                memory = '%.f' % (memory / 1024.0)
            else:
                pass
        return memory
# 获取Linux系统可用memory信息
    def get_ava_memory(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        # with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('MemAvailable'):
                memory = int(i.split()[1].strip())
                memory = '%.f' % (memory / 1024.0)
            else:
                pass
        return memory
# 获取Linux系统缓存memory信息
    def get_cach_and_buff_memory(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
        meminfo = stdout.readlines()
        # with open('/proc/meminfo') as meminfo:
        for i in meminfo:
            if i.startswith('Buffers'):
                Buffers_memory = int(i.split()[1].strip())
                Buffers_memory = '%.f' % (Buffers_memory / 1024.0)
            else:
                pass
        for i in meminfo:
            if i.startswith('Cached'):
                Cached_memory = int(i.split()[1].strip())
                Cached_memory = '%.f' % (Cached_memory / 1024.0)
            else:
                pass
        return int(Buffers_memory)+int(Cached_memory)
# 获取Linux系统网络IP信息
    def get_network_info(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("ifconfig")
        data = stdout.read().decode('utf-8')
        ret = re.compile('((?:1[0-9][0-9]\.)|(?:25[0-5]\.)|(?:2[0-4][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))')
        match = ret.search(data).group()
        return  match
#获取Linux系统CPU信息
    def get_cpu_info(self, host, port=22, username="root", password="Szlocal!!!"):
        cpunum = 0
        processor = 0
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /proc/cpuinfo")
        cpuinfo = stdout.readlines()
        #with stdout.read() as cpuinfo:
        for i in cpuinfo:
            if i.startswith('physical id'):
                cpunum = i.split(":")[1]
            if i.startswith('processor'):
                processor = processor + 1
            if i.startswith('model name'):
                cpumode = i.split(":")[1]
        return int(cpunum)+1, processor,cpumode


#获取Linux系统版本信息
    def get_os_version(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("cat /etc/redhat-release")
        data = stdout.read()
        return data

#获取Linux系统网卡MAC信息
    def get_network_MAC(self, host, port=22, username="root", password="Szlocal!!!"):
        client = self.session(host, port, username, password)
        stdin, stdout, stderr = client.exec_command("ifconfig ens160 |egrep 'ether' |awk '{print $2}'")
        data = stdout.read()
        print(data)
        return data


if __name__ == '__main__':

    from movie_cat.config.local_setting import hosts
    hosts = hosts.split(',')
    print(hosts)
    hosts_dict = {}
    for host in hosts:
        print('主机IP为%s的系统信息：'%host)
        result = GetLinuxMessage()
        #hostIP = '172.10.4.100'
        hostIP = host
        host_name = result.get_hostname(hostIP)
        total_memory = result.get_total_memory(hostIP)
        result.get_free_memory(hostIP)
        #print('主机缓存：'+str(result.get_cach_and_buff_memory(hostIP)))
        cache_and_buff = result.get_cach_and_buff_memory(hostIP)
        #print('主机可用内存：'+ str(result.get_ava_memory(hostIP)))
        ava_memory = result.get_ava_memory(hostIP)
        #print('主机名：'+ str(host_name))
        #print('主机总内存：'+ str(total_memory))
        #print('主机IP：'+ result.get_network_info(hostIP))
        host_IP = result.get_network_info(hostIP)
        #print('主机cpu物理核数：'+ str(result.get_cpu_info(hostIP)[0]))
        cpu_physical_num = str(result.get_cpu_info(hostIP)[0])
        #print('主机cpu逻辑核数：' + str(result.get_cpu_info(hostIP)[1]))
        cpu_processor_num = str(result.get_cpu_info(hostIP)[1])
        #print('主机cpu型号_cpu_kind：' + result.get_cpu_info(hostIP)[2])
        cpu_kind = result.get_cpu_info(hostIP)[2]
        #print(result.get_os_version(hostIP))
        os_version = result.get_os_version(hostIP)
        os_network_MAC = result.get_network_MAC(hostIP)
        os_network_MAC = str(os_network_MAC, encoding='utf-8')[0:-1]
        print('os_network_MAC:=========>'+os_network_MAC)
        host_list = {}
        host_name = str(host_name,encoding='utf-8')[0:-1]
        host_list['host_name'] = host_name
        host_list['host_IP'] = host_IP
        host_list['cpu_physical_num'] = cpu_physical_num
        host_list['cpu_processor_num'] = cpu_processor_num
        cpu_kind = cpu_kind[0:-1]
        host_list['cpu_kind'] = cpu_kind
        host_list['total_memory'] = total_memory
        host_list['ava_memory'] = ava_memory
        host_list['cache_and_buff'] = cache_and_buff
        os_version = str(os_version,encoding='utf-8')[0:-1]
        host_list['os_version'] = os_version

        print('===========================================================')
        # print(type(host_name))
        # print(type(host_IP))
        # print(type(cpu_physical_num))
        # print(type(cpu_processor_num))
        # print('cpu_kind'+str(type(cpu_kind)))
        # print(type(total_memory))
        # print(type(ava_memory))
        # print(type(cache_and_buff))
        # print(type(os_version))
        # print(host_list)
        import json
        host_info_json = json.dumps(host_list)
        print(host_info_json)
        hosts_dict[os_network_MAC] = host_info_json







