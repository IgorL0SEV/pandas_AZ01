import pandas as pd

df = pd.read_csv('dz.csv')

salary_by_sity = df.groupby('City')['Salary'].mean()

print (f"Средняя зарплата по городам : {salary_by_sity} .")

