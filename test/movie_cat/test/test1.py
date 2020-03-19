from movie_cat.common.utils.getCurentUser import getCurentUser
# result = getCurentUser()
# host = '172.10.4.100'
# userName = str(result.get_hostUserName(host),encoding='utf-8')
# #os_network_MAC = str(os_network_MAC, encoding='utf-8')[0:-1]
# print('===============================')
# print('当前用户名：'+userName)


from movie_cat.common.libs.tomcat_info import TomcatInfo
result = TomcatInfo()
host = '172.10.4.102'
result.getTomcatStatus(host)
status = result.rebootTomcat(host)
print(status)


