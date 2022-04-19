import pandas


class NormalisationContacts:

    def __init__(self, dataset_url, save_url):
        """

        :param dataset_url: Путь к dataset файлу
        :param save_url:  Путь к сохранению dataset файла
        """
        self.dataset = dataset_url
        self.save_url = save_url

    @staticmethod
    def validate_numbers(df, column):
        df = df[df[column].str.contains("380").fillna(False)]
        df = df[df[column].str.len() >= 13]
        return df

    @staticmethod
    def validate_emails(df, column):
        df = df[df[column].str.contains("@").fillna(False)]
        return df

    @staticmethod
    def validate_websites(df, column):
        df = df[df[column].str.contains('http') | df[column].str.contains('www') | df[column].str.contains('https')]
        return df

    @staticmethod
    def get_column(df, number):
        return df.columns[number]

    def save_dataset(self, df):
        df.to_csv(self.save_url)

    def parse_dataset(self):
        df = pandas.read_csv(self.dataset, error_bad_lines=False, sep='\t')
        df = df.dropna(how='all')
        df = self.validate_numbers(df, self.get_column(df, 5))
        df = self.validate_emails(df, self.get_column(df, 5))
        df = self.validate_websites(df, self.get_column(df, 5))

        self.save_dataset(df)


d = NormalisationContacts('dataset.csv', "filtered_dataset")
d.parse_dataset()
