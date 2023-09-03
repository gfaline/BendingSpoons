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


def lol_plt():
    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 22})

    materials = ['Reactive', 'Active', 'Proactive']
    x_pos = np.arange(len(materials))
    CTEs = [21.43, 25.31, 36.02]
    error = [3.12, 3.97, 4.33]

    fig, ax = plt.subplots()
    ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel("% of Tubes Repaired")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(materials)
    # ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
    ax.yaxis.grid(True)

    # Save the figure and show
    plt.tight_layout()
    plt.savefig('percentage_tubes_fixed.png')
    # plt.show()

    materials = ['Reactive', 'Active', 'Proactive']
    x_pos = np.arange(len(materials))
    CTEs = [183.11, 177.68, 161.83]
    error = [2.88, 4.019, 6.038]

    fig, ax = plt.subplots()
    ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel("Task Efficiency (sec)")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(materials)
    # ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
    ax.yaxis.grid(True)
    plt.ylim([100, 200])

    # Save the figure and show
    plt.tight_layout()
    plt.savefig('tube_efficiency.png')
    # plt.show()

#lol_plt()
# print("Performance")
# performance_32 = run_anova_3way_once('32_performance_updated_rover4.csv')
# # print("Performance cut fvalue: ", performance_32['fvalue'], " pvalue: ", performance_32['pvalue'])
# print(performance_32['tukey'])
#
# print("Tubes Fixed")
# perfect_fixed_32 = run_anova_3way_once('32_percent_tubes_fixed.csv')
# # print("Percent fixed fvalue: ", perfect_fixed_32['fvalue'], " pvalue: ", perfect_fixed_32['pvalue'])
# print(perfect_fixed_32['tukey'])

print("Lag")
#lag_32 = run_anova_3way_once('lag_1.csv')
lag_32 = run_anova_3way_once('lag_trial_order.csv')
# print("Percent fixed fvalue: ", perfect_fixed_32['fvalue'], " pvalue: ", perfect_fixed_32['pvalue'])
print(lag_32['tukey'])
#
# print("Correct Rover")
# rover_32_take3 = run_anova_3way_once('32_rover_events_correct_take5.csv')

# print("Recovery")
# recovery_32 = run_anova_3way_once('32_recovery_non_0.csv')
# # print("take 3 rover events fvalue: ", rover_32_take3['fvalue'], " pvalue: ", rover_32_take3['pvalue'])
# #print(rover_32_take3['tukey'])
#
#

# print("Repair time")
# repair_time_32 = run_anova_3way_once('32_repair_time.csv')
# print(repair_time_32['tukey'])
#
# print("Final station health")
# ending_health_all = run_anova_3way_once('32_ending_health.csv')
# print(ending_health_all['tukey'])


"""In paper, done unless I edit again"""
"""



print("Correct answers")
correct_answers_all = run_anova_3way_once('32_correct_answers.csv')

print("TWLQ: Team Workload")
workload_avg_32 = run_anova_3way_once("workload_avg_answers.csv")
# print(workload_avg_32['tukey'])

print ("SART: Situational Awareness")
situational_awareness_32 = run_anova_3way_once("situational_awareness_avg_answers.csv")
# print(situational_awareness_32['tukey'])

print("NASA-TLX: Workload")
TLX_avg_32 = run_anova_3way_once("TLX_avg_answers.csv")
# print(TLX_avg_32['tukey'])

perceived_performance_all = run_anova_3way_once('32_perceived_performance.csv')
print("perceived_performance fvalue: ", perceived_performance_all['fvalue'],
  " pvalue: ", perceived_performance_all['pvalue'])

print("Lowest station health")
lowest_health_all = run_anova_3way_once('32_lowest_health.csv')
print(lowest_health_all['tukey'])

ending_health_all = run_anova_3way_once('32_ending_health.csv')

difficulty_all = run_anova_3way_once('32_difficulty.csv')
correct_answers_all = run_anova_3way_once('32_correct_answers.csv')

print("ending_health fvalue: ", ending_health_all['fvalue'], " pvalue: ", ending_health_all['pvalue'])

print("difficulty fvalue: ", difficulty_all['fvalue'], " pvalue: ", difficulty_all['pvalue'])
print("correct_answers fvalue: ", correct_answers_all['fvalue'], " pvalue: ", correct_answers_all['pvalue'])

repair_time_32 = run_anova_3way_once('32_repair_time.csv')
print("repair time for tubes fvalue: ", repair_time_32['fvalue'], " pvalue: ", repair_time_32['pvalue'])
print(repair_time_32['tukey'])

rover_response_time_32 = run_anova_3way_once('32_avg_rover_response_time.csv')
print("rover_response_time fvalue: ", rover_response_time_32['fvalue'], " pvalue: ", rover_response_time_32['pvalue'])
print(rover_response_time_32['tukey'])

situational_awareness_32 = run_anova_3way_once("situational_awareness_avg_answers.csv")
print("situational_awareness fvalue: ", situational_awareness_32['fvalue'], " pvalue: ", situational_awareness_32['pvalue'])
print(situational_awareness_32['tukey'])

TLX_avg_32 = run_anova_3way_once("TLX_avg_answers.csv")
print("TLX_avg fvalue: ", TLX_avg_32['fvalue'], " pvalue: ", TLX_avg_32['pvalue'])
print(TLX_avg_32['tukey'])

workload_avg_32 = run_anova_3way_once("workload_avg_answers.csv")
print("workload_avg_answers fvalue: ", workload_avg_32['fvalue'], " pvalue: ", workload_avg_32['pvalue'])
print(workload_avg_32['tukey'])

"""
