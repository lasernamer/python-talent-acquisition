import codecs
import re
from itertools import groupby

f = codecs.open('dataset.csv', 'r', encoding='utf-8')
old_data=f.read().split('\n')
f.close()

pattern_phone = "^(.+|)(380)([0-9]{9})(;|)$"
pattern_email = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|org|edu)"
pattern_website = r"[a-zA-Z0-9]+\.(com|net|org|edu)"

new_data = list()

for line in old_data:
    contact_line=list()
    for i in line.split():
        if '380' in i or '38(0' in i:
            phone_number = re.sub(r'\D', '', i)
            if re.search(pattern_phone,phone_number):
                if len(phone_number)<13:
                    contact_line.insert(0,'Phone: ' + phone_number)

        if "@" in i:
            if re.search(pattern_email, i):
                contact_line.append('E-mail: ' + i)
                break

        if re.search(pattern_website, i):
            contact_line.append('Website: ' + i)


    if contact_line:
        new_data.append(contact_line)

new_data.sort()
new_data = [el for el, _ in groupby(new_data)]

count=0
while count<len(new_data)-1:
    if set(new_data[count]) & set(new_data[count+1]):
        a=set(new_data[count]) | set(new_data[count+1])
        a=list(a)
        new_data[count]=a
        del new_data[count+1]
    count+=1

f = codecs.open('dataset.csv', 'w', encoding='utf-8')

for line in new_data:
    f.write(' '.join(line) + '\n')

f.close()
