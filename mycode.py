import csv 
import re

intermediate_list=list()

regex_email =re.compile( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
regex_number =re.compile( r'(\+380)')
regex_website =re.compile( r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})')

#encoding="utf8" because Python 3 opens your files with a default encoding that doesn't match the contents. 
def fix():
    """
    change_data_set.csv - Includes all lines containing phone number or email or website
    change_data_set2.csv - Includes all lines containing phone number, email and website
    """

    with open('dataset.csv',encoding="utf8") as f:
        contents=csv.reader(f)
        for row in contents:
            for elem in row:
                if regex_number.search(elem) or regex_email.search(elem) or regex_website.search(elem):
                    intermediate_list.append(row)


    with open('change_data_set.csv','w',newline='',encoding="utf8") as f:
        writer=csv.writer(f)
        writer.writerows(intermediate_list)

if __name__ == "__main__":
    print(fix.__doc__)
    fix()




        






