from flask import Flask, render_template, request, url_for
import pandas as pd
import numpy as np
import math

def update_scores(df2, results):
    for index, row in df2.iterrows():
        count = 0
        for k in range(len(row.index)):

            if row.index[k] == "score":
                break
            if type(row.values[k]) == str and type(results.values[k]) == str:

                if row.values[k].lower() == results.values[k].lower():
                    count += 1
            else:
                if row.values[k] == results.values[k]:
                    count += 1

        df2["score"][index] = count

    return df2

def get_leader(df2):
    max_score = df2.shape[1]
    for i in range(max_score, 0, -1):
        if i in df2["score"].values:
            subdf = df2[df2["score"] == i]
            current_leader = subdf["Name"].values
            return current_leader

def get_scores_sorted(df2):
    sorted_scores = df2[["Name","score"]].sort_values(by=['score'], ascending=False)
    return sorted_scores.values

def update_results(results, item_to_update, value):
    if item_to_update == "" and value == "":
        return results
    results[item_to_update] = value
    return results

app = Flask(__name__)
df = pd.read_excel("Chiefsvs49ers.xlsx")
df = df.dropna(subset=['Name'])
df2 = df.append(pd.Series(name="results"))
score = [0] * len(df2)
df2["score"] = score
scores = df2.loc["results"]




@app.route('/', methods=["GET", "POST"])
def hello():
    selected_value = ""
    result = ""
    data = df2
    results = scores
    #results = results.drop(['score', 'Paid'])
    keys = results.keys()
    selected_value = request.form.get('bets')
    result = request.form.get('result')
    print(selected_value)
    print(result)
    results = update_results(results, selected_value, result)
    data = update_scores(data, results)
    leaders = get_scores_sorted(data)
    keys = keys[0:len(keys)-2]
    results = results.values[0:len(results.values)-2]
    bet_results = zip(keys, results)
    return render_template('index.html', users = keys, leaders=leaders, results = bet_results)
