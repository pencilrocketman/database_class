import numpy as np
import pandas as pd
import csv
shots = pd.read_csv('shots.csv')

tmp = 0
memo = {}
entries = shots[["PLAYER_NAME", "SHOT_ZONE_BASIC", "SHOT_ZONE_AREA"]]
stock = {}

for index, row in entries.iterrows():
    shot_type = row['SHOT_ZONE_BASIC'] + row['SHOT_ZONE_AREA']
    if shot_type in memo.keys():
        if row["PLAYER_NAME"] in stock.keys():
            stock[row["PLAYER_NAME"]][memo[shot_type]] += 1
        else:
            stock[row["PLAYER_NAME"]] = [0] * 16
            stock[row["PLAYER_NAME"]][memo[shot_type]] += 1
    else:
        memo[shot_type] = tmp
        tmp += 1
        if row["PLAYER_NAME"] in stock.keys():
            stock[row["PLAYER_NAME"]][memo[shot_type]] += 1
        else:
            stock[row["PLAYER_NAME"]] = [0] * 16
            stock[row["PLAYER_NAME"]][memo[shot_type]] += 1


with open('new_shots.csv', 'w') as f:
    writer = csv.writer(f, lineterminator = '\n')
    for k, v in stock.items():
        new_array = list(map(lambda n: round(100*n/sum(v), 1), v))
        new_array.insert(0, k)
        writer.writerow(new_array)

print(memo)
