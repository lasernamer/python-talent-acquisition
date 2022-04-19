import re


email_regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
url_regex = '^(((?!\-))(xn\-\-)?[a-z0-9\-_]{0,61}[a-z0-9]{1,1}\.)*(xn\-\-)' \
            '?([a-z0-9\-]{1,61}|[a-z0-9\-]{1,30})\.[a-z]{2,}$'
url_regex_scheme = '^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)' \
                   '*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$'
ua_phone_regex = '^(380)\d{9}$'


def parse_contacts(raw_data):
    """
    Function expects list with raw contact data. It separates phone numbers, emails and websites in to different lists
    and returns them as ";" split string. Unrecognized data is skipped.
    """
    phones = []
    emails = []
    websites = []
    for data in raw_data:
        if re.search(email_regex, data):
            emails.append(data)
        elif re.search(url_regex, data) or re.search(url_regex_scheme, data):
            websites.append(data)
        else:
            clean_data = re.sub("[^0-9]", "", data)
            if re.search(ua_phone_regex, clean_data):
                phones.append(clean_data)
            else:
                if len(clean_data) >= 9:
                    phones.append('380' + clean_data[-9:])
    return '; '.join(phones), '; '.join(emails), '; '.join(websites)


def parse_dataset(file):
    """
    Function expects CSV file. It reads and parses file and return dataset as list with correct contacts
    at the end of string at each element in the list.
    """
    fixed_dataset = []
    with open(file, 'r', encoding='utf-8') as f:
        for row in f.readlines():
            data_row = [row.replace('\n', '') for row in row.split(sep="\t")]
            contacts_raw = [data for data in data_row[5].replace(' ', '').split(sep=';')]
            for data in parse_contacts(contacts_raw):
                data_row.append(data)
            fixed_dataset.append(data_row)
        print(f'Dataset [read "{f.name}" and fix contacts. {len(fixed_dataset)} rows processed] => Done!')
    return fixed_dataset


def write_dataset(dataset, filename):
    """
    Function expects dataset as list and filename to write new CSV file. It uses TAB (\t) as CSV separator.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for data in dataset:
            f.write('\t'.join(data) + '\n')
        print(f'Dataset [write "{filename}"] => Done!')


if __name__ == '__main__':
    new_dataset = parse_dataset('dataset.csv')
    write_dataset(new_dataset, 'dataset_fixed.csv')
