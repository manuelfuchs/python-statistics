import pandas as pd
import scipy.stats as stats


# based on https://towardsdatascience.com/chi-square-test-with-python-d8ba98117626
def calculate_chi_square(variable1: pd.Series, variable2: pd.Series) -> int:
    contingency_table = pd.crosstab(variable1, variable2, margins=True, margins_name="Total")

    chi_square = 0
    rows = variable1.unique()
    columns = variable2.unique()
    for i in columns:
        for j in rows:
            observed = contingency_table[i][j]
            expected = contingency_table[i]['Total'] * contingency_table['Total'][j] / contingency_table['Total']['Total']
            chi_square += (observed - expected) ** 2 / expected

    return chi_square


def calculate_p_value(variable1: pd.Series, variable2: pd.Series, chi_square: float) -> float:
    rows = variable1.unique()
    columns = variable2.unique()
    return 1 - stats.norm.cdf(chi_square, (len(rows) - 1) * (len(columns) - 1))


def calculate_critical_value(variable1: pd.Series, variable2: pd.Series, alpha: float) -> float:
    rows = variable1.unique()
    columns = variable2.unique()
    return stats.chi2.ppf(1 - alpha, (len(rows) - 1) * (len(columns) - 1))
