import unittest
from pathlib import Path
from dataset_processor import parse_dataset


class TestDatasetProcessor(unittest.TestCase):
    test_file = Path(__file__).resolve().parent / 'test_dataset.csv'
    parsed_data_cases = [['"зареєстровано', '27.08.2009; 27.08.2009; 10741020000034427', '36594071',
                          'ГРОМАДСЬКА ОРГАНІЗАЦІЯ', '""TEST""""TEST""""""',
                          '+380442386677;3,80443332211;3,8044332211;test@mail.com;test.com; test2@mail.net',
                          '380442386677; 380443332211; 380044332211',
                          'test@mail.com; test2@mail.net',
                          'test.com'],
                         ['"зареєстровано', '24.01.2008; 24.01.2008; 14151020000019225', '35664472',
                          'ГРОМАДСЬКА ОРГАНІЗАЦІЯ', '""ГРОМАДСЬКА ОРГАНІЗАЦІЯ """"ТВОРЧА МАЙСТЕРНЯ """"ШТУКА""""""',
                          '80504300606"; info@shtuka.lviv.ua; www.shtuka.lviv.ua; i.ua',
                          '380504300606',
                          'info@shtuka.lviv.ua',
                          'www.shtuka.lviv.ua; i.ua'],
                         ['"припинено', '27.01.2011; 05.02.2011; 11451200000002171', '37466855',
                          'ГРОМАДСЬКА ОРГАНІЗАЦІЯ',
                          '""ФЕОДОСІЙСЬКЕ ГРОМАДСЬКЕ ФОРМУВАННЯ З ОХОРОНИ ГРОМАДСЬКОГО ПОРЯДКУ І '
                          'ДЕРЖАВНОГО КОРДОНУ """"ДОЗОР""""""',
                          '0504981107"; 5 75 20;',
                          '380504981107',
                          '',
                          '']]

    def test_parsed_data(self):
        new_dataset = parse_dataset(self.test_file)
        for case in new_dataset:
            self.assertEqual(case, self.parsed_data_cases[new_dataset.index(case)])


if __name__ == '__main__':
    unittest.main()
