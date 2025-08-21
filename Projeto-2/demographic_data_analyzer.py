import pandas as pd

def calculate_demographic_data(print_data=True):
   
    df = pd.read_csv("adult.data.csv")

    # 1. Quantos homens e mulheres tem no dataset?
    sex_count = df['sex'].value_counts()

    # 2. Quantidade de pessoas por raça
    race_count = df['race'].value_counts()

    # 3. Idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 4. Porcentagem de pessoas com diploma de bacharel
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 5. Porcentagem de pessoas com educação avançada que ganham >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. Porcentagem de pessoas sem educação avançada que ganham >50K
    lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 7. Número mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 8. Porcentagem de pessoas que trabalham o mínimo de horas e ganham >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 9. País com maior porcentagem de pessoas que ganham >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country_percentage = round((country_salary / country_total * 100).max(), 1)
    highest_earning_country = (country_salary / country_total * 100).idxmax()

    # 10. Ocupação mais popular para pessoas que ganham >50K na Índia
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].mode()[0]

    # Montamos o dicionário de resultados
    result = {
        'sex_count': sex_count,
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    if print_data:
        print("Número de homens e mulheres:\n", sex_count)
        print("Número de pessoas por raça:\n", race_count)
        print("Idade média dos homens:", average_age_men)
        print("Porcentagem de pessoas com bacharelado:", percentage_bachelors)
        print("Porcentagem com educação avançada ganhando >50K:", higher_education_rich)
        print("Porcentagem sem educação avançada ganhando >50K:", lower_education_rich)
        print("Número mínimo de horas trabalhadas por semana:", min_work_hours)
        print("Porcentagem de pessoas trabalhando mínimo de horas ganhando >50K:", rich_percentage_min_workers)
        print("País com maior porcentagem de >50K:", highest_earning_country)
        print("Porcentagem no país:", highest_earning_country_percentage)
        print("Ocupação mais popular para >50K na Índia:", top_IN_occupation)

    return result
