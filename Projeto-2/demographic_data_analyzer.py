import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    sex_count = df['sex'].value_counts()
    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country_percentage = round((country_salary / country_total * 100).max(), 1)
    highest_earning_country = (country_salary / country_total * 100).idxmax()

    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].mode()[0]

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

    return result


# 🚀 Só executa se rodar "python main.py"
if __name__ == "__main__":
    result = calculate_demographic_data()

    print("Número de homens e mulheres:\n", result['sex_count'])
    print("Número de pessoas por raça:\n", result['race_count'])
    print("Idade média dos homens:", result['average_age_men'])
    print("Porcentagem de pessoas com bacharelado:", result['percentage_bachelors'])
    print("Porcentagem com educação avançada ganhando >50K:", result['higher_education_rich'])
    print("Porcentagem sem educação avançada ganhando >50K:", result['lower_education_rich'])
    print("Número mínimo de horas trabalhadas por semana:", result['min_work_hours'])
    print("Porcentagem de pessoas trabalhando mínimo de horas ganhando >50K:", result['rich_percentage_min_workers'])
    print("País com maior porcentagem de >50K:", result['highest_earning_country'])
    print("Porcentagem no país:", result['highest_earning_country_percentage'])
    print("Ocupação mais popular para >50K na Índia:", result['top_IN_occupation'])
