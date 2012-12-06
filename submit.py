#!/usr/bin/python
import urllib, urllib2
import sys
import json
import os
from getpass import getpass
r=lambda : sys.stdin.readline()

def get_source(filename):
    if not os.path.exists(filename):
        return ({'error':True,'error_text':'No such file %s'%filename},'')
    fp = open(filename,'r')
    source = fp.read()
    fp.close()
    return ({'error':False},source)

def submit(username, password, problem_id, source, language):
    url = 'http://www.acmicpc.net/cmd/submit.php'
    values = {'username':username, 'password':password,
            'problem_id':problem_id,'source':source,
            'language':language}
    data = urllib.urlencode(values)
    req = urllib2.Request(url,data)
    response = urllib2.urlopen(req)
    result = response.read()
    response.close()
    result = json.loads(result)
    return result

def main():
    argv = sys.argv[1:]
    if len(argv) != 2:
        print 'usage: python submit.py problem_id filename'
        return
    problem_id = int(argv[0])
    filename = argv[1]
    language = 1
    res,source = get_source(filename)
    if res['error']:
        print res['error_text']
        return

    sys.stdout.write('Username: ')
    username = r().strip()
    password = getpass()
    if len(username) == 0:
        print 'Please type username'
        return
    if len(password) == 0:
        print 'Please type password'
        return
    res = submit(username,password,problem_id,source,language)
    if res['error']:
        print res['error_text']
        return
    
if __name__ == '__main__':
    main()
