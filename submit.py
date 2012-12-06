#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib, urllib2
import sys
import json
import os
from getpass import getpass
r=lambda : sys.stdin.readline()

def get_source(filename):
    if not os.path.exists(filename):
        return ({'error':True,'error_text':'%s는 없는 파일 입니다.'%filename},'')
    fp = open(filename,'r')
    source = fp.read()
    fp.close()
    return ({'error':False},source)

def get_language(filename):
    dummy, extension = os.path.splitext(filename)
    if len(extension) == 0:
        return -1
    if extension in ['.c']:
        return 0
    elif extension in ['.cpp','.cc','cxx']:
        return 1
    elif extension in ['.pas']:
        return 2
    elif extension in ['.java']:
        return 3
    elif extension in ['.rb']:
        return 4
    elif extension in ['.sh']:
        return 5
    elif extension in ['.py']:
        return 6
    elif extension in ['.php']:
        return 7
    elif extension in ['.pl']:
        return 8
    elif extension in ['.cs']:
        return 9
    elif extension in ['.m']:
        return 10
    elif extension in ['.go']:
        return 12
    elif extension in ['.f95','.for']:
        return 13
    elif extension in ['.scm']:
        return 14
    elif extension in ['.scala']:
        return 15
    elif extension in ['.lua']:
        return 16
    elif extension in ['.js']:
        return 17
    elif extension in ['.coffee']:
        return 18
    elif extension in ['.ada']:
        return 19
    elif extension in ['.vb']:
        return 20
    elif extension in ['.awk']:
        return 21
    elif extension in ['.ml']:
        return 22
    elif extension in ['.bf']:
        return 23
    elif extension in ['.ws']:
        return 24
    elif extension in ['.tcl']:
        return 26
    elif extension in ['.d']:
        return 29
    return -1

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
        print '사용법: python submit.py problem_id filename'
        return
    problem_id = int(argv[0])
    filename = argv[1]
    language = 1
    res,source = get_source(filename)
    if res['error']:
        print res['error_text']
        return
    language = get_language(filename)
    if language == -1:
        print '무슨 언어인지 모르겟어요. 확장자를 확인해 주세요.'
        return
    sys.stdout.write('아이디: ')
    username = r().strip()
    password = getpass('비밀번호: ')
    if len(username) == 0:
        print '아이디를 입력해 주세요.'
        return
    if len(password) == 0:
        print '비밀번호를 입력해 주세요.'
        return
    res = submit(username,password,problem_id,source,language)
    if res['error']:
        print res['error_text']
        return
    
if __name__ == '__main__':
    main()
