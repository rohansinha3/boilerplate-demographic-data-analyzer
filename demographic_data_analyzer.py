import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    l=[]
    l= df['race'].value_counts()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(l)

    # What is the average age of men?
    avg_age_df= df.loc[(df['age']>df['age'].mean()) & (df['sex']== 'Male')]
    average_age_men = avg_age_df['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachlor= len(df.loc[df['education']=='Bachelors'])
    percentage_bachelors = (bachlor/len(df)) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    higher_education = len(df.loc[(df['education']== 'Bachelors') | (df['education']== 'Masters') | (df['education']== 'Doctorate') & (df['salary'] == '>50K')])

    lower_education = len(df.loc[(df['education']!= 'Bachelors') & (df['education']!= 'Masters') & (df['education']!= 'Doctorate') & (df['salary'] == '>50K')])


    # percentage with salary >50K
    higher_education_rich = (higher_education/len(df)) * 100
    lower_education_rich = (lower_education/len(df)) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(min_work_hours)

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    high_salary_df= df.loc[(df['salary']== '>50K')]
    total_per_country= df['native-country'].value_counts()
    high_salary_per_country= high_salary_df['native-country'].value_counts()
    perc_high_sal= (high_salary_per_country/total_per_country) * 100
    per_high_sal_country= perc_high_sal.idxmax()
    perc= perc_high_sal.max()
    highest_earning_country = per_high_sal_country
    highest_earning_country_percentage = perc

    # Identify the most popular occupation for those who earn >50K in India.
    occ= df.loc[(df['salary']== '>50K') & (df['native-country']== 'India')]
    top_IN_occupation = occ['occupation'].value_counts().idxmax()

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
