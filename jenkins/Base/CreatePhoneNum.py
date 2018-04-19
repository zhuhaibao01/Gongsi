#coding=utf-8
import random, sys,requests
import MySQLdb
sys.path.append('..')

def a():
    topthreelist = [130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 151, 152, 153, 155, 156, 157, 158, 159, 176, 177,
                    180, 181, 182, 183, 184, 185, 186, 187, 188, 189]
    num = random.randint(1,30)
    num_8 = random.randint(11111110, 99999999)
    return str(topthreelist[num-1]) + str(num_8)

def sql(sql1):
    host = '10.10.100.206'
    port = 3306
    username = 'root'
    passwd = 'admin'
    db = 'smedia_center'
    conn = MySQLdb.connect(host=host, port=port, user=username, passwd=passwd, db=db, charset='utf8')
    cur = conn.cursor()
    data = cur.execute(sql1)
    result = cur.fetchall()
    mysqlphonelist = []
    for i in result:
        mysqlphonelist.append(i[0])
    cur.close()
    return mysqlphonelist


def allSql():
    '''
     sql1 查询所有的注册号码
     sql2 查询所有身份认证的手机号码
     sql3 查询所有的新媒人认证的手机号码
     sql4 查询查询服务商未认证的电话号码
     sql5 查询服务商已认证的电话号码
     sql6 查询服务商里的电话号码
     sql7 查询已经激活企业主的手机号
    '''
    sqlist={'sql1':'select user_name from s_member',
         'sql2':'select user_name from s_member where id in (select user_id from s_idcard)',
         'sql3':'select user_name from s_member where id =(select user_id from s_member_partner where status=\'PRE_PASS\' limit 1)',
         'sql4':'select user_name from s_member where id =(select user_id from s_member_city_operators where status=\'PRE_AUTH\' limit 1)',
         'sql5':'select user_name from s_member where id =(select user_id from s_member_city_operators where status=\'PRE_PASS\' limit 1)',
         'sql6':'select user_name from s_member where id in (select user_id from s_member_city_operators)',
         'sql7':'select user_name from s_member where id=(select user_id from s_member_entrepreneur where status=\'ALREADY_ACTIVATED\' limit 1)'
         }
    return sqlist

# print sql(allSql()['sql1'])[random.randint(1,len(allSql()['sql1']))]


def AutoMysqlPhoneIsOrNo(phonenum):
    """
    该方法实该查询数据库是否有该手机号，如果没有重新生成一个。
    """
    Mqlist=sql(allSql()['sql1'])
    if phonenum not in Mqlist:
        mobile = {'mobile': phonenum}
        # print mobile['mobile']
        url1 = 'http://10.10.100.206/ucenter/member/sendRegisterMessage'
        # url1 = 'http://10.10.100.163:8085/ucenter/member/sendRegisterMessage'
        r = requests.post(url=url1, data=mobile)
        # print r.json()
        # 连接到数据库
        conn = MySQLdb.connect(host='10.10.100.206', port=3306, user='root', passwd='admin', db='smedia_center',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute('select text from s_sms_log order by appdate desc limit 1')
        data = cur.fetchall()
        vitycode = data[0][0][3:9]
        # print vitycode
        cur.close()
        url2= 'http://10.10.100.206/ucenter/member/checkVerificationCode'
        # url2 = 'http://10.10.100.163:8085/ucenter/member/checkVerificationCode'
        content = {'userName': mobile['mobile'], 'code': vitycode}
        # print content['userName']
        r = requests.get(url=url2, params=content)
        # print r.json()
        token = r.json()['entity']
        print r.json()['entity']
        url3 = 'http://10.10.100.206/ucenter/member/registeredUser'
        # url3 = 'http://10.10.100.163:8085/ucenter/member/registeredUser'
        headers = {'Content-Type': 'application/json'}
        content = 'userName=%s&userPwd=123456&token=%s' % (mobile['mobile'], token)
        r = requests.post(url3 + "?" + content, headers=headers)
        # print r.json()
        print u"手机号%s不在数据库里,现在已经重新生成"%phonenum
        return phonenum
    else:
        print u"手机号%s已经在数据库存在" % phonenum
        return phonenum
# print AutoMysqlPhoneIsOrNo('13700000011')

def get_IdOrToken(sql):
    """
    获取token的方法,返回的元组
            0为usrId,
            1位usrtoken
            2为获取的header
            例如print(get_IdOrToken(sql(allSql()['sql1'])[0])[2])
    """
    content = {'userName':sql, 'userPwd':123456}
    # url = 'http://10.10.100.163:8085/ucenter/memberlogin/login'
    url = 'http://10.10.100.206/ucenter/memberlogin/login'
    r = requests.post(url=url, data=content)
    usrtoken = r.json()['entity']['token']
    usrId = r.json()['entity']['userId']
    header = {
        'X-AUTH-TOKEN': 'c230f588a4b04b44a577e47220175e9e',
        'X-USER-TOKEN': usrtoken
    }
    return (usrId,usrtoken,header)

# print(sql(allSql()['sql6']))
# print(get_IdOrToken(sql(allSql()['sql6'])[1]))

# 生成未注册的手机号方法（不在已注册的手机号里）
def C(phton_list):
    while True:
        phone = a()
        try:
            if phone in phton_list:
                continue
            return phone
        except BaseException as e:
            print e
C(sql(allSql()['sql1']))
# print int(C(sql(allSql()['sql1'])))


def kk():
    '''
    生成未进行新媒人认证的首媒手机号
    '''
    b=sql(allSql()['sql2'])
    a=sql(allSql()['sql1'])
    for i in b:
        if i in a:
            a.remove(i)
    return a
e=kk()
# print e[random.randint(1,len(e)-1)]

def kk1():
    '''
    生成未进行服务商认定的首媒手机号 
    '''
    b = sql(allSql()['sql6'])
    a = sql(allSql()['sql1'])
    for i in b:
        if i in a:
            a.remove(i)
    return a
ee=kk1()
# print ee[random.randint(1,len(ee)-1)]
