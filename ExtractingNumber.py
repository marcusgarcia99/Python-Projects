import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

with open('extracted_content/Instructions.txt') as f:
    content = print(f.read())

import re
import os

pattern = r'\d{3}-\d{3}-\d{4}'

test_string = 'Here is a phone number 123-123-1234'

re.findall(pattern,test_string)

def search(file,pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ""

os.getcwd()+'/extracted_content'

results = []
for folders, subfolders, files in os.walk(os.getcwd()+'/extracted_content'):
    for f in files:
        full_path = folders + '/'+f
        
        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())

