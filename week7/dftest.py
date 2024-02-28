import pandas as pd 
import numpy as np 


user_data = {'Jadon': [99, 98, 100], 'Bob': [100, 96, 99], 'Alex': [100, 100, 99], 'Randy': [67, 77, 70]}
y_axis_labels = ['Microscopic Diode Exam', 'DataFrame Matrix Manipulation Exam', 'Linear Algebra for Quantum Mechanics Exam']


df = pd.DataFrame(user_data, index=y_axis_labels)
print(df)


test_score_df = pd.DataFrame(user_data,
                          columns=y_axis_labels)

def rain_condition(v):
    if v < 1.75:
        return "Dry"
    elif v < 2.75:
        return "Rain"
    return "Heavy Rain"

def make_pretty(styler):
    styler.set_caption("Weather Conditions")
    styler.format(rain_condition)
    styler.format_index(lambda v: v.strftime("%A"))
    styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="YlGnBu")
    return styler

def style_test_scores(styler):
    styler.set_caption("Test Scores")
    styler.background_gradient(cmaps='Blues')
    return styler



print(test_score_df)


# print(test_score_df.loc["2021-01-04":"2021-01-08"].style.pipe(make_pretty))
