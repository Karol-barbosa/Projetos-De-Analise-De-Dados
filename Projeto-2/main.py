from demographic_data_analyzer import calculate_demographic_data

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
