import csv
import re

#   This script takes all data from last column of each row from input csv.file  
#   [!]It formating phone numbers into INTERNATIONAL format only if it has >7 numbers 
#       Cause: "275 1267" is a local city number and it cannot be used with +38 in prefix
#   It also takes email addresses and websites, finding them by:
#       Emails: By "@" in string    
#       Websites: By 'www' in string
#   As there was no extra info about the format of result output, all contact info is collected together \
#       in last column. But it is not problem to divide contacts in different columns by "phone"/"email"/"website".
#   Done as test for vacancy.

def format_tel(tel):
    # Method to format the string with mobile number 
    # to correct view
    tel = tel.removeprefix("+")
    tel = tel.removeprefix("38")
    tel = tel.removeprefix("8")
    tel = re.sub("[^0-9]", '', tel)
    if len(tel) <= 4:
        tel = ''
    if len(tel) <= 7:
        tel = f"{tel[:3]} {tel[3:]}"
    else:    
        tel = f"+38 {tel[:3]} {tel[3:6]} {tel[6:]}"
    return tel


def script():
    file_name = 'dataset.csv' 
    file = open(file_name, 'r', encoding='UTF-8')
    csv_file_input = csv.reader(file) #Read Data

    file = open('result_csv.csv', 'w') #Creating new file for results
    file.close
    
    with open(file_name, 'r', encoding='utf-8') as f:
        row_number = sum(1 for line in f) #Taking the number of rows in file:
        
    for index, i in enumerate(csv_file_input):
        if index % 2000 == 0: #Some kind of logs 
            print(f'Proccesing row: {index} of {row_number} ')
            
        # Init empty vars
        temp_emails = []
        temp_phones = []
        temp_webs = []
        # Process Data
        row_data = i[0].split('\t')[-1:] #Here taking data only from last cell
        contact_data = row_data[0].split('; ') #Dividing data by ";" to iterate it 
        
        for elem in contact_data: 
            if len(contact_data) == 1:  #if only 1 contact in row
                if '@' in elem:
                    #Searching emails in list
                    temp_emails.append(elem)
                elif 'www' in elem:
                    #Searching web-sites in list
                    temp_webs.append(elem)
                for num in range(-1,10):
                    #Searching phones in list
                    if str(num) in elem:
                        temp_phones.append(format_tel(elem))
                        break
                card = {
                    'emails': '; '.join(temp_emails),
                    'webs': '; '.join(temp_webs),
                    'phones': '; '.join(temp_phones)
                }
            else: #if more than 1 contact in row
                if '@' in elem and elem not in temp_emails: 
                    #Searching emails in list
                    temp_emails.append(elem)
                elif 'www' in elem and elem not in temp_webs:
                    #Searching web-sites in list
                    temp_webs.append(elem)
                for num in range(-1,10):
                    #Searching phones in list
                    if str(num) in elem and format_tel(elem) not in temp_phones and '@' not in elem:
                        temp_phones.append(format_tel(elem))
                card = {
                    'emails': '; '.join(temp_emails),
                    'webs': '; '.join(temp_webs),
                    'phones': '; '.join(temp_phones)
                }
                
        with open("result_csv.csv", 'a', encoding='utf-8') as csv_file_output:
            #Writing new file with normalized contact data
            file_writer = csv.writer(csv_file_output)
            
            #Joining all vars into 1 list to have a column-based view in csv
            new_i = i[0].split('\t')
            content = [i_3 for i_3 in new_i][:-1]
            results = [card['phones'], card['emails'], card['webs']]
            results = ', '.join(results)
            content.append(results)
            file_writer.writerow(content)   
    print(f'Proccesing row: {index} of {row_number}\nFinished!')
    
def main():
    script()
    
if __name__ == "__main__":
    main()