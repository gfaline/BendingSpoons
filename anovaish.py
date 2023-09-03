import csv
import glob
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats

import statsmodels.api as sm
from statsmodels.formula.api import ols

from bioinfokit.analys import stat

def run_anova_3way_once(file):
    df = pd.read_csv(file, sep=",") #datafile
    # df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['R','A','P','1','2','3'])
    df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['R', 'A', 'P'])
    df_melt.columns = ['index', 'treatments', 'value']

    # fvalue, pvalue = stats.f_oneway(df['R'], df['A'], df['P'],df['1'], df['2'], df['3'])
    fvalue, pvalue = stats.f_oneway(df['R'], df['A'], df['P'])
    print(str(df['R'].mean()) + " & " + str(df['R'].std()) + " & " +
          str(df['A'].mean()) + " & " + str(df['A'].std()) + " & " +
          str(df['P'].mean()) + " & " + str(df['P'].std()) + " & " +
          str(fvalue) + " & " + str(pvalue))

    res = stat()
    res.tukey_hsd(df=df_melt, res_var='value', xfac_var='treatments', anova_model='value ~ C(treatments)')
    print("Anova summary for ", file)
    print(res.anova_summary)
    # print(res.tukey_summary)

    ax = sns.boxplot(x='treatments', y='value', data=df_melt, color='#99c2a2')
    ax = sns.swarmplot(x="treatments", y="value", data=df_melt, color='#7d0013')
    plt.show()
    return {'fvalue': fvalue, 'pvalue': pvalue, 'tukey':res.tukey_summary}
