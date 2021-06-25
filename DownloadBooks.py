# import os
# import sys
import requests
import urllib3
# import pyinputplus
try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  
query = input('Book you want a download of: ')
query1 = query + ' PDF'
links = []
for j in search(query1, tld="co.in", num=20, stop=20, pause=2):
    links.append(j)

for i in range(len(links)):
    urls = links[i]
    if urls[-4:] == '.pdf':
        break

if urls == None:
    print('No Results found')
else:
    r = requests.get(urls, verify=False)
    username = input('What is your computer username: ')
    username = username.strip()
    name = input('How do you want to save the file(the name)?: ')
    name = name +'.pdf'
    print('Where do you want to save the file?:')
    directory_parts = ['Desktop','Downloads','Documents','desktop','downloads','documents']
    directory = input('Choose an Directory:\n1.Desktop\n2.Downloads\n3.Documents\n')
    
    if directory not in directory_parts:
        while directory not in directory_parts:
            print('Choose one of the options!')
            directory = input('Choose an Directory:\n1. Desktop\n2. Downloads\n3. Documents\n')

    with open('/Users/' + username+'/' + directory+'/'+name, 'wb') as f:
        f.write(r.content)
        f.close()
try:      
    r =  open('/Users/' + username+'/' + directory+'/'+name, 'rb')
except OSError:
    print('Error with file!')
    

print('Book is downloaded! Have fun!')
