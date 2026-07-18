"""
tables.py

Functions for creating publication-ready baseline characteristic tables.
"""

import pandas as pd
import numpy as np
from scipy import stats


def _mean_sd(series):
    """Return Mean ± SD."""
    return f"{series.mean():.1f} ± {series.std():.1f}"


def _anova_pvalue(data, variable, group):
    """
    Welch ANOVA approximation using scipy one-way ANOVA.
    (Can later be upgraded to Welch ANOVA.)
    """

    groups = [
        g[variable].dropna().values
        for _, g in data.groupby(group)
    ]

    if len(groups) < 2:
        return np.nan

    stat, p = stats.f_oneway(*groups)

    return p


def _ttest_pvalue(data, variable, group):
    """
    Independent t-test for two groups.
    """

    groups = [
        g[variable].dropna().values
        for _, g in data.groupby(group)
    ]

    if len(groups) != 2:
        return np.nan

    stat, p = stats.ttest_ind(
        groups[0],
        groups[1],
        equal_var=False
    )

    return p


def create_baseline_table(
    data,
    group,
    continuous,
    test="anova"
):
    """
    Create baseline descriptive table for continuous variables.

    Parameters
    ----------
    data : pandas.DataFrame

    group : str
        Grouping variable.

    continuous : list
        List of continuous variables.

    test : str
        "anova" or "ttest"

    Returns
    -------
    pandas.DataFrame
    """

    table = []

    group_levels = data[group].dropna().unique()

    for variable in continuous:

        row = {
            "Variable": variable,
            "Overall": _mean_sd(data[variable])
        }

        for level in group_levels:

            row[str(level)] = _mean_sd(
                data.loc[data[group] == level, variable]
            )

        if test == "anova":
            p = _anova_pvalue(data, variable, group)

        elif test == "ttest":
            p = _ttest_pvalue(data, variable, group)

        else:
            p = np.nan

        row["P-value"] = (
            f"{p:.3f}" if pd.notnull(p) else ""
        )

        table.append(row)

    return pd.DataFrame(table)


import pandas as pd
import numpy as np

from scipy import stats


def create_phase_angle_summary(
    data,
    group,
    by_variables,
    outcome="phase_angle"
):
    """
    Create a summary table of phase angle across categorical variables.

    Parameters
    ----------
    data : pandas.DataFrame
    group : str
        Column used for grouping (e.g. cohort1_label or bmi_group)
    by_variables : list
        Categorical variables to summarize
    outcome : str
        Continuous outcome variable (default = phase_angle)

    Returns
    -------
    pandas.DataFrame
    """

    tables = []

    for variable in by_variables:

        rows = []

        for level in sorted(data[variable].dropna().unique()):

            subset = data[data[variable] == level]

            row = {
                variable: level
            }

            # Overall
            row["Overall"] = (
                f"{subset[outcome].mean():.2f} "
                f"({subset[outcome].std():.2f})"
            )

            # Each study group
            for g in data[group].dropna().unique():

                values = subset.loc[
                    subset[group] == g,
                    outcome
                ]

                row[g] = (
                    f"{values.mean():.2f} "
                    f"({values.std():.2f})"
                    if len(values) > 0
                    else ""
                )

            # p-value
            groups = [
                subset.loc[
                    subset[group] == g,
                    outcome
                ].dropna()
                for g in data[group].dropna().unique()
            ]

            groups = [g for g in groups if len(g) > 0]

            if len(groups) >= 2:

                row["P-value"] = round(
                    stats.f_oneway(*groups).pvalue,
                    3
                )

            else:

                row["P-value"] = np.nan

            rows.append(row)

        table = pd.DataFrame(rows)

        table.insert(
            0,
            "Variable",
            variable
        )

        tables.append(table)

    return pd.concat(
        tables,
        ignore_index=True
    )