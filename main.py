import pandas as pd


file = pd.read_csv('dataset.csv', sep = '\t', encoding='utf-8', usecols=[*range(5, 6)])


file = file.replace(to_replace = '\+', value = '', regex=True)
file = file.replace(to_replace = '\(', value = '', regex=True)
file = file.replace(to_replace = '\)', value = '', regex=True)
file = file.replace(to_replace = '\-', value = '', regex=True)
file.to_csv('final.csv',sep = '\t',encoding = 'utf-8', index=False)
print(file)


