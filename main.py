import pandas as pd
import numpy as np




def update_scores(df2, results):
    for index, row in df2.iterrows():
        count = 0
        for k in range(len(row.index)):
            if row.index[k] == "score":
                break
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




def main():
    df = pd.read_excel("Chiefsvs49ers.xlsx")
    df2 = df.append(pd.Series(name="results"))
    score = [0] * len(df2)
    df2["score"] = score



    results = df2.loc["results"]
    keys = results.keys()
    flag = True
    while flag:

        print("Please select the number of the item to update:")
        k = 1
        for result in keys:
            print("{}: {}".format(k, result))
            k += 1
        print("q: quit")

        user_choice = int(input("Enter Selection: "))
        # check to see if user wants to quit
        if user_choice == "q":
            flag = False
            break

        # update item
        item_to_update = keys[user_choice - 1]
        value = input("Enter result of item: ")
        results[item_to_update] = value

        df2 = update_scores(df2, results)
        standings = get_scores_sorted(df2)
        print(standings)




    results["Anthem (2:04)"] = "Over"
    results["Total number of Jackson Mahomes Tik Toks during the Super Bowl Sunday (The whole day) (Over/under 6.5 times)"] = "Under"
    results["Who is show first on TV during the anthem"] = "Andy Reid"






main()






"""


vals = df.values

bets = ['bet1', 'bet2', 'bet3', 'bet4', 'bet5', 'bet6']
bet_results = ["over", "over", "mahomes", "gronk", "2", "under"]
dict = {}
for k in range(len(bets)):
    print("{}: {}. Current result is: {}".format(k, bets[k], bet_results[k]))


ryans_bets = ["over", "under", "mahomes", "brady", "3", "under"]
gabe_bets = ["under", "under", "brady", "gronk", "2", "over"]
shu_bets = ["over", "over", "brady", "gronk", "2", "over"]

dict = {"Ryan Kirshenbaum": [ryans_bets,0] , "Gabe Gutfrajnd": [gabe_bets,0], "Daniel Shuman": [shu_bets,0]}

keys = dict.keys()
winner = ""
max = 0

for i in dict.keys():
    choices = dict.get(i)
    for k in range(len(bet_results)):

        if choices[0][k] == bet_results[k]:
            choices[1] += 1
    if choices[1] > max:
        max = choices[1]
        winner = i

print("The current leader is {} with a score of {}.".format(winner, max))

"""




