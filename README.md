# Python Developer Assessment

Hi!

- Fork this repo
- Examine csv file
- Create python script for normalization contacts
- Perform changes to file and spit concats by fields: phone number (digits only, begin from 380); email address; website
- Push fixed csv and your code
- Create pull request to this repo in dedicated branch
- There is all. Show your skill :)

_______________________________________

Script dataset_processor.py reads and parses CSV file. It looks for raw contact data in Column6 and separates 
phone numbers, emails and websites in to new different columns 
and returns them as ";" split string. Unrecognized data is skipped. 
It writes new CSV file and uses TAB (\t) as CSV separator.
####How to run:
* python dataset_processor.py
####Simple test also available:
* python -m unittest .\tests\test_dataset_processor.py
### Created by: roman-zahoruiko (3x1gex@gmail.com)

