from statistics import *


if __name__ == '__main__':
    # create sample data according to survey
    data = [['18-29', 'Conservative'] for i in range(141)] + \
           [['18-29', 'Socialist'] for i in range(68)] + \
           [['18-29', 'Other'] for i in range(4)] + \
           [['30-44', 'Conservative'] for i in range(179)] + \
           [['30-44', 'Socialist'] for i in range(159)] + \
           [['30-44', 'Other'] for i in range(7)] + \
           [['45-65', 'Conservative'] for i in range(220)] + \
           [['45-65', 'Socialist'] for i in range(216)] + \
           [['45-65', 'Other'] for i in range(4)] + \
           [['65 & older', 'Conservative'] for i in range(86)] + \
           [['65 & older', 'Socialist'] for i in range(101)] + \
           [['65 & older', 'Other'] for i in range(4)]
    df = pd.DataFrame(data, columns=['Age Group', 'Political Affiliation'])
    variable1, variable2 = df['Age Group'], df['Political Affiliation']

    alpha = 0.05
    chi_square = calculate_chi_square(variable1, variable2)

    # The p-value approach
    p_value = calculate_p_value(variable1, variable2, chi_square)
    conclusion = "Failed to reject the null hypothesis."
    if p_value <= alpha:
        conclusion = "Null Hypothesis is rejected."

    print("chisquare-score is:", chi_square, " and p value is:", p_value)
    print(conclusion)

    # The critical value approach
    print("\n--------------------------------------------------------------------------------------")
    print("Approach 2: The critical value approach to hypothesis testing in the decision rule")
    critical_value = calculate_critical_value(variable1, variable2, alpha)
    conclusion = "Failed to reject the null hypothesis."
    if chi_square > critical_value:
        conclusion = "Null Hypothesis is rejected."

    print("chisquare-score is:", chi_square, " and p value is:", critical_value)
    print(conclusion)
