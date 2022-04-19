import csv
import re


if __name__ == "__main__":
    data = []

    with open("dataset.csv", encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')

        phone_re = "^(.+|)(380)([0-9]{9})(;|)$"
        email_re = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|org|edu)"
        website_re = r"[a-zA-Z0-9]+\.(com|net|org|edu)"

        for row in csv_reader:
            contact_line = []

            for line in row:
                if '380' in line or '38(0' in line:
                    # phone_number = re.sub(r'\D', '', i)
                    phone = re.search(phone_re, line)
                    if phone:
                        if len(line) < 13:
                            contact_line.insert(0, 'Phone: ' + phone.group(0))

                if "@" in line:
                    email = re.search(email_re, line)
                    if email:
                        contact_line.append('E-mail: ' + email.group(0))
                        break

                website = re.search(website_re, line)
                if website:
                    contact_line.append('Website: ' + website.group(0))

            if contact_line:
                data.append(contact_line)

    with open('new_dataset.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for contact in data:
            writer.writerow(contact)

    print("Done")
