import pandas as pd
import numpy as np
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round(df.iloc[np.where(df.sex == 'Male')].age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df.iloc[np.where(df.education == 'Bachelors')])/len(df)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    masters = np.where(df.education == 'Masters')[0]
    bachelors = np.where(df.education == 'Bachelors')[0]
    doctorate = np.where(df.education == 'Doctorate')[0]
  
    high_education = df.iloc[np.array(list((set(masters).union(set(bachelors))).union(set(doctorate))))]
    higher_education_rich = round(len(high_education.iloc[np.where(high_education['salary'] == '>50K')])/len(df)*100,1)
    low_education = df.iloc[np.setdiff1d(df.index,high_education.index)]
    lower_education_rich = round(len(low_education.iloc[np.where(low_education['salary'] == '<=50K')])/len(df)*100,1)
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = df.iloc[np.where(df['hours-per-week'] == 1)]
    salary_more = min_hours.iloc[np.where(min_hours['salary']=='>50K')]
    salary_less = min_hours.iloc[np.where(min_hours['salary']=='<=50K')]
    rich_percentage = round(len(salary_more)/len(min_hours)*100,1)

    # What country has the highest percentage of people that earn >50K?
    def high_wage(country):
      cont = df.iloc[np.where(df['native-country'] == country)]
      high_sal = cont.iloc[np.where(cont['salary'] == '>50K')]
      per =  len(high_sal)/len(cont)*100
      return per
    dic = {}
    for i in df['native-country'].unique():
      x = high_wage(i)
      dic.update({i:x})
    
    highest_earning_country = max(dic,key=dic.get)
    highest_earning_country_percentage = round(dic[max(dic,key=dic.get)],1)
 
    # Identify the most popular occupation for those who earn >50K in India.
    def cont_sal(country,sal):
      cont = df.iloc[np.where(df['native-country'] == country)]
      high_sal = cont.iloc[np.where(cont['salary'] == sal)]
      per =  len(high_sal)/len(cont)*100
      return high_sal
    
    top_IN_occupation = cont_sal('India','>50K')['occupation'].value_counts().sort_values(ascending=False).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
