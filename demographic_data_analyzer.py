import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('adult.data.csv')

df.replace('?',np.NaN,inplace=True)
df.dropna(axis=0,inplace=True)
df.isnull().sum()

df.reset_index(inplace=True)

# Q1
print(df.race.value_counts())

# Q2
print(df.iloc[np.where(df.sex == 'Male')].age.mean())

# Q3
print(len(df.iloc[np.where(df.education == 'Bachelors')])/len(df)*100)

# Q4
masters = np.where(df.education == 'Masters')[0]
bachelors = np.where(df.education == 'Bachelors')[0]
doctorate = np.where(df.education == 'Doctorate')[0]
high_education = df.iloc[np.array(list((set(masters).union(set(bachelors))).union(set(doctorate))))]
print(len(high_education.iloc[np.where(high_education['salary'] == '>50K')])/len(df)*100)

# Q5
low_education = df.iloc[np.setdiff1d(df.index,high_education.index)]
print(len(low_education.iloc[np.where(low_education['salary'] == '<=50K')])/len(df)*100)

# Q6
print(df['hours-per-week'].min())

# Q7
min_hours = df.iloc[np.where(df['hours-per-week'] == 1)]
salary_more = min_hours.iloc[np.where(min_hours['salary']=='>50K')]
salary_less = min_hours.iloc[np.where(min_hours['salary']=='<=50K')]
print(len(salary_more)/len(min_hours)*100)

# Q8
def high_wage(country):
    cont = df.iloc[np.where(df['native-country'] == country)]
    high_sal = cont.iloc[np.where(cont['salary'] == '>50K')]
    per =  len(high_sal)/len(cont)*100
    return per

dic = {}
for i in df['native-country'].unique():
    x = high_wage(i)
    dic.update({
        i:x
    })
    
max_country = max(dic,key=dic.get)
max_salary_percent = dic[max(dic,key=dic.get)]
print('Country with max number of employees get salary >50K & minimum hours of work is:\n',max_country)
print('percentage:',max_salary_percent)

# Q9
def cont_sal(country,sal):
    cont = df.iloc[np.where(df['native-country'] == country)]
    high_sal = cont.iloc[np.where(cont['salary'] == sal)]
    per =  len(high_sal)/len(cont)*100
    return high_sal
print(cont_sal('India','>50K')['occupation'].value_counts().sort_values(ascending=False).index[0])

