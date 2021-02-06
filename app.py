from flask import Flask, render_template, request, url_for
import pandas as pd
import numpy as np



data = [
['Gabe', 'Over', 'Over', 'Shanahan', 'Under', 'Yes', 'Heads', '49ers', 'Pass', 'TD', 'Williams', 'Samuel', 'Chiefs', 'Chiefs', 'Gould', 'Mahomes', 'Chiefs', 'Garropolo', 'Mathieu', 'No', 'Yes', 'Hill', 'Mostert', 'Over', 'Under', 'Under', 'Under', 'Bosa', 'Samuel', 'Under', 'Over', 'Yes', 'Chiefs', 'Chiefs', 'Chiefs', 'Garropolo', 'Under', 'Clear', 'If you had my love', 'Teammates', '49ers 28 - 24 ', 'Yes'],
['Daniel Bleiwas', 'Over', 'Over', 'Andy Reid', 'Under', 'Yes', 'Heads', '49ers', 'Run', 'TD', 'Kittle', 'Mostert', '49ers', '49ers', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Bosa', 'No', 'No', 'Hill', 'Mostert', 'Over', 'Under', 'Under', 'Under', 'Bosa', 'Kittle', 'Under', 'Over', 'Yes', '49ers', 'Chiefs', 'Chiefs', 'Garropolo', 'Under', 'Red', 'On the floor', 'Teammates', '49ers 28 - 27', 'Yes'],
['Rafa', 'Under', 'Over', 'Andy Reid', 'Over', 'Yes', 'Heads', '49ers', 'Run', 'TD', 'Mostert', 'Kelce', '49ers', 'Chiefs', 'Gould', 'Mahomes', '49ers', 'Mahomes', 'Buckner', 'No', 'Yes', 'Kelce', 'Mostert', 'Under', 'Over', 'Under', 'Over', 'Buckner', 'Samuel', 'Under', 'Over', 'Yes', '49ers', '49ers', '49ers', 'Mahomes', 'Over', 'Yellow', "Let's Get Loud", 'God', 'Chiefs 34 - 30', 'Yes'],
['Adam Sabba', 'Over', 'Under', 'Shanahan', 'Over', 'No', 'Tails', 'Chiefs', 'Run', 'TD', 'Hill', 'Williams', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Chiefs', 'Garropolo', 'Fuller', 'No', 'No', 'Hill', 'Williams', 'Under', 'Over', 'Over', 'Under', 'Jones', 'Watkins', 'Under', 'Under', 'No', 'Chiefs', '49ers', '49ers', 'Mahomes', 'Over', 'Blue', 'On the floor', 'God', 'Chiefs 42 - 35', 'Yes'],
['Middle', 'Under', 'Over', 'Andy Reid', 'Under', 'Yes', 'Tails', '49ers', 'Pass', 'FG', 'Williams', 'Kittle', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Chiefs', 'Garropolo', 'Sorenson', 'No', 'No', 'Sanders', 'Mostert', 'Over', 'Under', 'Over', 'Under', 'Buckner', 'Hill', 'Under', 'Over', 'Yes', 'Chiefs', '49ers', 'Chiefs', 'Mahomes', 'Over', 'Red', "Hips don't lie", 'Teammates', 'Chiefs 25 - 20', 'Yes'],
['Shuman', 'Under', 'Over', 'Andy Reid', 'Over', 'No', 'Heads', 'Chiefs', 'Pass', 'TD', 'Samuel', 'Williams', '49ers', 'Chiefs', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Moseley', 'No', 'No', 'Samuel', 'Mostert', 'Under', 'Under', 'Under', 'Under', 'Armstead', 'Sanders', 'Under', 'Over', 'No', '49ers', 'Chiefs', '49ers', 'Garropolo', 'Under', 'Orange', 'Get Right', 'Teammates', '49ers 30 - 24', 'Yes'],
['Rasko the Clown', 'Over', 'Over', 'Andy Reid', 'Over', 'No', 'Tails', 'Chiefs', 'Run', 'TD', 'Mahomes', 'Kittle', 'Chiefs', '49ers', 'Gould', 'Mahomes', 'Chiefs', 'Garropolo', 'Mathieu', 'No', 'No', 'Watkins', 'Mostert', 'Over', 'Under', 'Under', 'Under', 'Clark', 'Kelce', 'Under', 'Over', 'Yes', 'Chiefs', '49ers', '49ers', 'Mahomes', 'Over', 'Purple', 'Get Right', 'Teammates', 'Chiefs 33 - 26', 'Yes'],
['Zucker', 'Over', 'Under', 'Andy Reid', 'Over', 'No', 'Tails', 'Chiefs', 'Pass', 'TD', 'Hill', 'Kelce', 'Chiefs', '49ers', 'Gould', 'Mahomes', 'Chiefs', 'Garropolo', 'Breeland', 'No', 'No', 'Hill', 'Mostert', 'Over', 'Under', 'Under', 'Over', 'Buckner', 'Watkins', 'Over', 'Over', 'Yes', 'Chiefs', '49ers', '49ers', 'Mahomes', 'Under', 'Yellow', 'Get Right', 'Teammates', 'Chiefs 28 - 20', 'Yes'],
['Max Ashley', 'Over', 'Over', 'Andy Reid', 'Over', 'No', 'Heads', 'Chiefs', 'Pass', 'TD', 'Mostert', 'Mostert', '49ers', '49ers', 'Gould', 'Mahomes', 'Chiefs', 'Garropolo', 'Ford', 'No', 'No', 'Kelce', 'Mostert', 'Under', 'Under', 'Under', 'Over', 'Ford', 'Kittle', 'Under', 'Over', 'Yes', '49ers', '49ers', 'Chiefs', 'Garropolo', 'Under', 'Yellow', 'Get Right', 'Teammates', '49ers 27 - 24', 'Yes'],
['Sacke', 'Over', 'Under', 'Andy Reid', 'Over', 'No', 'Tails', '49ers', 'Pass', 'TD', 'Kelce', 'Kittle', 'Chiefs', '49ers', 'Gould', 'Mahomes', 'Chiefs', 'Garropolo', 'Clark', 'No', 'No', 'Kelce', 'Mostert', 'Under', 'Under', 'Under', 'Under', 'Buckner', 'Watkins', 'Over', 'Over', 'No', 'Chiefs', 'Chiefs', 'Chiefs', 'Mahomes', 'Over', 'Red', "Love don't cost a thing", 'Family', 'Chiefs 31 - 24', 'Yes'],
['Chaikof', 'Under', 'Under', 'Andy Reid', 'Under', 'Yes', 'Heads', '49ers', 'Run', 'TD', 'Kittle', 'Williams', '49ers', '49ers', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Buckner', 'No', 'No', 'Watkins', 'Mostert', 'Over', 'Over', 'Over', 'Over', 'Buckner', 'Kittle', 'Over', 'Under', 'No', '49ers', '49ers', 'Chiefs', 'Mostert', 'Under', 'Red', 'If you had my love', 'God', '49ers 28 - 25 ', 'Yes'],
['Erdman', 'Over', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', '49ers', 'Run', 'FG', 'Hardman', 'Kelce', '49ers', 'Chiefs', 'Gould', 'Mahomes', '49ers', 'Williams', 'Buckner', 'No', 'No', 'Kelce', 'Mostert', 'Under', 'Under', 'Over', 'Over', 'Armstead', 'Samuel', 'Under', 'Over', 'No', '49ers', 'Chiefs', 'Chiefs', 'Mahomes', 'Over', 'Yellow', 'She wolf', 'Teammates', 'Chiefs 32 - 28', 'Yes'],
['Tyberg', 'Under', 'Under', 'Andy Reid', 'Under', 'Yes', 'Heads', '49ers', 'Run', 'FG', 'Samuel', 'Mostert', '49ers', '49ers', 'Gould', 'Mahomes', 'Chiefs', 'Garropolo', 'Ford', 'No', 'No', 'Kittle', 'Mostert', 'Over', 'Over', 'Under', 'Under', 'Clark', 'Kittle', 'Under', 'Over', 'No', '49ers', 'Chiefs', 'Chiefs', 'Garropolo', 'Over', 'Purple', 'Get Right', 'Teammates', '49ers 31 - 27', 'Yes'],
['Nadav & Yoni', 'Under', 'Under', 'Shanahan', 'Over', 'No', 'Heads', '49ers', 'Pass', 'TD', 'Hill', 'Mostert', 'Chiefs', '49ers', 'Butker', 'Mahomes', 'Chiefs', 'Garropolo', 'Fuller', 'No', 'No', 'Hill', 'Mostert', 'Over', 'Over', 'Over', 'Under', 'Bosa', 'Kelce', 'Over', 'Under', 'Yes', 'Chiefs', '49ers', '49ers', 'Mahomes', 'Over', 'Red', "Let's Get Loud", 'God', 'Chiefs 35 - 28', ''],
['Jake ', 'Under', 'Over', 'Andy Reid', 'Under', 'No', 'Heads', 'Chiefs', 'Run', 'FG', 'Mostert', 'Kelce', '49ers', 'Chiefs', 'Gould', 'Mahomes', '49ers', 'Mahomes', 'Sherman', 'No', 'No', 'Kelce', 'Mostert', 'Under', 'Under', 'Over', 'Over', 'Buckner', 'Kittle', 'Under', 'Over', 'Yes', '49ers', 'Chiefs', 'Chiefs', 'Mahomes', 'Over', 'Purple', "Let's Get Loud", 'Teammates', 'Chiefs 28 - 27', ''],
['Gig', 'Under', 'Over', 'Andy Reid', 'Under', 'No', 'Tails', 'Chiefs', 'Run', 'TD', 'Kittle', 'Mostert', '49ers', 'Chiefs', 'Butker', 'Mahomes', '49ers', 'Garropolo', 'Ford', 'No', 'No', 'Hardman', 'Coleman', 'Over', 'Over', 'Under', 'Over', 'Ford', 'Sanders', 'Over', 'Over', 'Yes', '49ers', '49ers', 'Chiefs', 'Kittle', 'Over', 'Red', "Let's Get Loud", 'Teammates', '49ers 31 -28', 'Yes'],
['Ambar', 'Over', 'Over', 'Shanahan', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'TD', 'Kelce', 'Sanders', 'Chiefs', '49ers', 'Gould', 'Mahomes', '49ers', 'Williams', 'Buckner', 'No', 'No', 'Hill', 'Mostert', 'Over', 'Under', 'Over', 'Over', 'Bosa', 'Robinson', 'Over', 'Over', 'Yes', '49ers', 'Chiefs', '49ers', 'Mahomes', 'Under', 'Yellow', 'On the floor', 'God', 'Chiefs 31 - 21', ''],
['Omri Chazot', 'Under', 'Under', 'Shanahan', 'Over', 'No', 'Heads', 'Chiefs', 'Run', 'TD', 'Samuel', 'Kelce', '49ers', 'Chiefs', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Sherman', 'No', 'No', 'Kittle', 'Mostert', 'Over', 'Under', 'Over', 'Over', 'Clark', 'Sanders', 'Under', 'Over', 'No', '49ers', 'Chiefs', '49ers', 'Garropolo', 'Over', 'Orange', "Let's Get Loud", 'Teammates', '49ers 38 - 27', 'Yes'],
['Josh ', 'Over', 'Under', 'Andy Reid', 'Under', 'No', 'Tails', 'Chiefs', 'Run', 'TD', 'Hill', 'Mostert', 'Chiefs', '49ers', 'Butker', 'Mahomes', '49ers', 'Garropolo', 'Mathieu', 'No', 'No', 'Hill', 'Mostert', 'Under', 'Over', 'Under', 'Under', 'Bosa', 'Kittle', 'Over', 'Under', 'No', 'Chiefs', '49ers', '49ers', 'Mahomes', 'Over', 'Purple', 'Get Right', 'Teammates', 'Chiefs 34 - 28', 'Yes'],
['Chad ', 'Under', 'Under', 'Andy Reid', 'Over', 'No', 'Heads', '49ers', 'Run', 'TD', 'Kelce', 'Mostert', 'Chiefs', '49ers', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Sherman', 'No', 'No', 'Hill', 'Mostert', 'Under', 'Under', 'Under', 'Under', 'Bosa', 'Samuel', 'Under', 'Over', 'No', 'Chiefs', '49ers', 'Chiefs', 'Mahomes', 'Under', 'Red', 'Medicine', 'Teammates', 'Chiefs 30 - 24', 'Yes'],
['Rachel Gershman', 'Over', 'Under', 'Shanahan', 'Under', 'No', 'Tails', '49ers', 'Pass', 'FG', 'Mostert', 'Mostert', '49ers', '49ers', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Sherman', 'No', 'No', 'Kittle', 'Mostert', 'Over', 'Over', 'Over', 'Under', 'Bosa', 'Kittle', 'Under', 'Over', 'Yes', '49ers', '49ers', 'Chiefs', 'Kittle', 'Under', 'Red', "Let's Get Loud", 'Teammates', '49ers 28 - 24 ', 'Yes'],
['Shayne', 'Over', 'Over', 'Andy Reid', 'Over', 'Yes', 'Heads', 'Chiefs', 'Run', 'TD', 'Mostert', 'Kelce', '49ers', '49ers', 'Butker', 'Mahomes', 'Chiefs', 'Garropolo', 'Mathieu', 'No', 'No', 'Hill', 'Mostert', 'Over', 'Under', 'Under', 'Over', 'Clark', 'Samuel', 'Over', 'Over', 'No', '49ers', 'Chiefs', 'Chiefs', 'Garropolo', 'Over', 'Red', 'On the floor', 'Teammates', '49ers 31 - 27', ''],
['Mitch ', 'Under', 'Over', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Run', 'TD', 'Samuel', 'Kittle', '49ers', '49ers', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Buckner', 'No', 'Yes', 'Kittle', 'Mostert', 'Under', 'Under', 'Under', 'Over', 'Buckner', 'Samuel', 'Over', 'Over', 'No', '49ers', 'Chiefs', 'Chiefs', 'Garropolo', 'Over', 'Yellow', 'Whenever, Whenever', 'God', '49ers 34 - 28', ''],
['Jeremy', 'Over', 'Under', 'Andy Reid', 'Under', 'No', 'Tails', 'Chiefs', 'Run', 'FG', 'Mostert', 'Mostert', '49ers', 'Chiefs', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Warner', 'No', 'No', 'Kelce', 'Mostert', 'Over', 'Under', 'Under', 'Under', 'Armstead', 'Williams', 'Under', 'Over', 'Yes', '49ers', '49ers', '49ers', 'Garropolo', 'Under', 'Red', 'Jenny from the block', 'Teammates', '49ers 28 - 24 ', 'Yes'],
['K Baum', 'Under', 'Over', 'Andy Reid', 'Under', 'No', 'Heads', 'Chiefs', 'Run', 'FG', 'Mostert', 'Kelce', '49ers', 'Chiefs', 'Butker', 'Mahomes', '49ers', 'Mahomes', 'Bosa', 'No', 'No', 'Kelce', 'Mostert', 'Under', 'Under', 'Under', 'Over', 'Bosa', 'Williams', 'Over', 'Over', 'No', 'Chiefs', 'Chiefs', '49ers', 'Mahomes', 'Under', 'Yellow', 'Get Right', 'Teammates', 'Chiefs 27 - 20', 'Yes'],
['Jake R', 'Over', 'Under', 'Andy Reid', 'Under', 'No', 'Heads', 'Chiefs', 'Run', 'TD', 'Kelce', 'Mostert', 'Chiefs', '49ers', 'Gould', 'Mahomes', '49ers', 'Williams', 'Bosa', 'No', 'No', 'Hill', 'Mostert', 'Under', 'Under', 'Under', 'Over', 'Clark', 'Kelce', 'Under', 'Over', 'Yes', 'Chiefs', '49ers', '49ers', 'Mahomes', 'Under', 'Yellow', 'She wolf', 'God', 'Chiefs 27-24', ''],
['Joe', 'Over', 'Over', 'Andy Reid', 'Over', 'No', 'Heads', '49ers', 'Pass', 'TD', 'Hardman', 'Hill', 'Chiefs', '49ers', 'Gould', 'Mahomes', '49ers', 'Garropolo', 'Mathieu', 'No', 'Yes', 'Watkins', 'Williams', 'Under', 'Over', 'Under', 'Over', 'Clark', 'Hill', 'Under', 'Over', 'Yes', 'Chiefs', '49ers', '49ers', 'Mahomes', 'Over', 'Yellow', "Hips don't lie", 'Family', 'Chiefs 34 - 24', 'Yes'],
['Quaglia', 'Under', 'Over', 'Andy Reid', 'Over', 'Yes', 'Tails', '49ers', 'Run', 'FG', 'Kittle', 'Kelce', '49ers', 'Chiefs', 'Butker', 'Mahomes', '49ers', 'Garropolo', 'Bosa', 'No', 'No', 'Kelce', 'Mostert', 'Over', 'Under', 'Under', 'Over', 'Bosa', 'Kittle', 'Under', 'Under', 'No', '49ers', 'Chiefs', '49ers', 'Mahomes', 'Over', 'Yellow', "Hips don't lie", 'Teammates', 'Chiefs 35 - 28', 'Yes'],
['Chubbs', 'Over', 'Under', 'Andy Reid', 'Under', 'Yes', 'Tails', 'Chiefs', 'Pass', 'TD', 'Kelce', 'Kelce', 'Chiefs', 'Chiefs', 'Butker', 'Mahomes', 'Chiefs', 'Garropolo', 'Mathieu', 'No', 'No', 'Kelce', 'Mostert', 'Over', 'Under', 'Under', 'Over', 'Bosa', 'Kelce', 'Over', 'Over', 'Yes', 'Chiefs', 'Chiefs', '49ers', 'Mahomes', 'Over', 'Red', 'She wolf', 'God', 'Chiefs 35 - 27', 'Yes'],
['Ophir', 'Under', 'Under', 'Andy Reid', 'Over', 'Yes', 'Heads', '49ers', 'Run', 'FG', 'Kelce', 'Kelce', '49ers', 'Chiefs', 'Gould', 'Mahomes', '49ers', 'Mahomes', 'Bosa', 'No', 'No', 'Hill', 'Mostert', 'Over', 'Over', 'Over', 'Under', 'Bosa', 'Kelce', 'Over', 'Over', 'Yes', '49ers', 'Chiefs', '49ers', 'Garropolo', 'Over', 'Orange', "Hips don't lie", 'Teammates', '49ers 31 - 27', ''],
['Ryan O', 'Over', 'Under', 'Andy Reid', 'Over', 'No', 'Heads', '49ers', 'Run', 'TD', 'Kittle', 'Williams', 'Chiefs', '49ers', 'Gould', 'Mahomes', '49ers', 'Mahomes', 'Sherman', 'No', 'Yes', 'Kelce', 'Mostert', 'Over', 'Under', 'Under', 'Under', 'Bosa', 'Kelce', 'Over', 'Over', 'No', 'Chiefs', '49ers', 'Chiefs', 'Mahomes', 'Over', 'Clear', "Let's Get Loud", 'Teammates', 'Chiefs 41 - 34', 'Yes'],
['Adam Sinclair', 'Over', 'Over', 'Andy Reid', 'Over', 'Yes', 'Tails', 'Chiefs', 'Pass', 'TD', 'Coleman', 'Hill', '49ers', 'Chiefs', 'Gould', 'Mahomes', '49ers', 'Williams', 'Bosa', 'No', 'Yes', 'Watkins', 'Coleman', 'Under', 'Over', 'Under', 'Over', 'Bosa', 'Watkins', 'Under', 'Over', 'No', '49ers', '49ers', 'Chiefs', 'Mahomes', 'Over', 'Yellow', 'Jenny from the block', 'Teammates', 'Chiefs 31 - 28', 'Yes']]

df = pd.DataFrame(data, columns=['Name', 'Anthem (2:04)', 'Total number of Jackson Mahomes Tik Toks during the Super Bowl Sunday (The whole day) (Over/under 6.5 times)', 'Who is show first on TV during the anthem', "Will the Total Points scored in the 1st half be Over/Under Pascal Siakam's Point Total vs. Bulls of Feb. 2nd", "Will Travis Kelce and Tyreek Hill combine to catch more balls than Giannis Antetokounmpo's Rebound total against the Suns on Feb. 2nd", 'Coin Toss', 'Team to win Coin Toss', 'First Play', 'First type of score', 'First Touchdown Scorer ', 'Last Touchdown Scorer ', 'Team to score first', 'Team to score Last', 'Player to hit First Field Goal', 'Most Throwing Yards', 'First Takeaway', 'First Player to Commit a Turnover', 'First playe to force a turnover ', 'Will there be a safety', 'Will there be a D/ST TD', 'Lead Receiver', 'Lead Rusher', 'Total Sacks (4.5)', 'Total TO (2.5)', 'Total Penalties Accepted (12.5)', 'Longest TD (45.5)', 'First Sack', 'Player to Catch the 1st pass', 'Shortest TD (1.5)', 'Longest FG (43.5)', 'Succesful 2 point conversion', 'Leading at half', 'Team to have First Coaches Challenge', 'First Timeout', 'Super Bowl MVP (3 Points)', 'Total Points (54.5)', 'Gatorade Color (2 Points)', 'First song (2 Points)', 'Who does MVP Thank first', 'Score of game', 'Paid'])


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